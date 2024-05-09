import sqlite3

def create_schema():
    conn = sqlite3.connect('caronas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE caronas
                 (id TEXT PRIMARY KEY,
                 nome TEXT,
                 cidade_partida TEXT,
                 cidade_chegada TEXT,
                 banda TEXT,
                 data TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_schema()
