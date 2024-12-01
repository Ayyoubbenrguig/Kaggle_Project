import sqlite3

conn = sqlite3.connect('data_base.db')

print("la base de données est bien crée")


conn.close()


