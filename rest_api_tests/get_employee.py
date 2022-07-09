import jsonpath as jsonpath
import requests
import jsonpath
import json

url = 'http://127.0.0.1:5000/'


requests.get("http://127.0.0.1:5000/")
v_response = requests.get(url)

v_content = v_response.text
print(v_content)
v_statuscode = v_response.status_code
print(v_statuscode)

v_json_data = json.loads(v_content)
print(v_json_data)

# v_per_page = jsonpath.jsonpath(v_json_data, 'per_page')
# print(v_per_page)

v_Employees_elemnts = jsonpath.jsonpath(v_json_data, 'Employees')
print(v_Employees_elemnts)
print(len(v_Employees_elemnts[0]))

assert v_statuscode == 200
