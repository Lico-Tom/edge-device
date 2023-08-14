from socket import *


def sendToSocket(data):
    # 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 准备接收方的地址
    dest_addr = ('192.168.31.56', 8080)  # 元组
    # 发送数据到服务端
    try:
        udp_socket.sendto(data.encode("utf-8"), dest_addr)
    except IOError:
        pass
    finally:
        udp_socket.close()
