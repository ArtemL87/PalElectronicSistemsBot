import pandas as pd
import sqlite3  # можно заменить на psycopg2 для PostgreSQL или pymysql для MySQL


def excel_sql():
    # Загружаем Excel
    df = pd.read_excel("data.xlsx", sheet_name="Sheet")

    # Подключаемся к базе SQLite (или другой)
    conn = sqlite3.connect("mydb.sqlite")

    # Записываем данные в таблицу
    df.to_sql("my_table", conn, if_exists="replace", index=False)

    conn.close()


excel_sql()
