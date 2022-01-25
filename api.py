import requests
import json

url = "http://httpbin.org/post"

payload = json.dumps({
  "Sensor 1": "Distancia",
  "Sensor 2": "LDR",
  "Sensor 3": "sensor humedad de suelo"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)