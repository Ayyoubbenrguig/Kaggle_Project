#Import Primary Modules:
import sqlite3
import pandas as pd
import numpy as np  # useful for many scientific computing in Pytho
import matplotlib.pyplot as plt



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

  

# Exploration de data

data_describe = data.describe()
#data_info = data.info()

list_columns = data.columns.tolist()

Region = data["Region/Country/Area"]
Countries = data["country"]
Series = data["Series"]
Value = data["Value"]
Footnotes = data["Footnotes"]
Source = data["Source"]

new_data = data[["country", "Value"]]

# Netoyage de la data:

data.rename(columns={"Region/Country/Area": "Area_numero"}, inplace=True)
new_list_columns = data.columns.tolist()



data.dropna(subset=["Footnotes"], inplace=True)
sum_data_null = data.isnull().sum()


  


## Visualisation data:

def plot_filtered_bar_chart(data, list_countries, output_file="bar_plot_filtered_countries.png"):

    # Filtrer les données pour ne garder que les pays valides
    filtered_data = data[data["country"].isin(list_countries)]

    # Regrouper par pays et agréger les valeurs (somme des valeurs)
    grouped_data = filtered_data.groupby("country", as_index=False)["Value"].sum()

    # Trier les données par ordre décroissant
    grouped_data = grouped_data.sort_values(by="Value", ascending=False)

    # Dessiner le bar plot
    plt.figure(figsize=(12, 6))
    plt.bar(grouped_data["country"], grouped_data["Value"], color="skyblue")

    # Ajouter des labels et un titre
    plt.xlabel("Countries", fontsize=12)
    plt.ylabel("Total Value", fontsize=12)
    plt.title("Total Value by Country (Filtered)", fontsize=14)
    plt.xticks(rotation=45)  # Incliner les étiquettes des pays
    plt.grid(axis="y", linestyle="--", alpha=0.7)  # Grille horizontale

    # Enregistrer le graphique sous forme d'image
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)  # Enregistrement en haute qualité

    # Afficher le graphique
    plt.show()






    



print(data.head())
print(data.shape)
print(data_describe)
#print(data_info)
print(list_columns)
#print(Region)
#print(Countries)
#print(Series)
#print(Value)
#print(Footnotes)
#print(Source)
#print(new_data)



#print(sum_data_null)  # 659 ligne is null for Footnotes
#print(new_list_columns)
#print(list_countries)


# Visualisation de graphes:
#plot_filtered_bar_chart(data, list_countries, output_file="bar_plot_filtered_countries.png")
