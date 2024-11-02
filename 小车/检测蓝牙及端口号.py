import bluetooth

#根据树莓派的蓝牙名称和地址
bluetooth_name = "raspberrypi"
bluetooth_address = None

#检测周围存在的蓝牙并存为列表
nearby_devices = bluetooth.discover_devices()

#检测是否能查找到目标蓝牙名称
for i in nearby_devices:
    if bluetooth_name == bluetooth.lookup_name(i):
        bluetooth_address = i
        break

#能找到则输出蓝牙名
if bluetooth_address is not None:
    print("Found", bluetooth_address)
else:
    print("Not Found")
