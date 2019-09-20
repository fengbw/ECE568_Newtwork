from socket import *
import os, sys

if __name__ == "__main__":
    hostIp='127.0.0.1'
    port = 2048
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind((hostIp,port))
    sock.listen(5)
    print('---开始监听{0}:{1}'.format(hostIp,port), '---')
    while True:
        #接受一个客户端的连接
        conn, addr = sock.accept()
        print("Recived a client from {0}".format(addr))
        #与客户端进行交互，直到客户端退出
        while True:
            #接收客户端发来的信息，一次最多收1024字节
            recivedData = conn.recv(1024)
            recivedData = recivedData.decode()
            if recivedData[:3] == "GET":
                filename = recivedData.split(" ")[1]
                try:
                    f = open(filename, "r")
                except IOError:
                    output_data = "ERROR: no such file"
                    conn.send(output_data.encode())
                else:
                    output_data = f.read()
                    conn.send(output_data.encode())
                    f.close()
            elif recivedData[:6] == "BOUNCE":
                output_data = recivedData[7:]
                conn.send(output_data.encode())
            elif recivedData[:4] == "EXIT":
                if len(recivedData) == 4:
                    output_data = "Normal_Exit"
                else:
                    output_data = recivedData[5:]
                conn.send(output_data.encode())
                conn.close()
                sock.close()
                break
            else:
                output_data = "No command. Please input GET|BOUNCE|EXIT command."
                conn.send(output_data.encode())
        break
