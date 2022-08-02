from flask import render_template, request, redirect, url_for, session, flash
from flask_app.models.game import Game
from flask_app import app

app.secret_key = 'super secret key'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

""" @app.route('/game', methods=['POST'])
def game():
    if request.method == 'POST':
        if request.form['submit'] == 'Start Game':
            session['game'] = Game(request.form['num_players'], request.form['num_cards'])
            return redirect(url_for('game_page'))
        elif request.form['submit'] == 'Reset':
            session.clear()
            return redirect(url_for('index'))
    return redirect(url_for('index')) """


@app.route('/game')
def game():
    session['game'] = session.get('game', False)
    players = []
    if not session ['game']:
        game = Game(['Ninja','Pirate'],10)
        session['game'] = True
        players = game.players
    return render_template('game.html', players=players)