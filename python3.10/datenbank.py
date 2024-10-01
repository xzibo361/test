import os
import sqlalchemy as db



con_str = "mysql+pymysql://root:test123@localhost/movie"
engine = db.create_engine(con_str)
 
# ein DB-Verbindungsobjekt erzeugen
connection = engine.connect()
 
# ein Metadaten-Objekt erzeugen
meta_data = db.MetaData()

# Entwurfsskript für "actor"-Tabelle
actor = db.Table(
  "actorZwei", meta_data,
  db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
  db.Column("first_name", db.String(50), nullable=False),
  db.Column("last_name", db.String(50), nullable=False),
  db.Column("age", db.Integer, nullable=False),
  db.Column("date_of_birth", db.Date, nullable=False),
  db.Column("active", db.Boolean, nullable=False))
 
# "actor"-Tabelle erstellen und Informationen im 
# Metadaten-Objekt speicher
meta_data.create_all(engine)
# Insert-Anweisung erzeugen
sql_query = db.insert(actorZwei)
 
# eine Liste aus Dictionary-Einträgen erstellen
data_list = [{"first_name":"John", "last_name":"Smith", 
  "age":50, "date_of_birth":"1969-04-05", "active":True},{"first_name":"Brian", "last_name":"Morgan", 
  "age":38, "date_of_birth":"1981-02-11", "active":True}, 
    {"first_name":"David", "last_name":"White", 
  "age":77, "date_of_birth":"1942-06-30", "active":False}]
 
# Insert-Anweisung ausführen
result = connection.execute(sql_query, data_list)
