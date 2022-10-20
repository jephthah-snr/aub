import requests
# api_url = "https://forms.googleapis.com"
# route = "/v1/forms/{formId}"
# api_key = "AIzaSyDhBNw8cOgsRy5lbPLpEhDHZX3CJyzmdzM"
# response = requests.get(f"{api_url}{route}", api_key)
# print(response.json())



options = {
  'method': 'GET',
  'url': 'https://yusufnb-quotes-v1.p.rapidapi.com/widget/~einstein.json',
  'headers': {
    'X-RapidAPI-Key': 'ffe6850db2msh6d105bba0bf734dp1c6bdejsna1b9596314ff',
    'X-RapidAPI-Host': 'yusufnb-quotes-v1.p.rapidapi.com'
  }
}


response = requests.get(options)

print(response)