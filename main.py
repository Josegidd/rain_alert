import requests
from twilio.rest import Client
account_sid = "ACdd754fdbc31f1da2067c196aa8debd95"
auth_token = "a2f44f34d6afa757ecbff5688a649eb8"
Rain_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "63899f8417d0a93d10f58fedc065a6d2"
parameters = {
    "lat": 5.423840,
    "lon": 7.574050,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(Rain_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
weather_id = []

will_rain = False

for hour in weather_slice:
    weather_id.append(hour["weather"][0]["id"])


for data in weather_id:
    if data <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hi Gideon, its going to rain today!!!",
        from_='+14704729337',
        to='+23408034224011'
    )

    print(message.status)
# print(weather_data["hourly"][0]["weather"][0]["id"])


