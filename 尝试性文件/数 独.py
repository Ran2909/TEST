if __name__ == "__main__":
    main()
ac_num = 0
pause = True
difficulty = 3
from tkinter import *
from tkinter import ttk
import time
import pygame as py


def setDiff(difF):
    global difficulty
    global diff
    try:
        difficulty = int(difF)
        diff.destroy()
    except:
        pass


diff = Tk()
diff.title('难度选择')
diff.geometry('300x90')
diff.resizable(0, 0)
Label(diff, text='选择你要挑战的难度!(0~9)', font=('微软雅黑', 9)).pack()
cmb = ttk.Combobox(diff)
cmb.pack()
cmb['value'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
Button(diff, text='我选好了', command=lambda: setDiff(cmb.get())).pack()
diff.mainloop()
window = Tk()
window.title('数独')
window.geometry('390x500')
window.resizable(0, 0)
begin_time = 0
steps = 0
rights = 0
wrongs = 0
dwc = difficulty * 9
ac_name = None

list = range(1, 82)
try:
    ran = random.sample(list, dwc)
except:
    if difficulty > 9:
        ran = random.sample(list, 9)
    elif difficulty < 0:
        ran = random.sample(list, 1)
    print('难度输入出现问题 你将无法通关')
try:
    py.mixer.init()
    py.mixer.music.load("C:\\Users\\小李\\Desktop\\python文件\\bg.mp3")
    py.mixer.music.play(-1)
except py.error as e:
    print("无法加载音乐:", e)

music_playing = True  # 初始状态为播放


# 停止/继续音乐函数
def stopOrPlayMusic():
    global music_playing
    if music_playing:
        py.mixer.music.stop()
        music_playing = False
    else:
        py.mixer.music.play(-1)
        music_playing = True


# 添加停止音乐按钮
Button(window, text='♫', font=('楷体', 7), relief='sunken', bg='green', command=stopOrPlayMusic).place(x=365, y=11)


def setBlock(num, name):
    global begin_time
    if begin_time == 0:
        begin_time = time.time()
    global ac_name
    global ac_num
    if ac_name != name and name != None and ac_name != None:
        ac_name.config(text='?', bg='orange', activebackground='orange', relief='groove')
    if name.cget('bg') != 'green':
        name.config(text='···', relief='sunken', bg='lightblue', activebackground='lightblue')
        ac_name = name
        ac_num = num
    else:
        ac_name = None



