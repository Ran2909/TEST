import pygame
pygame.init()
window= pygame.display.set_mode((500,1000))
pygame.display.set_caption('display picture')

#============游戏启动页面静态效果=============
#-------显示图片------
# 1. 加载图片
image1 = pygame.image.load('Pictures/雨后少女.jpg')

# 2. 渲染图片 blit(渲染对象,坐标）
window.blit(image1,(-200,-400))
    # 操作图片
    # 1）计算图片大小
w,h = image1.get_size()
print(w,h)
    # 2) 旋转和缩放
'''scale(缩放对象，目标大小)'''
new1 = pygame.transform.scale(image1,(500,1000))
window.blit(new1,(0,0))
'''rotozoom(缩放/旋转对象，旋转角度，缩放比例)'''
new2 = pygame.transform.rotozoom(image1,180,0.5)
window.blit(new2,(100,200))
# 3. 刷新界面
'''
#pygame.display.flip() #仅第一次刷新
#pygame.display.update() #第一次以后的刷新'''
pygame.display.flip()



while True:
#================游戏帧刷新=================



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()