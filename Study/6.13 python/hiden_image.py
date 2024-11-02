#!C:\Users\29098\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10
import random
import string
from PIL import Image
from tkinter import Tk, filedialog

def choose_image_A():
    root = Tk()
    root.withdraw()
    imgA_path = filedialog.askopenfilename(title="请选择表面图")
    choose_image_B(imgA_path)

def choose_image_B(imgA_path):
    root = Tk()
    root.withdraw()
    imgB_path = filedialog.askopenfilename(title="请选择内部图")
    save_path = "C:/Users/29098/Desktop/" + generate_random_filename() + ".png"
    modify_images(imgA_path, imgB_path, save_path)

def modify_images(imgA_path, imgB_path, save_path):
    # 加载两张素材图片并转化为灰度图
    imgA = Image.open(imgA_path).convert('L')
    imgB = Image.open(imgB_path).convert('L')

    # 调整亮度代码，第一行是把A图片调亮，第二行是把B图片调暗
    imgA = imgA.point(lambda gray: int((gray + 255) / 2))
    imgB = imgB.point(lambda gray: int(gray / 2))

    # 新建空白图片
    img = Image.new('RGBA', imgA.size)

    # 遍历每一个像素点，计算出透明度和灰度后填充到空白图片
    for x in range(img.width):
        for y in range(img.height):
            alpha = 255 - imgA.getpixel((x, y)) + imgB.getpixel((x, y))
            color = int(imgB.getpixel((x, y)) * 255 / alpha) if alpha else 127
            img.putpixel((x, y), (color, color, color, alpha))

    # 保存图片到指定路径
    img.save(save_path)

def generate_random_filename():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(10))

# 显示图像选择窗口
choose_image_A()
