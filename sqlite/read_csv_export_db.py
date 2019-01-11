import sqlite3
import pandas as pd


def main():
    df = pd.read_csv('pokemon.csv')

    df = df[['pokedex_number', 'name', 'generation', 'type1', 'type2', 'is_legendary',
             'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
    df = df.set_index('name')

    with sqlite3.connect('pokemons.db') as conn:
        df.to_sql('pokemons', conn)


if __name__ == '__main__':
    main();
