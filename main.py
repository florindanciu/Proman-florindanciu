from flask import Flask, render_template, url_for
from util import json_response

import data_handler

app = Flask(__name__)


@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return data_handler.get_boards()


@app.route("/board/<int:id>/delete", methods=['POST'])
def delete_board(id):
    data_handler.delete_board(id)


@app.route("/board/<int:board_id>/collumn/<int:collumn_id>/delete", methods=['POST'])
def delete_collumn(board_id, collumn_id):
    data_handler.delete_collumn(board_id, collumn_id)


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route("/card/<int:id>/archive", methods=['POST'])
def archive_card(id):
    data_handler.archive_card(id)


@app.route("/card/<int:id>/dearchive", methods=['POST'])
def dearchive_card(id):
    data_handler.archive_card(id, False)


@app.route("/card/<int:id>/delete", methods=['POST'])
def delete_card(id):
    data_handler.delete_card(id)


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
