from functions   import is_even
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

print(f'status code is (repsonse.status_code)')


print(response.text)

