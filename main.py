from flask import Flask, render_template, url_for, request, jsonify
from util import json_response

import data_handler
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')


@app.route("/add_board", methods=["GET", "POST"])
def add_board():
    if request.method == "POST":
        new_board = json.loads(request.data.decode("utf-8"))["title"]
        data_handler.add_board(new_board)
    return 'ok'


@app.route("/rename_board", methods=["GET", "POST"])
def rename_board():
    if request.method == "POST":
        board_id = json.loads(request.data.decode("utf-8"))["id"]
        new_board_name = json.loads(request.data.decode("utf-8"))["title"]
        data_handler.update_board_title(new_board_name, board_id)
    return 'ok'


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return data_handler.get_boards()


@app.route("/get-cards", methods=["POST"])
@json_response
def get_cards_for_board():
    board_id = json.loads(request.data.decode("utf-8"))["id"]
    return data_handler.get_cards_for_board(board_id)


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
