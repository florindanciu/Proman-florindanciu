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


@app.route("/add_board", methods=["POST"])
@json_response
def add_board():
    if request.method == "POST":
        new_board = json.loads(request.data.decode("utf-8"))["title"]
        data_handler.add_board(new_board)
    return True


@app.route("/rename_board", methods=["POST"])
def rename_board():
    if request.method == "POST":
        board_id = json.loads(request.data.decode("utf-8"))["id"]
        new_board_name = json.loads(request.data.decode("utf-8"))["title"]
        data_handler.update_board_title(new_board_name, board_id)
    return True


@app.route('/add-status', methods=['POST'])
def add_status():
    board_id = json.loads(request.data.decode("utf-8"))["boardId"]
    data_handler.add_status(board_id, 'New Status')
    return True


@app.route("/rename-status", methods=["POST"])
def rename_status():
    status_id = json.loads(request.data.decode("utf-8"))["statusId"]
    title = json.loads(request.data.decode("utf-8"))["title"]
    data_handler.change_status_title(status_id, title)
    return True


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


@app.route("/get-cards/<id>")
@json_response
def get_cards_for_board(id):
    data = {
        'cards': data_handler.get_cards_for_board(id),
        'statuses': data_handler.get_statuses_for_board(id)
    }
    return data


@app.route('/add-card', methods=['POST'])
def add_card():
    board_id = json.loads(request.data.decode("utf-8"))["boardId"]
    status_id = json.loads(request.data.decode("utf-8"))["statusId"]
    data_handler.add_card(board_id, status_id, 'New Card')
    return True


@app.route("/move-card", methods=['POST'])
def move_card():
    card_id = json.loads(request.data.decode("utf-8"))["cardId"]
    status_id = json.loads(request.data.decode("utf-8"))["statusId"]
    data_handler.change_card_status(card_id, status_id)
    return True


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
