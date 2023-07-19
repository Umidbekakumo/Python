import requests, inquirer, json, boto3

url = "https://f4idu2pd8h.execute-api.us-east-1.amazonaws.com/v1/info"
headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Origin*": "*"
}
rsp = requests.get(url=url, headers=headers)
data = rsp.json()['body']

instructors = json.loads(data)[0]['staff']

instructors_questions = [
    inquirer.List('name', message="choose a instructor", choices=[x['name'] for x in instructors])
]

user_rsp = inquirer.prompt(instructors_questions)
for inst in instructors:
    if inst['name'] == user_rsp['name']:
        email = inst['email']
        name = ['name']
        print(f"""
********** Info for {inst['name']} **********
-----------------------
Name: {inst['name']}
Title: {inst['title']}
email: {inst['email']}
-----------------------
""")

url = "https://f4idu2pd8h.execute-api.us-east-1.amazonaws.com/v1/email"
headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Acess-Control-Allow-Orgins*": "*"
}

data = '{"name}: "Abdul Sharif", "email": "email", "subject": "Localhost at your service", "message": "This message from not lambda but localhost for hoemework"}'
rsp = requests.post(url=url, headers=headers, data=data)
print(rsp)

