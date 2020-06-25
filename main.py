from flask import Flask, render_template, url_for, request, redirect, session, flash
from util import json_response

import data_handler
import hashing
import json

app = Flask(__name__)
app.secret_key = b'D3Z03lRQ_Neft7apw_oGzw'


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
    return True


@app.route("/board/<int:board_id>/collumn/<int:collumn_id>/delete", methods=['POST'])
def delete_collumn(board_id, collumn_id):
    data_handler.delete_collumn(board_id, collumn_id)
    return True


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
    return True


@app.route("/card/<int:id>/dearchive", methods=['POST'])
def dearchive_card(id):
    data_handler.archive_card(id, False)
    return True


@app.route("/card/<int:id>/delete", methods=['POST'])
def delete_card(id):
    data_handler.delete_card(id)
    return True


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email_register')
        password = request.form.get('passwd')
        confirm = request.form.get('confirm')
        secure_password = hashing.hash_password(password)
        user_info = data_handler.get_user_info_by_email(email)

        if user_info is not None:
            flash('Email already used!', 'info')
        elif password == confirm:
            data_handler.add_user_info(first_name, last_name, email, secure_password)
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Registration does not mach!', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email_login')
        password = request.form.get('password')
        user_info = data_handler.get_user_info_by_email(email)

        if not user_info:
            flash('Email not found!', 'danger')
            return redirect(url_for('login'))
        elif hashing.verify_password(password, user_info['password']):
            session['email'] = email
            flash('You are now logged in', 'success')
            return render_template('index.html', user_info=user_info)
        else:
            flash('Incorrect password!', 'danger')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route("/logout")
def logout():
    session.clear()
    flash('You are now logged out', 'info')
    return redirect(url_for('index'))


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
