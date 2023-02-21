import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.status_code)
print(response.json())
print()
print(response.headers)
print("\n\nContent-Type:",response.headers.get('Content-Type'))

