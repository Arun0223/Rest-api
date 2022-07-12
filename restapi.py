### REST ==> Representational state transfer
import requests as r
api_url='https://jsonplaceholder.typicode.com/todos/1'
response=r.get(api_url)
# print(response.json())
response1=r.get(api_url)
# print(response.json())
response2=r.get(api_url)
print(response2.json())

