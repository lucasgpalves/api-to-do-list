import os
import psycopg2
from dotenv import load_dotenv

class ConnectionDB:
    
    load_dotenv(dotenv_path='.env')
    
    # Conexão ao banco de dados PostgreSQL
    def init_connection():
        try:
            print("Connection established")
            return psycopg2.connect(
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_ADDRESS"),
                port=os.getenv("DB_PORT"),
                client_encoding="UTF8"
            )
        except Exception as e:
            print(f"Connection cannot be established: {e}")
            exit(1)  # Encerra o programa se a conexão falhar