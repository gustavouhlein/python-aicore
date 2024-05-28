# AI Core | Sistema de Assistente com IA

Este repositório apresenta um sistema de assistente que utiliza tecnologias de inteligência artificial para fornecer suporte eficiente aos usuários. O assistente é configurado para responder perguntas com precisão, baseando-se em uma base de conhecimento extraída de um arquivo CSV.

## Tecnologias Utilizadas

### Langchain

Langchain é uma biblioteca que facilita a criação de pipelines complexos para processamento de linguagem natural (NLP). No projeto, usamos:

- **Langchain Community Vectorstores (FAISS)**: Para realizar a busca vetorial eficiente dentro dos documentos da base de conhecimento.
- **Langchain OpenAI Embeddings**: Para gerar representações vetoriais das entradas de texto.
- **Langchain Prompts e Chains**: Para criar prompts personalizados e encadear modelos de linguagem para gerar respostas contextuais.

### OpenAI

Utilizamos a API do OpenAI para integrar o modelo de linguagem GPT-3.5-turbo, que é capaz de gerar respostas naturais e contextualizadas para as perguntas dos usuários.

### FAISS

Facebook AI Similarity Search (FAISS) é uma biblioteca que permite a busca eficiente e a recuperação de informações em grandes conjuntos de dados vetoriais. No projeto, FAISS é usado para realizar buscas na base de conhecimento e encontrar informações relevantes para as consultas dos usuários.

### Flask

Flask é um microframework para web em Python que nos permite criar uma API RESTful para o nosso assistente de IA. Usamos Flask para definir endpoints que permitem:

- Fazer perguntas ao assistente e obter respostas.
- Baixar a base de conhecimento.
- Fazer upload de uma nova base de conhecimento.

### Flask-CORS

Flask-CORS é uma extensão para Flask que permite o suporte a Cross-Origin Resource Sharing (CORS). Isso é essencial para permitir que o front-end de diferentes origens interaja com a API de maneira segura.

### Dotenv

A biblioteca `python-dotenv` é usada para carregar variáveis de ambiente a partir de um arquivo `.env`. Isso facilita a configuração e o gerenciamento de credenciais e outros parâmetros de configuração sensíveis.

## Endpoints da API

### `/api/ask` [POST]

Este endpoint recebe uma mensagem do usuário e retorna uma resposta gerada pelo assistente de IA.

### `/api/download_knowledge_base` [GET]

Este endpoint permite baixar o arquivo `knowledge_base.csv`, que contém a base de conhecimento.

### `/api/upload_knowledge_base` [POST]

Este endpoint permite o upload de um novo arquivo CSV para atualizar a base de conhecimento.

## Como Rodar o Projeto

1. Clone o repositório e navegue até o diretório do projeto.
2. Crie um ambiente virtual e instale as dependências.
3. Crie um arquivo `.env` com suas variáveis de ambiente, como chaves de API.
4. Inicie o aplicativo Flask.
