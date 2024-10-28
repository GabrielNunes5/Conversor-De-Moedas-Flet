import flet as ft
from api_cambio import cambio

def main(page: ft.Page):
    # Configurações da janela e layout
    page.padding = 12
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.title = "Conversor de Moedas"
    page.window.width = 400
    page.window.height = 500

    # Campos de entrada e exibição de resultado
    quantidade = ft.TextField(label="Valor a Converter", width=200)
    base_moeda = ft.TextField(label="Moeda Origem (ex: USD)", width=100)
    destino_moeda = ft.TextField(label="Moeda Destino (ex: EUR)", width=100)
    resultado = ft.Text(value="Resultado: ", size=20)
    taxa_conversao = ft.Text(value="", size=16, visible=False)

    # Função de conversão ao clicar
    def converter(e):
        # Extrair valores e realizar conversão
        try:
            # Substituir vírgula por ponto e converter para float
            valor_quantidade = float(quantidade.value.replace(',', '.'))
            info_moedas = cambio(base_moeda.value, destino_moeda.value, valor_quantidade)

            # Verifica se info_moedas é uma string (erro) ou um par de valores
            if isinstance(info_moedas, str):  # Se for uma mensagem de erro
                resultado.value = info_moedas  # Exibe a mensagem de erro
                taxa_conversao.visible = False  # Esconder taxa de conversão
            else:
                valor_convertido, val_considerado = info_moedas  # Desempacota os valores
                resultado.value = f"Resultado: {valor_convertido:.2f}"
                taxa_conversao.value = f"Valor considerado para conversão: {val_considerado:.4f}"
                taxa_conversao.visible = True  # Exibe a taxa de conversão

            page.update()

        except ValueError:
            resultado.value = "Erro: Valor inválido. Use um ponto ou uma vírgula para o separador decimal."
            taxa_conversao.visible = False
            page.update()


    # Botão para chamar a função de conversão
    btn_converter = ft.ElevatedButton(text="Converter", on_click=converter)

    # Adicionar elementos à página
    page.add(
        quantidade,
        base_moeda,
        destino_moeda,
        btn_converter,
        resultado,
        taxa_conversao
    )

if __name__ == "__main__":
    ft.app(target=main)
