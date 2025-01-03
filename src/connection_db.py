import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

class ConnectionDB:

    load_dotenv(dotenv_path='.env')

    @staticmethod
    def init_connection():
        try:
            db_url = (
                f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
                f"@{os.getenv('DB_ADDRESS')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
            )
            
            engine = create_engine(db_url, echo=False)  # echo=True exibe as queries no log
            Session = sessionmaker(bind=engine)

            print("Connection established")
            return Session
        except Exception as e:
            print(f"Connection cannot be established: {e}")
            exit(1)     
        
    @staticmethod
    def get_session():
        Session = ConnectionDB.init_connection()
        session = Session()
        try:
            yield session
        finally:
            session.close()