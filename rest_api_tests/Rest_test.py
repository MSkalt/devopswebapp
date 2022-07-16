import jsonpath as jsonpath
import requests
import jsonpath
import json

url = 'http://127.0.0.1:5000/'
add = '/add/'
put = '/put/'
delete = '/delete/'


def testGetRequest_01():

        requests.get(url)
        v_response = requests.get(url)
        v_content = v_response.text
        v_statuscode = v_response.status_code
        v_json_data = json.loads(v_content)
        v_Employees_elemnts = jsonpath.jsonpath(v_json_data, 'Employees')
        assert v_statuscode == 200

def testPostRequest_02():
        requests.get(url)
        v_response = requests.get(url)
        res = requests.post(url+add, json={'FirstName': 'gaga', 'LastName': 'Skalt', 'Gender': 'Male', 'Salary': 10000})
        v_response = requests.get(url)
        v_content = v_response.text
        v_statuscode = v_response.status_code
        assert v_statuscode == 200

def testPutRequest_03():
        requests.get(url)
        v_response = requests.get(url)
        res = requests.post(url+put, json={'FirstName': 'gaga', 'LastName': 'Skalt', 'Gender': 'Male', 'Salary': 10000})
        v_response = requests.get(url)
        v_content = v_response.text
        v_statuscode = v_response.status_code
        assert v_statuscode == 200

def testDeleteEequest_04():
        requests.get(url)
        v_response = requests.get(url)
        res = requests.post(url+delete+'1')
        v_response = requests.get(url)
        v_content = v_response.text
        v_statuscode = v_response.status_code
        assert v_statuscode == 200

#Error

def testPutRequest_05():
        requests.get(url)
        v_response = requests.get(url)
        res = requests.post(url+add, json={'FirstName1':  10000})
        v_response = requests.get(url)
        v_content = v_response.text
        v_statuscode = v_response.status_code
        assert v_statuscode == 200

def testPutRequest_03():
        requests.get(url)
        v_response = requests.get(url)
        res = requests.post(url+put+'aaaaaaaaaa')
        v_response = requests.get(url)
        v_content = v_response.text
        v_statuscode = v_response.status_code
        assert v_statuscode == 200