from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"  # Corrigindo a formatação da string de conexão
        self.__engine = None
        self.session = None
        
    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)
        
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)  # Vinculando o sessionmaker ao engine
        self.session = session_maker()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


with DBConnectionHandler() as db_handler:
    db_handler.connect_to_db()