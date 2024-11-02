# 读取串口数据并保存
import serial

# 设置串口号和波特率
ser = serial.Serial('COM6', 9600)
# a为储存数据的列表
a = []
# count为次数，采集多少次就停止
count = 0
while count != 100:
    data = ser.readline()  # 按行读取串口数据进来
    data = data.decode()  # 读进来的数据是bytes形式，需要转化为字符串格式
    data = data[0:len(data)-3]
    data = data.split(",")
    count += 1
    data = list(map(float, data))
    print(data)
    a.append(data)  # 添加到列表里



