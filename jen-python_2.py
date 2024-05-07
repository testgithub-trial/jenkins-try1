import requests

files = {
    'type': (None, 'projectRoles'),
    'roleName': (None, 'test2'),
    'user': (None, 'sita'),
}

response = requests.post(
    'http://127.0.0.1:8080/role-strategy/strategy/assignUserRole',
    files=files,
    auth=('ram', '11b1a9e2bf0a50a2b3cffcf2420995817d'),
)
print(response.status_code)