from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common

# @database_common.connection_handler
# def get_data(cursor: RealDictCursor) -> list:
#     query = """
#             SELECT *
#             FROM question
#             ORDER BY id"""
#     cursor.execute(query)
#     return cursor.fetchall()


@database_common.connection_handler
def get_boards(cursor: RealDictCursor) -> list:
    query = """
            SELECT *
            FROM boards
            ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def add_board(cursor: RealDictCursor, title) -> list:
    query = """
            INSERT INTO boards (title)
            VALUES (%s);"""
    cursor.execute(query, (title,))

@database_common.connection_handler
def update_board_title(cursor: RealDictCursor, title) -> list:
    query = """
        UPDATE boards
        SET title = %s 
        WHERE id = %s;
        """
    cursor.execute(query, (title,))


