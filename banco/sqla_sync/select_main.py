from typing import List
from conf.helpers import formata_data
from conf.db_session import create_session
from models.filmes import Filme

def select_todos_filmes() -> None:
    with create_session() as session:
        filmes: List[Filme] = session.query(Filme).all()

        for lf in filmes:
            print(f'ID: {lf.id}')
            print(f'Filme: {lf.movie}')
            print(f'Ano de lançamento: {formata_data(lf.released_year)}')
            print(f'Diretor: {lf.director}')
            print(f'Avaliação: {lf.rating}')
            print('\n')  # Adicione uma linha em branco entre os filmes

def select_filtro_nome(nome_filme: str) ->None:
    with create_session() as session:
        nomes_filtrados: List[Filme] = session.query(Filme).filter(Filme.movie == nome_filme ).all() #.first() .one_or_none()
        if not nomes_filtrados:
            print(f'Nenhum filme encontrado com o nome "{nome_filme}"')
            return

        for lf in nomes_filtrados:
            print(f'ID: {lf.id}')
            print(f'Filme: {lf.movie}')
            print(f'Ano de lançamento: {formata_data(lf.released_year)}')
            print(f'Diretor: {lf.director}')
            print(f'Avaliação: {lf.rating}')
            print('\n')  # Adicione uma linha em branco entre os filmes


if __name__ == '__main__':
    select_todos_filmes()
