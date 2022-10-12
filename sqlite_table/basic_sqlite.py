import sqlite3

# create db + create cursor
connexion = sqlite3.connect("album.db")
cursor = connexion.cursor()

# create table
cursor.execute('CREATE TABLE artiste (artist_id INTEGER NOT NULL PRIMARY KEY, name VARCHAR);')

cursor.execute(
    'CREATE TABLE album (album_id INTEGER NOT NULL PRIMARY KEY, artist_id INTEGER REFERENCES artiste, title VARCHAR, '
    'year INTEGER);')

# add data to table artiste
cursor.execute('INSERT INTO artiste (name) VALUES ("VEXENTO");')
# recover id artist
vexento_id = cursor.lastrowid

cursor.execute('INSERT INTO artiste (name) VALUES ("Exyl");')
exil_id = cursor.lastrowid

# add value to table album
cursor.execute(
    'INSERT INTO album (artist_id, title,year) VALUES (' + str(vexento_id) + ', "Never Letting Go", "2017");')
cursor.execute('INSERT INTO album (artist_id, title,year) VALUES (' + str(vexento_id) + ', "Inspire", "2018");')

cursor.execute('INSERT INTO album (artist_id, title,year) VALUES (' + str(exil_id) + ', "Ping!", "2018");')
cursor.execute('INSERT INTO album (artist_id, title,year) VALUES (' + str(exil_id) + ', "Ping! 2", "2022");')
cursor.execute('INSERT INTO album (artist_id, title,year) VALUES (' + str(exil_id) + ', "Terraria", "2020");')

# commit change in db + close
connexion.commit()
connexion.close()
