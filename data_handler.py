from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_user_info_by_email(cursor: RealDictCursor, email) -> list:
    query = """
            SELECT *
            FROM users
            WHERE email = %s"""
    cursor.execute(query, (email,))
    return cursor.fetchone()


@database_common.connection_handler
def add_user_info(cursor: RealDictCursor, first_name, last_name, email, password):
    query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%s, %s, %s, %s);
        """
    cursor.execute(query, (first_name, last_name, email, password,))

