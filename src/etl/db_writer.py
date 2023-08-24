import psycopg2
from psycopg2 import sql

class local_database_creator:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to the database")
        except psycopg2.Error as e:
            print("Error: Unable to connect to the database")
            print(e)

    def create_table(self, table_name, columns):
        if not self.connection:
            print("Not connected to the database")
            return
        
        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({});").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(
                sql.SQL("{} {}").format(
                    sql.Identifier(column_name),
                    sql.SQL(data_type)
                )
                for column_name, data_type in columns.items()
            )
        )

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_table_query)
            self.connection.commit()
            print(f"Table '{table_name}' created successfully")
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error creating table '{table_name}'")
            print(e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")

