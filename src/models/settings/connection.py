from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None
        
    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)
        
    def get_engine(self):
        return self.__engine
    
    def get_session(self):
        if self.session is None:
            Session = sessionmaker(bind=self.__engine)
            self.session = Session()
        return self.session
    
    def close_session(self):
        if self.session is not None:
            self.session.close()
            self.session = None
    
    def __enter__(self):
        self.connect_to_db()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_session()

db_handler = DBConnectionHandler()