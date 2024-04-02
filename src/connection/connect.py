import logging
import psycopg2
import sys

sys.path.append(".")
from src.connection.config import get_config_param

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def connect(config=get_config_param()):
    with psycopg2.connect(**config) as conn:
        logging.info('Connected to the PostgreSQL server.')
        return conn


if __name__ == '__main__':
    connect(get_config_param())
