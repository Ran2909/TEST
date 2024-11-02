#完成一个游戏最少要哪些代码

import pygame

# 1. 初始化操作
pygame.init()

# 2. 创建游戏窗口
'''
    set_mode(窗口大小)
    window : 把窗口变成一个对象，方便后续操作
'''
window = pygame.display.set_mode((400,600))

    #设置游戏标题
pygame.display.set_caption('Love Story')
    #设置背景颜色
window.fill((255,100,255))
# 3. 让游戏保持一直运行的状态
'''
    game loop(游戏循环)
'''
while True:

# 4. 检测事件(有没有事件触发)
    for event in pygame.event.get():
    #不同事件不同反应
        #退出
        if event.type == pygame.QUIT:
            exit()#结束的是该线程



