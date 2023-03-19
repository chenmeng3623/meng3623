##服务器
import socket
import threading
import time

##控制客户端
def handle_client(client,clientaddr):
    pass

def ServerModule(serverchat):
    IpAddr = '192.168.137.1'
    Port   = 8888

    # 定义服务器套接字，设置通信类型
    # IPV4:AF_INET, IPV6:AF_INET6, SOCK_STREAM:TCP, SOCK_DGRAM:UDP
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcp_server:
        # 服务器套接字绑定地址和端口
        tcp_server.bind((IpAddr,Port))
        # 服务器开启监听状态，可同时监听多个客户端（考虑多线程问题）
        tcp_server.listen(2)

        # 接受客户端连接，返回客户端套接字和地址
        while True:
            client, clientaddr = tcp_server.accept()
            # 多线程
            t = threading.Thread(target=handle_client,args=(client,clientaddr))
            t.start()
            with client:
                print(clientaddr,"connected")

                while True:
                    # 接收客户端发来的信息，设置接收单条信息的长度（如最长1024字节）
                    client_msg = client.recv(1024)
                    time.sleep(5)
                    if not client_msg:
                        break

                    # 对接收到的信息进行解码
                    msg = client_msg.decode('utf-8')
                    print(msg)
                    # 给客户端反馈信息，表示已收到
                    client.send(serverchat.encode())

            # 关闭服务器
            tcp_server.close()


serverchat = "我很好"
ServerModule(serverchat)
