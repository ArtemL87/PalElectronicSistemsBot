import pandas as pd
import sqlite3  # можно заменить на psycopg2 для PostgreSQL или pymysql для MySQL


def excel_sql(doc):
    # Загружаем Excel
    df = pd.read_excel(doc, sheet_name="Sheet")

    # Подключаемся к базе SQLite (или другой)
    conn = sqlite3.connect("../database.db")

    # Записываем данные в таблицу
    df.to_sql("scores", conn, if_exists="replace", index=False)

    conn.close()

    # Загружаем Excel
    df = pd.read_excel(doc, sheet_name="Лист1")

    # Подключаемся к базе SQLite (или другой)
    conn = sqlite3.connect("../database.db")

    # Записываем данные в таблицу
    df.to_sql("phones", conn, if_exists="replace", index=False)

    conn.close()
