# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import Utilisateur, Carte, Leader, Deck
from database import creer_tables, get_db_connection, get_decks, add_deck, afficher_table


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('show_decks'))

@app.route('/decks')
def show_decks():
    decks = get_decks()
    return render_template('decks.html', decks=decks)

@app.route('/add_deck', methods=['GET', 'POST'])
def add_deck_route():
    if request.method == 'POST':
        deck_name = request.form['deck_name']
        colors = request.form['colors']  # Assuming colors are provided as a comma-separated string
        leader_name = request.form['leader_name']
        add_deck(deck_name, colors, leader_name)
        return redirect(url_for('show_decks'))
    return render_template('add_deck.html')

if __name__ == '__main__':
    app.run(debug=True)
