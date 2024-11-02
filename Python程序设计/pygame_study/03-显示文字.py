import pygame
pygame.init()
window= pygame.display.set_mode((500,500))
pygame.display.set_caption('display strings')

#==============显示文字============
# 1. 创建字体对象
'''Font(字体文件路径，字号）'''
font = pygame.font.Font('E:/BDWP/Slidechunfeng-Regular.ttf',30)

# 2. 创建文字对象
'''render(文字内容，True，文字颜色,文字背景颜色)'''
text = font.render('开始游戏',True,(100,0,0))

# 3. 渲染到窗口上
window.blit(text,(200,200))


# 4. 操作文字对象
    # 1) 获取大小
w,h=text.get_size()
window.blit(text,(500-w,500-h))
    # 2) 缩放和旋转
newt1=pygame.transform.scale(text,(200,50))
window.blit(newt1,(0,60))

newt2 = pygame.transform.rotozoom(text,180,0.5)
window.blit(newt2,(200,100))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()