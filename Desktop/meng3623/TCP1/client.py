##客户端
import socket

def ClientModule(clientchat):
    IpAddr = '192.168.137.1'
    Port   = 8888

    # 定义客户端套接字
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcp_client:
        # 连接服务器
        tcp_client.connect((IpAddr,Port))

        while True:
            ##读取输入的内容
            if clientchat == "":
                break
            # 向服务器发送信息并编码
            tcp_client.send(clientchat.encode())

            ##等待接收服务器的信息
            server_msg = tcp_client.recv(1024).decode('utf-8')
            print(server_msg)
            if not server_msg:
                break

        # 关闭客户端
        tcp_client.close()


clientchat = "你好吗"
ClientModule(clientchat)
