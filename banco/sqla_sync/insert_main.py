from conf.db_session import create_session
from models.filmes import Filme
from datetime import datetime
import pandas as pd

def insert_filme() -> None:
    print('Cadastrando Filme')

    movie: str = input('Informe o nome do Filme: ')
    released_year_str: str = input('Informe o Ano de lançamento do Filme: ')
    director: str = input('Nome do diretor do Filme: ')
    rating_str: str = input('Qual a Nota que vc da para o filme entre 0.0 a 10.0:')

    try:
        released_year = pd.to_datetime(released_year_str)
        rating = float(rating_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

    lf: Filme = Filme(movie=movie, released_year=released_year, director=director, rating=rating)

    with create_session() as session:
        session.add(lf)
        session.commit()

    print('Sucesso')
    print(f'ID: {lf.id}')
    print(f'Filme: {lf.movie}')
    print(f'Ano de lançamento: {lf.released_year}')
    print(f'Diretor: {lf.director}')
    print(f'Avaliação: {lf.rating}')

if __name__ == '__main__':
    insert_filme()
