from socket import *
import os,sys

if __name__ == "__main__":
    hostIp = '127.0.0.1'
    port = 2048
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect((hostIp,port))
    print("---Have connected server---")
    while True:
        print("---Please input command---")
        send_data = input()
        sock.send(send_data.encode())
        #print(sock.recv(1024).decode())
        print("---Recived from server---")
        recivedData = sock.recv(1024).decode()
        print(recivedData)
        if send_data[:4] == "EXIT":
            break
    sock.close()
