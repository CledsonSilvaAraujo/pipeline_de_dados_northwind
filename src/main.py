
from etl.extrator_csv import extrator_csv
from etl.extrator_postgresql import extrator_postgres
from etl.csv_writer import csv_writer
from utils.folder_generator import folder_generator
import os
def main():
    
    #setup folders
    directory_generator = folder_generator()
    directory_generator.generate_folder('csv')
    directory_generator.generate_folder('postgres')

    # Extrair Arquivo CSV
    csv_reader = extrator_csv("./data/order_details.csv")
    data = csv_reader.read_csv()


    # Inserir os dados do CSV
    cabecalho = ["order_id","product_id","unit_price","quantity","discount"]
    nome_arquivo = "./output_order_details.csv"
    writer = csv_writer(nome_arquivo, cabecalho)
    for row in data:
        writer.adicionar_linha(row)
    writer.escrever_csv()


    #Extrair Banco de Dados
    db_reader = extrator_postgres(
        dbname="northwind",
        user="northwind_user",
        password="thewindisblowing",
        host="localhost",
        port="5432"
    )
    db_reader.connect()
    
    list_of_tables = ['categories','products','suppliers','customers','customer_customer_demo','customer_demographics','shippers','us_states','region','territories','employee_territories','employees']
    for table in list_of_tables:

        query = "SELECT * FROM {}".format(table)
        data = db_reader.execute_query(query)
        
        for row in data:
            print(row)
    db_reader.disconnect()

    # Criar banco de dados
    # Exemplo de uso
if __name__ == "__main__":
    db = local_database_creator(dbname="mydb", user="myuser", password="mypassword")
    db.connect()
    
    table_columns = {
        "id": "SERIAL PRIMARY KEY",
        "name": "VARCHAR(255)",
        "age": "INT"
    }
    db.create_table(table_name="people", columns=table_columns)
    
    db.disconnect()

if __name__ == "__main__":
    main()
