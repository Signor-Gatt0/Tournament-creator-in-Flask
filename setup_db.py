import sqlite3
import os

if not os.path.exists('app/instance'):
    os.makedirs('app/instance')

db_path = os.path.join('app/instance', 'tournament.db')
connection = sqlite3.connect(db_path)

with open('app/tournament.sql') as f:
    connection.executescript(f.read())

connection.close()