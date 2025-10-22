import pandas as pd
import httpx
from airflow.sdk import dag, task


@task()
def download_dados_dos_clientes() -> str:
    """
    Faz o download dos dados dos clientes e salva num csv localmente.

    Retorna o nome do arquivo local.
    URL: https://azcnfwcdcj.s3.us-east-1.amazonaws.com/clientes.csv.zip
    """
    ...


@task()
def download_dados_dos_produtos() -> str:
    """
    Faz o download dos dados dos produtos e salva num csv localmente.

    Retorna o nome do arquivo local.
    URL: https://azcnfwcdcj.s3.us-east-1.amazonaws.com/produtos.csv.zip
    """
    ...


@task()
def download_dados_dos_pedidos() -> str:
    """
    Faz o download dos dados dos pedidos e salva num csv localmente.

    Retorna o nome do arquivo local.
    URL: https://azcnfwcdcj.s3.us-east-1.amazonaws.com/pedidos.csv.zip
    """
    ...


@task()
def transformar(
    arquivo_clientes: str,
    arquivo_produtos: str,
    arquivo_pedidos: str,
) -> None:
    """
    Transforma os dados normalizados dos clientes, produtos e pedidos.

    O resultado final deve ser salvo num arquivo csv local.
    O resultado final deve ser uma tabela com somente duas colunas:
        nome_do_cliente
        total

    O "total" de um pedido = "preco * (1 - desconto)"
    A coluna "total" é a soma dos totais de todos os pedidos para o cliente.
    """
    ...



@dag()
def processa_dados_de_vendas():
    """
    Dag para processar os dados de vendas.

    Primeiro deve ser feito o download dos dados.
    O download dos tres são independentes (um não precisa esperar pelo outro).

    Depois os dados devem ser transformados.
    A tarefa de transformar deve aguardar todos os tres downloads para começar.
    """
    ...

    a = download_dados_dos_clientes()
    b = download_dados_dos_produtos()
    c = download_dados_dos_pedidos()
    transformar(a, b, c)



# processa_dados_de_vendas()
