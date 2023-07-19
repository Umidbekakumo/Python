#create digital ocean droplet 

import os, digitalocean

TOKEN = os.getenv('DROPLET_TOKEN')

manager = digitalocean.Manager(token=TOKEN)

# my_droplets = manager.get_all_droplets()
# for droplet in my_droplets:
#    print(droplet.load())

def all_droplets(manager):
    droplets = []
    all_droplets = manager.get_all_droplets()
    for droplet in all_droplets:
        # droplets.append(
        # print(str(droplet).split(' '))
        droplets.append({"id": (str(droplet).split(' '))[1]})
        droplets.append({"name": (str(droplet).split(' '))[2][:-1]})
    
    
    return droplets

print(all_droplets(manager=manager))


def create_droplet(token, name, region, image, size, ssh_key, user_data):
    for key in get_sshkeys(manager=manager):
        ssh_keyname = key['name']
        ssh_keyid = key['id']
        print(key['name'])
    user_ssh = input("please enter which key you would like to use: ")
    
    droplet = digitalocean.Droplet(
        token=TOKEN,
        name=name,
        region=region, 
        image=image, 
        size_slug=size
        ssh_keys=[ssh_keyid]
        user_data=user_data
    )
    resp = droplet.create()
    return resp
    

# print(digitalocean.Droplet.get_data)



def get_sshkeys(manager, name):
    keys = manager.get_all_sshkeys
    key = []
    for key in keys:
        ssh_keys.append({"id": (str(key).split(' '))[1]})
        ssh_keys.append({"name": (str(key).split(' '))[2][:-1]})
        


create_droplet(
    token=TOKEN,
    name="NewDroplet",
    region="nyc1",
    imagine="centos-stream-8-64x",
    size="s-1vcpu-1gb",
    ssh_key="MacKey",
    user_data="""
#!/bin/bash
sudo yum install epel-release -y
sudo yum install httpd -y 
echo "this is my web-server" > 
"""
)
