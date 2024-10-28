# Conversor de Moedas

Este é um projeto simples de Conversor de Moedas desenvolvido em Python, utilizando uma API externa para realizar a conversão de moedas em tempo real. A interface gráfica é implementada com a biblioteca Flet.

## 📋 Informações Gerais do Projeto

- **Linguagem:** Python
- **Bibliotecas utilizadas:**
  - `requests` para requisições HTTP
  - `flet` para a interface gráfica
- **Objetivo:** Facilitar a conversão de valores entre diferentes moedas de forma prática e rápida.
- **Funcionalidade:** O usuário insere o valor a ser convertido, a moeda de origem e a moeda de destino. A aplicação então faz a consulta de conversão e exibe o resultado.

## 🚀 Como Clonar o Projeto

Para clonar este repositório, basta executar o seguinte comando:

```bash
git clone https://github.com/GabrielNunes5/Conversor-De-Moedas-Flet.git
cd Conversor-De-Moedas-Flet
```

## 🔑 Configuração de Variáveis de Ambiente
O projeto utiliza a chave de API para o serviço de câmbio. Para configurar a variável de ambiente, siga as instruções:
- **Crie uma conta em ExchangeRate API para obter uma chave de API.**
- **Crie um arquivo .env na raiz do projeto e insira a variável:**
```bash
API_KEY="sua_api_key_aqui"
```
- **Certifique-se de que o arquivo .env esteja no .gitignore para manter sua chave de API segura.**

## 🛠️ Como Rodar o Projeto
- **Instale as dependências necessárias:**
```bash
pip install -r requirements.txt
```
- **Execute a aplicação:**
```bash
python app.py
```
- **A interface do Conversor de Moedas será iniciada em uma nova janela.**

## 🌟 Funcionalidades do Projeto
- **Conversão entre moedas: Converte valores entre diferentes moedas com base na taxa de câmbio atual.**
- **Interface amigável: Interface intuitiva para facilitar a entrada de dados e exibição do resultado.**
- **Tratamento de erros: Mensagens de erro são exibidas para problemas comuns, como chave de API inválida, moedas não suportadas, etc.**

## 📸 Imagem do Projeto
![Interface do Conversor de Moedas](https://i.ibb.co/6mwZsPq/Conversor-de-Moedas-27-10-2024-22-44-59.png)
![Interface do Conversor de Moedas](https://i.ibb.co/F5dztLy/Conversor-de-Moedas-27-10-2024-22-50-03.png)
![Interface do Conversor de Moedas](https://i.ibb.co/71y23ND/Conversor-de-Moedas-27-10-2024-22-45-19.png)
