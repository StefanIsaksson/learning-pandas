import sqlite3
import pandas as pd


def main():
    conn = sqlite3.connect("pokemons.db")
    df = pd.read_sql_query("select name, type1, type2 from pokemons where generation=1;", conn)

    df = df.set_index('name')

    df.to_csv('generation_1_pokemons.csv')


if __name__ == '__main__':
    main();
