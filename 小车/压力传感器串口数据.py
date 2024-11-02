import serial

ser = serial.Serial('COM6', 460800)
a = []
count = 0

while count<5:
    data = ser.read(38)  # 读取长度为38字节的数据
    try:
        # 解析数据
        frame_head = data[:4]  # 帧头
        data_length = data[4]  # 数据长度
        channel_data = [int.from_bytes(data[i:i+4], byteorder='little', signed=True) for i in range(5, 36, 4)]  # 通道数据
        sum_check = data[36]  # 和校验
        add_check = data[37]  # 附加校验

        # 计算校验
        sum_check_calc = sum(data[:36]) & 0xFF  # 计算和校验
        add_check_calc = sum_check_calc & 0xFF  # 计算附加校验

        # 打印数据
        print("Frame Head:", frame_head)
        print("Data Length:", data_length)
        print("Channel Data:", channel_data)
        print("Sum Check:", sum_check)
        print("Add Check:", add_check)

        # 验证校验
        if sum_check == sum_check_calc and add_check == add_check_calc:
            print("Checksum validation: Passed")
        else:
            print("Checksum validation: Failed")

        # 将数据存入列表
        a.append(channel_data)
        count += 1

    except ValueError as e:
        print(f"ValueError: {e}")

print(a)