import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored
from tabulate import tabulate
pd.set_option("display.max_columns", None, "display.max_rows", None)

tabulka = pd.read_csv("path/tabulka_dat.csv").drop(columns=["Unnamed: 0"]) #path = path to your local disk

# vyhledávní podle jména autora
zadej = input("Zadej jméno autora: ")
tabulka_vyber = tabulka[["author", "title", "year_published"]]
tabulka.author = tabulka.author == f"{zadej}"

print(tabulate(tabulka_vyber[tabulka.author], headers=["author", "title", "year_published"], tablefmt="psql"))
print(colored("počet položek: ", "green"), len(tabulka_vyber[tabulka.author]))

# ověření, zda je text v databázi
vstup_dilo = input(colored("Zjistit, zda je text v databázi? (A/N): ", "blue"))

if vstup_dilo == "A": 
    vstup_konkretni_dilo = input(colored("Napiš název textu: ", "blue"))
    if vstup_konkretni_dilo in list(tabulka.title):
        print(colored("Text je v databázi", "green"))
    else:
         print(colored("Text není v databázi", "red"))
else:
    pass

# tisk celé tabulky
vstup2 = input(colored("Vytisknout celou tabulku? (A/N): ", "blue"))

if vstup2 == "A":
    print(tabulate(tabulka_vyber, headers=["author", "title"], tablefmt="psql"))
    print(colored("Počet položek: ", "green"), len(tabulka_vyber))
else:
    pass

# tisk tabulky podle let vzestupně

vstup6 = input(colored("Vytisknout tabulku seřazenou vzestupně dle let? (A/N): ", "blue"))

if vstup6 == "A":
    tabulka_dle_roku = tabulka[["title", "year_published"]].dropna()
    print(tabulate(tabulka_dle_roku.sort_values(by=["year_published"], ascending=True), tablefmt="psql"))
else:
    pass

# tisk roků a počtu titulů v každém roce
vstup7 = input(colored("Vytisknout tabulku roků a počtu děl v uvedených letech? (A/N): ", "blue"))
if vstup7 == "A":
    years = []
    tabulka_roky = tabulka_vyber.year_published.dropna()

    for rok in tabulka_roky:
        years.append(int(rok))

    sorted_years = sorted(years)

    texts = []
    for i in sorted_years:
        texts.append(sorted_years.count(i))

    slov = dict(zip(sorted_years, texts))

    print(tabulate(pd.Series(slov).to_frame(), tablefmt="psql"))

    pd.Series(slov).to_frame().to_excel("C:path/tabulka roku a del.xlsx") #path = path to your local disk
else:
    pass

# zadávání výběru podle rozmezí let
vstup3 = input(colored("Vytisknout data v rozmezí let (A/N): ", "blue"))

if vstup3 == "A":
    vstup4 = int(input(colored("Zadej počáteční rok: ", "red")))
    vstup5 = int(input(colored("Zadej konečný rok: ", "red")))

    tabulka_vyber_roky = tabulka[["author", "title", "year_published"]]
    tabulka_vyber_roky["year_published"].between(vstup4, vstup5, inclusive="both")
    result = tabulka_vyber_roky[tabulka_vyber_roky["year_published"].between(vstup4, vstup5, inclusive="both")].sort_values(by="year_published", ascending=True)
    print(tabulate(result, headers=["title", "year_published"], tablefmt="psql"))
    
    print(colored("Počet záznamů: ", "green"), len(result))
    
else:
    pass
