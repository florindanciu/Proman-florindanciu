from flask import Flask, render_template, url_for, request, redirect, session, flash
from util import json_response

import data_handler
import hashing

app = Flask(__name__)
app.secret_key = b'D3Z03lRQ_Neft7apw_oGzw'


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
    pass


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    pass


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
