import sys
sys.path.append(".")
from src.model.category import Category

from src.connection.connect import connect

def get_categories(filter = ""):
    result = []
    query = f'SELECT * from categories {f"where {filter}" if len(filter) > 0 else ""}'
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                dict_row = {}
                for index, value in enumerate(cur.description):
                    dict_row[value[0]] = row[index]
                result.append(Category(**dict_row))
        return result


if __name__ == '__main__':
    print([elem for elem in get_categories()])
