import pygame

def init():
	pygame.init()
	win=pygame.display.set_mode((100,100))

def getkey(keyname):
    ans = False
    for eve in pygame.event.get():
        pass
    keyinput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyname))
    if keyinput[myKey]:
        ans = True
    pygame.display.update()

    return ans

def main():
    if getkey('LEFT'):
        print('Left')
    if getkey('RIGHT'):
        print('Right')

if __name__=='__main__':
    init()
    while True:
        main()
