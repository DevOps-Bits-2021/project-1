import requests

url = "https://community-food2fork.p.rapidapi.com/get"

querystring = {"rId":"37859","key":"c07a7238aefeff5f21d72c939270f2e7"}

headers = {
    'x-rapidapi-host': "community-food2fork.p.rapidapi.com",
    'x-rapidapi-key': "2a692a86f5mshc772d7860f78f2fp120b00jsn13f3a19f55c5"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)