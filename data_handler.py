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
def delete_board(cursor: RealDictCursor, id) -> list:
    query = """
        DELETE FROM boards
        WHERE boards.id = %s
        """
    cursor.execute(query, (id, ))


@database_common.connection_handler
def delete_card(cursor: RealDictCursor, id) -> list:
    query = """
        DELETE FROM cards
        WHERE cards.id = %s
        """
    cursor.execute(query, (id, ))


@database_common.connection_handler
def delete_collumn(cursor: RealDictCursor, boardId, statusId) -> list:
    query = """
        DELETE FROM board_statuses 
        WHERE board_statuses.board_id = %s AND board_statuses.status_id = %s
        """
    cursor.execute(query, (boardId, statusId, ))