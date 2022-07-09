import requests

resp=requests.get("http://127.0.0.1:5000/")
print(resp)
code=resp.status_code
assert code ==200, "Code does not match"

# print(resp.text)
#
# print(resp.content)

print(resp.json())
print(resp.headers)
print(type(resp.headers))
print(resp.cookies)
print(resp.url)



