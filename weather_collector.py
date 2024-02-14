from key_saver import key
import requests
import time
from db_config import create_database, data_to_list, insert_to_db

cities = [
    'London,uk', 'New York,us', 'Paris,fr', 'Moscow,ru', 'Tokyo,jp',
    'Beijing,cn', 'Cairo,eg', 'Rio de Janeiro,br', 'Sydney,au', 'Berlin,de',
    'Mexico City,mx', 'Delhi,in', 'Istanbul,tr', 'Bangkok,th', 'Jakarta,id',
    'Toronto,ca', 'Seoul,kr', 'Shanghai,cn', 'Karachi,pk', 'Lagos,ng',
    'Mumbai,in', 'Los Angeles,us', 'Chicago,us', 'Chennai,in', 'Kolkata,in',
    'Riyadh,sa', 'Buenos Aires,ar', 'Madrid,es', 'Saint Petersburg,ru', 'Manila,ph',
    'Kiev,ua', 'Barcelona,es', 'Bangalore,in', 'Ho Chi Minh City,vn', 'Miami,us',
    'Lima,pe', 'Paris,fr', 'Nairobi,ke', 'Houston,us', 'Dallas,us', 'Berlin,de',
    'Santiago,cl', 'Atlanta,us', 'Hong Kong,hk', 'Sydney,au', 'Boston,us',
    'Seattle,us', 'Dubai,ae', 'Philadelphia,us', 'San Francisco,us'
]

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Failed to get weather in {city}. Status code: {response.status_code}')
        return None


# Функция для проверки работоспособности запросов
def collect_weather_data():
    for city in cities:
        data = get_weather_data(city)
        if data:
            print(f"Weather data for {city}:")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Temperature feels like: {data['main']['feels_like']} °C")
            print(f"Atmospheric pressure: {data['main']['pressure']} millibar")
            print(f"Humidity: {data['main']['humidity']} %")
            print(f"Wind speed: {data['wind']['speed']} m/s")
            print("----------------------------")
        time.sleep(1)


def collect_data():
    create_database()
    for city in cities:
        data_json = get_weather_data(city)
        data = data_to_list(data_json)
        if data is not None:
            insert_to_db(data)


if __name__ == "__main__":
    collect_data()
