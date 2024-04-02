import sys
sys.path.append(".")

from src.connection.connect import connect


def get_dict(query):
    result = []
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                dict_row = {}
                for index, value in enumerate(cur.description):
                    dict_row[value[0]] = row[index]
                result.append(dict_row)
        return result

if __name__ == '__main__':
    query = f'SELECT * from categories join products on categories.category_id = products.category_id where categories.category_id = 7'
    print([elem for elem in get_dict(query)])