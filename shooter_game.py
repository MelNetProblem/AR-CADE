#Создай собственный Шутер!
fps = 144
from pygame import mixer
from pygame import *
from pygame import font
from random import randint
speed = 7
pos = 1
trava = 110
skin = 0
stem = 13
lose = 0
displaying = 20
musika = 1
score = 0
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >5:
            self.rect.x -= speed
        if keys_pressed[K_d] and self.rect.x<650:
            self.rect.x += speed 
    def fire(self):
        bullet = Bullet("bulls.png",self.rect.centerx,self.rect.top,10,30,10)
        mixer_music.play()
        mixer.init()
        mixer_music.load("fire.mp3")
        mixer_music.play()
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global lose
        self.rect.y+=self.speed
        if self.rect.y>500:
            self.rect.y = 0
            self.rect.x = randint(100,600)
            lose+=1
class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<0:
            self.kill()




loser = GameSprite("lose.png",10,450,50,50,0)
'''
scorer = GameSprite("score.png",0,700,500,50,0)
'''
hero = Player("hero.png",300,450,50,50,11)
enemy = Enemy("enemy1.png",300,20,50,50,10)
window = display.set_mode((700,500))
display.set_caption("AR-CADE")
startbutton = GameSprite("123.png",350,250,80,50,0)
background = transform.scale(image.load("bigground.png"),(700,500))
lose_png = GameSprite("youloser.png",0,0,700,500,0)
startmenu = transform.scale(image.load("startmenu.png"),(700,500))


bullet = Bullet("bulls.png",100,100,50,50,10)


bullets = sprite.Group()
bullets.add(bullet)
bullet.kill()

monsters = sprite.Group()
for i in range(6):
    monsters.add(Enemy("enemy"+str(i+1)+".png",randint(50,650),0,50,50,randint(1,2)))

font.init()
font1 = font.Font(None,70)
game = True
mixer.init()
finish= False
mixer_music.load("soundtrack.mp3")
mixer_music.play()
'''
while trava == 10:
    '''
 
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

    sprites_list=sprite.groupcollide(monsters,bullets,True,True)
    for s in sprites_list:
        score+=1
        monsters.add(Enemy("enemy"+str(randint(1,6))+".png",randint(80,620),5,50,50,1))
    if lose>=15 or sprite.spritecollide(hero,monsters,True):
        finish = True
    if finish == True:
        lose_png.reset()
        '''
        if stem == 13:
            pos = 2
        if pos == 1:
            startbutton.reset()
            startbutton.update() 
            window.blit(background, (0, 0))
        if pos == 2:
        '''
    if not(finish):
        text_lose = font1.render(str(lose),1,(255,193,7))
        window.blit(background, (0, 0))
        window.blit(text_lose,(60,455))
        hero.reset()
        hero.update()
        monsters.update()
        monsters.draw(window)
        loser.update()
        loser.reset()
        bullets.update()
        bullets.draw(window)
    display.update()
    #time.delay(fps)

    
    

















