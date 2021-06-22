import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95' #generated api key was not working --> b54f10f7fd2a9debf5bffe628d20c909'
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

try:
	api_link = requests.get(complete_api_link)
	api_data = api_link.json()

	temp_city = ((api_data['main']['temp']) - 273.15)
	weather_desc = api_data['weather'][0]['description']
	hmdt = api_data['main']['humidity']
	wind_spd = api_data['wind']['speed']
	date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
except Exception:
	print("Wrong City or Problem in API KEY...")
else :
	s1 = "\n-------------------------------------------------------------"
	s2 = f"Weather Stats for - {location.upper()} || {date_time}"
	s3 = "-------------------------------------------------------------\n"
	s4 = "Current temperature   : {:.2f} deg C".format(temp_city)
	s5 = f"Current weather desc  : {weather_desc}"
	s6 = f"Current Humidity      : {hmdt} %"
	s7 = f"Current wind speed    : {wind_spd} kmph"
	log_str = ""
	for x in (s1,s2,s3,s4,s5,s6,s7):
		log_str += x+ "\n"
	print(log_str)

	log_file = open('Weather_logs.txt','a')
	log_file.write(log_str)
	log_file.close()
