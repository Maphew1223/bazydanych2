import sqlite3
import pandas as pd

stations_data = pd.read_csv("clean_stations.csv")
measure_data = pd.read_csv("clean_measure.csv")

print(stations_data)
print(measure_data)

conn = sqlite3.connect("database.db")

stations_data.to_sql("stations", conn, if_exists="replace", index=False)
measure_data.to_sql("measurements", conn, if_exists="replace", index=False)

result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)

conn.close()