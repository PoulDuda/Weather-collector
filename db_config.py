import sqlite3
from datetime import datetime

DB_FILE = 'weather.db'


def create_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS WeatherData (
        City TEXT, 
        Country TEXT, 
        Temperature REAL,
        Description TEXT,
        Feels REAL,
        Pressure REAL, 
        Humidity REAL,
        Wind_speed REAL,
        Time DATETIME)
        """
    )
    connection.commit()
    connection.close()


def data_to_list(json_data):
    data = list()
    data.append(json_data['name'])
    data.append(json_data['sys']["country"])
    data.append(json_data['main']['temp'])
    data.append(json_data['weather'][0]['description'])
    data.append(json_data['main']['feels_like'])
    data.append(json_data['main']['pressure'])
    data.append(json_data['main']['humidity'])
    data.append(json_data['wind']['speed'])
    return data


def insert_to_db(data):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data.append(current_time)
    cursor.execute(
        "INSERT INTO WeatherData (City, Country, Temperature, Description, Feels, Pressure, Humidity, Wind_speed, Time) VALUES (?,?,?,?,?,?,?,?,?)",
        data)
    connection.commit()
    connection.close()
