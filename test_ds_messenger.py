import socket
import json
import time
from ds_messenger import DirectMessage, DirectMessenger

server = "168.235.86.101"
port = 3021
timestamp = str(time.time())

def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
        server_conn.connect((server, port))
        stuff = {}
        stuff["join"] = {
                        "username": 'greenmmm',
                        "password": 'heheha',
                        "token": ""
                    }
        data_str = json.dumps(stuff)
        server_conn.sendall(data_str.encode())
        response = server_conn.recv(3021).decode()
        response_json = json.loads(response)
        print(response_json)   
        if "token" in str(response_json):
                    temp = str(response_json).index("token")
                    token = str(response_json)[temp+9:-3]
    
        formated = DirectMessage()
        formated.recipient = 'help'
        formated.message = 'fuck you bitch'
        formated.timestamp = timestamp

        mew = DirectMessenger("168.235.86.101", 'greenmmm', 'heheha')
        mew.token = token

        mew.send("fuck you bitch", 'help')









    '''
        
        formated = ({
                "token": token,
                "directmessage": {
                    "entry": 'greenfn',
                    "recipient": 'help',
                    'timestamp': timestamp
                }
                })

        data_str = json.dumps(formated)
        server_conn.sendall(data_str.encode())
        response = server_conn.recv(3021).decode()
        response_json = json.loads(response)
        print(response_json)
                
        read = ({
                "token": token,
                "directmessage": 'new'
                })

        data_str = json.dumps(read)
        server_conn.sendall(data_str.encode())
        response = server_conn.recv(3021).decode()
        response_json = json.loads(response)
        print(response_json)

        read = ({
                "token": token,
                "directmessage": 'all'
                })
                
        data_str = json.dumps(read)
        server_conn.sendall(data_str.encode())
        response = server_conn.recv(3021).decode()
        response_json = json.loads(response)
        print(response_json)
'''

if __name__ == '__main__':
        start()
