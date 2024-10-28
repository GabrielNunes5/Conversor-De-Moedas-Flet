import requests, os

API_KEY = os.getenv("API_KEY")

def cambio(base_moeda: str, destino_moeda: str, quantidade: float):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_moeda}/{destino_moeda}/{quantidade}"
    response = requests.get(url)
    cotacao = response.json()
    val_considerado = response.json()

    # Tratamento de erro
    if cotacao.get("result") == "error":
        error_type = cotacao.get("error-type")
        
        if error_type == "unsupported-code":
            return "Erro: Código de moeda não suportado."
        elif error_type == "malformed-request":
            return "Erro: Requisição malformada."
        elif error_type == "invalid-key":
            return "Erro: API key inválida."
        elif error_type == "inactive-account":
            return "Erro: Conta inativa, confirme o e-mail."
        elif error_type == "quota-reached":
            return "Erro: Limite de requisições atingido."
        else:
            return error_type
    
    # Caso não haja erro, retorna os valores de conversão
    return cotacao.get("conversion_result"), val_considerado.get("conversion_rate")