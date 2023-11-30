from conf.db_session import create_session
from select_main import select_filtro_nome, formata_data  # Importe a função select_filtro_nome e formata_data de select_main
from models.filmes import Filme

def atualizar_filme_por_nome(nome_filme: str, novos_dados: dict) -> None:
    with create_session() as session:
        # Consulta o filme pelo nome
        filme = session.query(Filme).filter_by(movie=nome_filme).first()

        if not filme:
            print(f'Filme com o nome "{nome_filme}" não encontrado.')
            return

        # Atualiza os dados do filme com os novos dados fornecidos
        for campo, valor in novos_dados.items():
            setattr(filme, campo, valor)

        # Confirma a transação
        session.commit()

        print(f'Filme com o nome "{nome_filme}" foi atualizado com sucesso.')

# Exemplo de uso
if __name__ == '__main__':
    # Substitua 'NOME_DO_FILME' pelo nome real do filme que você deseja atualizar
    nome_filme_para_atualizar = 'teste'

    # Substitua os campos e valores pelos dados que você deseja atualizar
    dados_atualizados = {
        'released_year': '2023-01-01',  # Substitua pela nova data de lançamento
        'rating': 7.0,  # Substitua pela nova avaliação
        'director': 'Carrinho',
    }

    # Chamada da função de seleção correta
    # ...
    filmes_encontrados = select_filtro_nome(nome_filme_para_atualizar)

    print(f'Filmes encontrados para o nome "{nome_filme_para_atualizar}": {filmes_encontrados}')

    if filmes_encontrados:
        # Atualiza o primeiro filme encontrado (assumindo que o nome é único)
        atualizar_filme_por_nome(filmes_encontrados[0].movie, dados_atualizados)
    else:
        print(f'Nenhum filme encontrado com o nome "{nome_filme_para_atualizar}".')

