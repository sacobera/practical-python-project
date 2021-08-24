import requests

def get_weather_desc_and_temp():
    api_key = "52843ca063d9dd9a9c734193816d654b"
    # api_key= "67da29cb91129f1a68c1c06c1be92daa"
    city = "Orlando"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get("weather")[0].get("description")

    #Getting the minimum and maximum temperature 
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description' : description,
            'temp_min' :temp_min,
            'temp_max' : temp_max}

def main():
#PRINT THE RESULTS 
weather_dict = get_weather_desc_and_temp()
print("Today's forecast is", weather_dict.get('description'))
print("The minimum temperature is", weather_dict.get('temp_min'))
print("The maximum temperature is", weather_dict.get('temp_max'))

main()