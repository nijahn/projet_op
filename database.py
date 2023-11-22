# database.py
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('decks.db')
    conn.row_factory = sqlite3.Row
    return conn



def creer_tables():
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cartes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                couleur TEXT,
                cout INTEGER,
                puissance INTEGER,
                attributs TEXT,
                extension TEXT,
                niveau_counter INTEGER
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS decks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                couleurs TEXT,
                leader TEXT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cartes_decks (
                id_carte INTEGER,
                id_deck INTEGER,
                FOREIGN KEY (id_carte) REFERENCES cartes (id),
                FOREIGN KEY (id_deck) REFERENCES decks (id)
            );
        """)
        
        
def afficher_table(conn, nom_table):
    print(f"Contenu de la table {nom_table}:")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {nom_table}")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("\n")
    
# database.py
import sqlite3

def get_decks():
    conn = get_db_connection()
    decks = conn.execute('SELECT * FROM decks').fetchall()
    conn.close()
    return decks

def add_deck(deck_name, colors, leader_name):
    conn = get_db_connection()
    conn.execute('INSERT INTO decks (nom, couleurs, leader) VALUES (?, ?, ?)', 
                 (deck_name, colors, leader_name))
    conn.commit()
    conn.close()
