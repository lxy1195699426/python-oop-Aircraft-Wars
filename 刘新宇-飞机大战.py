import pygame
from pygame.locals import *
import time
import random


class HeroPlane(object):
	"""我方飞机"""
	def __init__(self,screen_temp):
		self.x = 210
		self.y = 700
		self.image = pygame.image.load("./feiji/hero1.png")
		self.screen = screen_temp
		self.bullet_list = []
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
			if bullet.judge():
				self.bullet_list.remove(bullet)
	def move_left(self):
		self.x-=5
	def move_right(self):
		self.x+=5
	def move_down(self):
		self.y+=5
	def move_up(self):
		self.y-=5
	def fire(self):
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class Bullet(object):
	"""子弹类"""
	def __init__(self,screen_temp,x,y):
		self.x = x+40
		self.y = y-20
		self.image = pygame.image.load("./feiji/bullet.png")
		self.screen = screen_temp

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		self.y-=20

	def judge(self):
		if self.y<0:
			return True
		else:
			return False
class EnemyPlane(object):
	def __init__(self,screen_temp):
		self.x = 0
		self.y = 0
		self.image = pygame.image.load("./feiji/enemy0.png")
		self.screen = screen_temp
		self.direction = "right" 
		self.bullet_list = []
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
	def move(self):
		if self.direction=="right":
			self.x+=5
		elif self.direction=="left":
			self.x-=5

		if self.x>480-50:
			self.direction="left"
		elif self.x<0:
			self.direction="right"			
	def fire(self):
		rand_num = random.randint(1,100)
		if rand_num == 1 or rand_num == 78:
			self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
class EnemyBullet(object):
	def __init__(self,screen_temp,x,y):
		self.x = x+25
		self.y = y+40
		self.screen = screen_temp
		self.image = pygame.image.load("./feiji/bullet1.png")

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		self.y+=5
def key_control(hero_temp):
	#获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是d或者right
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                hero_temp.move_down()
            #检测按键是否是d或者right
            elif event.key == K_w or event.key == K_UP:
                print('up')
                hero_temp.move_up()

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
def main():
	#1.创建窗口
	screen = pygame.display.set_mode((480,852),0,32)

	#2.创建背景图片
	background = pygame.image.load("./feiji/background.png")

	#5.创建飞机图片
	#hero = pygame.image.load("./feiji/hero1.png")
	hero = HeroPlane(screen)

	#8.创建敌机对象
	enemy = EnemyPlane(screen)

	while True:
		#3.背景图片覆盖窗口
		screen.blit(background,(0,0))

		#6.飞机图片覆盖窗口
		hero.display()
		
		#9.显示敌机
		enemy.display()

		#10.敌机移动
		enemy.move()
		
		enemy.fire()
		#4.覆盖后显示
		pygame.display.update()

		key_control(hero)
		time.sleep(0.01)

if __name__ == '__main__':
	main()