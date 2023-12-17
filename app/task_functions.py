import csv

import psycopg2
from psycopg2 import sql

from app.settings import settings

db_params = {
    'host': settings.DB_HOST,
    'port': settings.DB_PORT,
    'user': settings.DB_USER,
    'password': settings.DB_PASSWORD,
    'database': settings.DB_NAME
}


def get_faers_data():
    print()
    query = sql.SQL("SELECT * FROM combined.faers_combined LIMIT 10000")
    csv_file_path = 'output_data.csv'
    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                data = cur.fetchall()
    except psycopg2.Error as e:
        print(f"Error: {e}")
        raise Exception("Failed to fetch data from database")

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)
        print(f"Data has been saved to {csv_file_path}")
    return csv_file_path
