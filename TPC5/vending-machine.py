import json
from datetime import datetime

def print_machine_info(message: str):
    print("maq: " + message)

def get_date() -> str:
    return datetime.today().strftime('%Y-%m-%d')

def load_stock(filename: str) -> list(dict()):
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def handle_restock(stock: list(dict())):
    print_machine_info("Produtos Disponiveis:")

    for index, item in enumerate(stock):
        print(f'{index + 1}. {item['nome']} (Código: {item['cod']}, Quantidade: {item['quant']}, Preço: €{item['preco']:.2f})')

    input('>> ')

def parse_input(stock: list(dict())):
    input_str = input('>> ')

    match (input_str.lower()):
        case 'repor':
            handle_restock(stock)
        case _:
            print('Operação ' + input_str + ' não implementada.')

if __name__ == "__main__":
    current_stock = load_stock("stock.json")

    print_machine_info(get_date() + ', Stock carregado, Estado atualizado.')

    if not current_stock:
        print_machine_info('Não foram encontrados produtos em stock.')
    else:
        print_machine_info('Bom dia. EStou disponível para atender o seu pedido.')
        parse_input(current_stock)
