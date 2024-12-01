import sqlite3
import pandas as pd


# connection à la base de données:
conn = sqlite3.connect('data_base.db')
cursor = conn.cursor()

# importer la data
data = pd.read_csv('Data/statistics.csv')


list_countries = []
with open("Data/countries.txt") as file:
    for line in file:
        # Diviser chaque ligne par les tabulations ou espaces multiples
        countries_in_line = line.strip().split()
        list_countries.extend(countries_in_line)  # Ajouter les pays à la liste


cursor.execute('''
CREATE TABLE IF NOT EXISTS indicators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Region_Country_Area TEXT,
    country TEXT,
    Year INTEGER,
    Series TEXT,
    Value REAL,
    Footnotes TEXT,
    Source TEXT
)
''')


# Insérer les données dans la table `indicators`
data.to_sql('indicators', conn, if_exists='replace', index=False)


# Créer la table `countries` si elle n'existe pas déjà
cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT UNIQUE
)
''')

# Insérer les pays dans la table `countries`
for country in list_countries:
    try:
        cursor.execute("INSERT OR IGNORE INTO countries (country) VALUES (?)", (country,))
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion du pays {country}: {e}")


# Valider les changements

conn.commit()


# supprimer les entrées avec les valeurs manquantes

cursor.execute("DELETE FROM Indicators WHERE Value IS NULL")

conn.commit()

# Visualisation

query ='''
SELECT country, AVG(Value) as avg_Value FROM indicators
WHERE country IN (SELECT country FROM countries)
GROUP BY country
ORDER BY AVG(Value) DESC LIMIT 5
'''

results = cursor.execute(query).fetchall()


print("Résultat :", results)


conn.close()
