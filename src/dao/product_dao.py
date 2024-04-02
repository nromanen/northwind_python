import sys
sys.path.append(".")
from src.connection.connect import connect
from src.model.product import Product


def get_products(filter = ""):
    """Takes in an optional condition for query.
    Don't type `where` word if you need usage query with condition"""

    result = []
    query = f'SELECT * from products {f"where {filter}" if len(filter) > 0 else ""}'
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                dict_row = {}
                for index, value in enumerate(cur.description):
                    dict_row[value[0]] = row[index]
                result.append(Product(**dict_row))
        return result


if __name__ == '__main__':
    print([elem for elem in get_products("product_id < 4")])
