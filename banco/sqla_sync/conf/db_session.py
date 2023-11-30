import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine  # Import corrigido

from models.model_base import ModelBase

#from conf.db_session import create_tables

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False) -> Engine:
    """
    Função de criar o banco de dados
    """
    global __engine

    if __engine:
        return
    
    if sqlite: 
        arquivo_db = 'db/filmes.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        conn_str = ""
    
    return __engine

def create_session() -> Session:
    """
    Função de criar a sessão de conexão do banco de dados
    """
    global __engine
    
    if not __engine:
        create_engine(sqlite=True)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session

def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine(sqlite=True)
    
    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
