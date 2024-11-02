import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#设置端口号
port = 1

#绑定电脑蓝牙地址和端口
server_sock.bind(("2C-33-58-E4-B0-AF", port))
server_sock.listen(1)
if __name__ =='__main__':
    try:
        while True:
            print('正在等待接收数据。。。')
            client_sock,address=server_sock.accept()
            print('连接成功')
            print("Accepted connection from ", address)
            while True:
                data =client_sock.recv(1024).decode() #不断接收数据
                print("received [%s]" % data)
    except:
        client_sock.close()
        server_sock.close()
        print('disconnect!')