from typing import Optional 
from util import obter_conexao 
from sql.produto_sql import * 
from models.produto_model import Produto 
 
 
def criar_tabela(): 
    with obter_conexao() as conexao: 
        db = conexao.cursor() 
        db.execute(SQL_CRIAR_TABELA) 
 
 
def inserir(produto: Produto) -> Optional[Produto]: 
    with obter_conexao() as conexao: 
        db = conexao.cursor() 
        db.execute(SQL_INSERIR,  
            (produto.nome, 
            produto.descricao, 
            produto.estoque, 
            produto.preco, 
            produto.categoria)) 
         
        if db.rowcount > 0: 
            produto.id = db.lastrowid 
            return produto 
        else: 
            return None 


def buscar_todos(): 
    with obter_conexao() as conexao: 
        db = conexao.cursor() 
        db.execute(SQL_OBTER_TODOS) 
        return db.fetchall()