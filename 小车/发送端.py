import bluetooth

# 树莓派蓝牙的地址
pi_address = 'E4:5F:01:3D:BB:29'
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1

# 连接树莓派蓝牙
if __name__ == '__main__':
    try:
        sock.connect((pi_address, port))
        while True:
            send_string = "Hello, Bluetooth!"  # 修改这里的字符串为你想要发送的内容
            sock.send(send_string.encode())
    except bluetooth.btcommon.BluetoothError as e:
        print("Bluetooth连接错误:", str(e))
    finally:
        sock.close()


