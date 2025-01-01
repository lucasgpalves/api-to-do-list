import os
import psycopg2
from dotenv import load_dotenv

class ConnectionDB:
    
    load_dotenv(dotenv_path='.env')
    
    # print(f'DB_NAME={os.getenv("DB_NAME")}')
    # print(f'DB_USER={os.getenv("DB_USER")}')
    # print(f'DB_PASSWORD={os.getenv("DB_PASSWORD")}')
    # print(f'DB_ADDRESS={os.getenv("DB_ADDRESS")}')
    # print(f'DB_PORT={os.getenv("DB_PORT")}')
    
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