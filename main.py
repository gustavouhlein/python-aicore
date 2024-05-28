from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

def load_documents():
    loader = CSVLoader(file_path="knowledge_base.csv", encoding='latin1')
    return loader.load()

documents = load_documents()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)
    return [doc.page_content for doc in similar_response]

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

template = """
Contexto: Você é um assistente de IA especializado no sistema X. Seu objetivo é ajudar os usuários a entender e utilizar o sistema, respondendo a perguntas e fornecendo informações detalhadas e precisas sobre suas funcionalidades, características, configuração, resolução de problemas e melhores práticas.
Instruções: Responda de forma clara e concisa. Caso necessário, forneça passos detalhados ou exemplos específicos para ajudar o usuário. Se a pergunta não for diretamente relacionada ao sistema X, não responda e oriente o usuário a procurar outra fonte.
Se você não tiver informações sobre a questão do usuário na base, não responda. Informe que não há informações na base de conhecimento e oriente a procura por suporte. 
Sua resposta será enviada diretamente ao usuário.
Pergunta do usuário: {message}
Base de conhecimento: {knowledge_base} 
Nota: Personalize as respostas conforme necessário e sempre verifique se a informação está atualizada e correta.
"""

prompt = PromptTemplate(
    input_variables=["message", "knowledge_base"],
    template=template
)

chain = LLMChain(prompt=prompt, llm=llm)

def generate_response(message):
    knowledge_base = retrieve_info(message)
    response = chain.run(message=message, knowledge_base=knowledge_base)
    return response

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message')
    if message:
        response = generate_response(message)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Informe a mensagem."}), 400

@app.route('/api/download_knowledge_base', methods=['GET'])
def download_knowledge_base():
    try:
        return send_file('knowledge_base.csv', as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/upload_knowledge_base', methods=['POST'])
def upload_knowledge_base():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado."}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nome do arquivo inválido."}), 400
    try:
        file.save('knowledge_base.csv')
        global documents, db
        documents = load_documents()
        db = FAISS.from_documents(documents, embeddings)
        return jsonify({"message": "Base de conhecimento atualizada com sucesso."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
