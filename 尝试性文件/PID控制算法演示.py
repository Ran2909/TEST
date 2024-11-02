import numpy as np
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.integral = 0

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.last_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.last_error = error
        return output

class Drone:
    def __init__(self, initial_height):
        self.height = initial_height
        self.controller = PIDController(1, 0.1, 0.5)

    def update(self, target_height, dt):
        error = target_height - self.height
        output = self.controller.update(error, dt)
        self.height += output * dt

# 示例用法
drone = Drone(0)
target_height = 10
dt = 0.1
for i in range(100):
    drone.update(target_height, dt)
    print(drone.height)
import pygame

pygame.init()

# 设置窗口界面
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drone Control")

# 初始化无人机参数
drone = Drone(0)
target_height = 0

#初始化PID控制器参数
kp = 1
ki = 0.3
kd = 0.6
controller = PIDController(kp, ki, kd)

# 时间
clock = pygame.time.Clock()

# 游戏主体
while True:
    # 游戏处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_height = pygame.mouse.get_pos()[1]

    # 随时间更新无人机参数
    dt = clock.tick(60) / 1000.0
    error = target_height - drone.height
    output = controller.update(error, dt)
    drone.height += output * dt

    # 无人机和目标高度的展现形式
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (0, target_height, WINDOW_WIDTH, 2))
    pygame.draw.rect(screen, (255, 0, 0), (0, drone.height, WINDOW_WIDTH, 2))
    pygame.display.update()