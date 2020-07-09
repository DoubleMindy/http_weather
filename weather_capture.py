import requests

def get_weather(location, language = 'en', options = ''):
	response = requests.get(url.format(location, options, language))
	return response.text


url = 'http://wttr.in/{0}?n{1}Tqu&lang={2}'
print(get_weather('London'))
print(get_weather('Шереметьево', 'ru'))
print(get_weather('череповец', 'ru', 'm'))