import requests, os, inquirer, digitalocean, json


TOKEN = os.getenv('DROPLET_TOKEN')

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
url = "https://api.digitalocean.com/v2/droplets"

with open('install.sh','r') as file:
    file_contents = file.read()

options = [
    inquirer.List('image',
                message ='select an image:',
                choices=['centos-stream-8-x64','ubuntu-20-04-x64', 'debian-10-x64'],
                ),
    inquirer.List('size',
                message = 'select a size:',
                choices =['s-1vcpu-1gb', 's-1vcpu-512mb', 's-1vcpu-2gb'],
                ),
    inquirer.List('region',
                message = 'select a region',
                choices =['nyc1', 'nyc2', 'nyc3',],
                ),
    inquirer.List('sshkeys',
                message = 'select a ssh key',
                choices =['38389732', '38577516', '38586832'],
                ),
]
answers = inquirer.prompt(options)



data = {
    "name": "NewDroplet",
    "region": answers['region'],
    "image": answers['image'],
    "size": answers['size'],
    "ssh_keys": [answers['sshkeys']],
    "user_data": file_contents
}

data_json = json.dumps(data)

do_resp = requests.post(url, headers=headers, data=data_json)
print(do_resp.text)




if do_resp.status_code == 202:
    slack_url = 'SLACK_API'
    slack_payload = {
        "text": "Droplet server created successfully by umid"
    }
    slack_resp = requests.post(slack_url, json=slack_payload)

