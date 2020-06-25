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
def add_status(cursor: RealDictCursor, board_id, title) -> list:
    query = """
        INSERT INTO statuses (board_id, title)
        VALUES (%s, %s)
        """
    cursor.execute(query, (board_id, title,))


@database_common.connection_handler
def add_card(cursor: RealDictCursor, board_id, status_id, title) -> list:
    query = """
        INSERT INTO cards (board_id, status_id, title, cards_order)
        VALUES (%s, %s, %s, 0)
        """
    cursor.execute(query, (board_id, status_id, title,))


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
        WHERE board_id = %s AND archived = 'false'
        """
    cursor.execute(query, (board_id,))
    return cursor.fetchall()


@database_common.connection_handler
def change_card_status(cursor: RealDictCursor, card_id, status_id) -> list:
    query = """
        UPDATE cards
        SET status_id = %s
        WHERE id = %s
        """
    cursor.execute(query, (status_id, card_id,))


@database_common.connection_handler
def get_statuses_for_board(cursor: RealDictCursor, board_id) -> list:
    query = """
        SELECT id, title, board_id
        FROM statuses
        WHERE board_id = %s
        ORDER BY id
        """
    cursor.execute(query, (board_id,))
    return cursor.fetchall()

@database_common.connection_handler
def change_status_title(cursor: RealDictCursor, status_id, title) -> list:
    query = """
        UPDATE statuses
        SET title = %s
        WHERE id = %s
        """
    cursor.execute(query, (title, status_id,))