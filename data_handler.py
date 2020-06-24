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
def get_board_id(cursor: RealDictCursor, title) -> list:
    query = """
            SELECT id
            FROM boards
            WHERE title = %s"""
    cursor.execute(query, (title,))
    return cursor.fetchone()

@database_common.connection_handler
def add_board(cursor: RealDictCursor, title) -> list:
    query = """
            INSERT INTO boards (title)
            VALUES (%s);"""
    cursor.execute(query, (title,))

@database_common.connection_handler
def update_board_title(cursor: RealDictCursor, title, id) -> list:
    query = """
        UPDATE boards
        SET title = %s 
        WHERE id = %s;
        """
    cursor.execute(query, (title, id,))

@database_common.connection_handler
def get_cards_for_board(cursor: RealDictCursor, board_id) -> list:
    query = """
            SELECT *
            FROM cards
            WHERE board_id = %s"""
    cursor.execute(query, (board_id,))
    return cursor.fetchall()




