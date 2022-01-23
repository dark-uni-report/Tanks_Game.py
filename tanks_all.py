import pygame, sys, math
import runpy
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, a):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rot = True
        self.mov = False
        self.shoot = False
        self.a = a
        self.flag = 0
        self.run = True
        self.rot_arg_1 = 0
        self.rot_arg_2 = 0
        self.check = False



#pygame.init()

def Start():
    pygame.init()
    timer = pygame.time.Clock()
    w = pygame.display.set_mode((910, 512))
    background = pygame.image.load('menu_window.jpg')
    background_rect = background.get_rect()
    p1 = Player("start.png", 455, 256)
    p1_cp = p1.image
    p1_r = p1_cp.get_rect(center = (p1.x, p1.y))
    print(p1_r)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
		    x, y = pygame.mouse.get_pos() 
		    if x > 386 and x < 541 and y > 189 and y < 323:
                        pygame.quit()
			#runpy.run_module('start_33.py')
                        #os.system('start_3.py')
			#sys.exit()
			Play()

        w.blit(background, background_rect)
        w.blit(p1.image, p1_r)                    
        pygame.display.update()


def Play():
        #pygame.init()
        #w = (pygame.display.set_mode((910, 512)), pygame.RESIZABLE)
        w = pygame.display.set_mode((910, 512))


        background = pygame.image.load('grass.jpg')
        background_rect = background.get_rect()
        p1 = Player("tank_11.png", 50, 40, 0)
        p2 = Player("tank_21.png", 850, 450, 0)
        b1 = Player("bullet_11.png", -100, -100, 0)
        b1_cp = b1.image
        b2 = Player("bullet_22.png", -100, -100, 0)
        b2_cp = b2.image


        sides = []
        sides.append(Player("side_11.png", 404, 200, 0))
        sides.append(Player("side_12.png", 404, 262, 0))
        sides.append(Player("side_14.png", 351, 232, 0))
        sides.append(Player("side_14.png", 289, 232, 0))
        sides.append(Player("side_14.png", 800, 242, 0))
	sides.append(Player("side_13.png", 250, 70, 0))
        sides.append(Player("side_15.png", 522, 22, 0))
        sides.append(Player("side_14.png", 478, 433, 0))
        sides.append(Player("side_14.png", 540, 433, 0))
        sides.append(Player("side_13.png", 755, 481, 0))
        sides.append(Player("side_15.png", 458, 22, 0))
        sides.append(Player("side_14.png", 702, 490, 0))
        sides.append(Player("side_14b.png", 32, 250, 0))
        sides.append(Player("side_16.png", 685, 110, 0))
        sides.append(Player("side_17.png", 230, 390, 0))
        sides.append(Player("side_17.png", 590, 250, 0))
        sides.append(Player("side_16.png", 560, 297, 0))
        sides.append(Player("side_18.png", 52, 491, 0))


        exb1 = Player("ex_p2.png", -100, -100, 0) 
        exb1_cp = exb1.image
        exb1_r = exb1_cp.get_rect(center = (-100, -100))
        exb2 = Player("ex_p2.png", -100, -100, 0) 
        exb2_cp = exb1.image
        exb2_r = exb1_cp.get_rect(center = (-100, -100))


        ex1 = Player("ex.png", -100, -100, 0)
        ex1_cp = ex1.image
        ex2 = Player("ex.png", -100, -100, 0)
        ex2_cp = ex2.image


	stop = Player("stopp.png", 400, 30, 0)
        stop_cp = stop.image
        stop_r = stop_cp.get_rect(center = (53, 492))


        menu = Player("menuu.png", 400, 30, 0)
	menu_cp = menu.image
        menu_r = menu_cp.get_rect(center = (32, 251))
 

        win_1 = Player("blue_win1.jpg", 400, 30, 0)
        win_2 = Player("red_win1.jpg", 400, 30, 0)
        win_1_cp = win_1.image
        win_1_r = win_1_cp.get_rect(center = (455, 256))
        win_2_cp = win_2.image
        win_2_r = win_2_cp.get_rect(center = (455, 256))



    timer = pygame.time.Clock()
    points1 = 0
    points2 = 0
    
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    p1.rot = False
                    p1.mov = True
                    p1.rot_arg_1 += 1                
                    if not b1.shoot:
                        b1.x = p1.x
                        b1.y = p1.y
                        b1.a = p1.a       
                    b1 = Player("bullet_22.png", b1.x, b1.y, b1.a)
                    b1.shoot = True
                elif e.key == pygame.K_w:
                    p2.rot = False
                    p2.mov = True
                    p2.rot_arg_2 += 1
                    if not b2.shoot:
                        b2.x = p2.x
                        b2.y = p2.y
                        b2.a = p2.a
                    b2 = Player("bullet_11.png", b2.x, b2.y, b2.a)              
                    b2.shoot = True
                elif e.key == pygame.K_SPACE:
                    if p1.check or p2.check:
                        pygame.quit()
                        #runpy.run_module('start_4.py')
                        #sys.exit()
                Start()
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    p1.rot = True
                    p1.mov = False
                elif e.key == pygame.K_w:
                    p2.rot = True
                    p2.mov = False    
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1 and p1.run and p2.run:
                    x, y = pygame.mouse.get_pos() 
                    if x > 32 and x < 74 and y > 471 and y < 512:
                        stop = Player("startt.png", 400, 30, 0)
                        stop_cp = stop.image
                        stop_r = stop_cp.get_rect(center = (53, 492))                    
                        p1.run = False
                        p2.run = False
                        b1.shoot = False
                        b2.shoot = False
                        b1.x = -100
                        b1.y = -100
                        b2.x = -100
                        b2.y = -100                    
                    elif x > 6 and x < 58 and y > 226 and y < 276:
                        pygame.quit()
                        #runpy.run_module('start_4.py')
                        #os.system('start_3.py')
                        #sys.exit()  
                Start()
                elif e.button == 1 and not p1.run and not p2.run:
                    stop = Player("stopp.png", 400, 30, 0)
                    stop_cp = stop.image
                    stop_r = stop_cp.get_rect(center = (53, 492))                
                    x, y = pygame.mouse.get_pos() 
                    if x > 32 and x < 74 and y > 471 and y < 512:
                        p1.run = True
                        p2.run = True                   
                    elif x > 6 and x < 58 and y > 226 and y < 276:
                        pygame.quit()
                        #runpy.run_module('start_4.py')
                        #os.system('start_3.py')
                        #sys.exit() 
                Start()
    
        exb1.x = -100
        exb1.y = -100
        exb2.x = -100
        exb2.y = -100
        ex1.x = -100
        ex2.x = -100
        ex1.y = -100
        ex2.y = -100
        t = 0    
        if b1.shoot and p1.run:
            b1_cp = pygame.transform.rotate(b1.image, b1.a % 360)
            db1 = (math.pi / 180) * (b1.a % 360)
            dbx1 = abs(30 * math.cos(db1))
            dby1 = abs(30 * math.sin(db1))
            if 0 <= db1 <= math.pi / 2:
                sbx1 = 1
                sby1 = -1
            elif math.pi / 2 < db1 <= math.pi:
                sbx1 = -1
                sby1 = -1
            elif math.pi < db1 <= 1.5 * math.pi:
                sbx1 = -1
                sby1 = 1
            elif 1.5 * math.pi < db1 <= 2 * math.pi:
                sbx1 = 1
                sby1 = 1
            if b1.x > 0 and b1.x < 910 and b1.y > 0 and b1.y < 512:
                b1.x += sbx1 * dbx1
                b1.y += sby1 * dby1
                b1_a = b1.image.get_rect(center = (b1.x, b1.y))
                for s in sides:
                    if b1_a.colliderect(s.image.get_rect(center = (s.x, s.y))):
                        t = 0.5
                        exb1.x = b1.x
                        exb1.y = b1.y
                        b1.x = -100    
                        b1.y = -100    
                        b1.shoot = False       
                        break
            else:
                b1.x = -100   
                b1.y = -100   
                b1.shoot = False
                
        if b2.shoot and p2.run:
            b2_cp = pygame.transform.rotate(b2.image, b2.a % 360)
            db2 = (math.pi / 180) * (b2.a % 360)
            dbx2 = abs(30 * math.cos(db2))
            dby2 = abs(30 * math.sin(db2))
            if 0 <= db2 <= math.pi / 2:
                sbx2 = 1
                sby2 = -1
            elif math.pi / 2 < db2 <= math.pi:
                sbx2 = -1
                sby2 = -1
            elif math.pi < db2 <= 1.5 * math.pi:
                sbx2 = -1
                sby2 = 1
            elif 1.5 * math.pi < db2 <= 2 * math.pi:
                sbx2 = 1
                sby2 = 1
            if b2.x > 0 and b2.x < 910 and b2.y > 0 and b2.y < 512:
                b2.x += sbx2 * dbx2
                b2.y += sby2 * dby2
                b2_a = b1.image.get_rect(center = (b2.x, b2.y))            
                for s in sides:
                    if b2_a.colliderect(s.image.get_rect(center = (s.x, s.y))):
                        t = 0.5
                        exb2.x = b2.x
                        exb2.y = b2.y
                        b2.x = -100
                        b2.y = -100
                        b2.shoot = False         
                        break
            else:
                b2.x = -100
                b2.y = -100
                b2.shoot = False
           
        if p1.rot and p1.run:
            if p1.rot_arg_1 % 2 == 0:
                p1.a += 10
            else:
                p1.a -= 10
            p1_cp = pygame.transform.rotate(p1.image, p1.a)
        elif p1.mov and p1.run:
            p1_cp = pygame.transform.rotate(p1.image, p1.a % 360)
            d1 = (math.pi / 180) * (p1.a % 360)
            dx1 = abs(10 * math.cos(d1))
            dy1 = abs(10 * math.sin(d1))
            if 0 <= d1 <= math.pi / 2:
                sx1 = 1
                sy1 = -1
            elif math.pi / 2 < d1 <= math.pi:
                sx1 = -1
                sy1 = -1
            elif math.pi < d1 <= 1.5 * math.pi:
                sx1 = -1
                sy1 = 1
            elif 1.5 * math.pi < d1 <= 2 * math.pi:
                sx1 = 1
                sy1 = 1
            p1.x += sx1 * dx1
            p1.y += sy1 * dy1
            #if p1_r.colliderect(p2_r):
                #p1.x -= 10
                #p1.y -= 10
            p1_a = p1.image.get_rect(center = (p1.x, p1.y))
            for s in sides:
                if p1_a.colliderect(s.image.get_rect(center = (s.x, s.y))):
                    p1.x -= sx1 * dx1
                    p1.y -= sy1 * dy1
            if p1.x >= 894 or p1.x <= 16:
                p1.x -= sx1 * dx1
            if p1.y >= 496 or p1.y <= 16:
                p1.y -= sy1 * dy1        
        if p2.rot and p2.run:
            if p2.rot_arg_2 % 2 == 0:
                p2.a -= 10
            else:
                p2.a += 10        
            p2_cp = pygame.transform.rotate(p2.image, p2.a)
        elif p2.mov and p2.run:
            p2_cp = pygame.transform.rotate(p2.image, p2.a % 360) 
            d2 = (math.pi / 180) * (p2.a % 360)
            dx2 = abs(10 * math.cos(d2))
            dy2 = abs(10 * math.sin(d2))
            if 0 <= d2 <= math.pi / 2:
                sx2 = 1
                sy2 = -1
            elif math.pi / 2 < d2 <= math.pi:
                sx2 = -1
                sy2 = -1
            elif math.pi < d2 <= 1.5 * math.pi:
                sx2 = -1
                sy2 = 1
            elif 1.5 * math.pi < d2 <= 2 * math.pi:
                sx2 = 1
                sy2 = 1
            p2.x += sx2 * dx2 
            p2.y += sy2 * dy2
            p2_a = p1.image.get_rect(center = (p2.x, p2.y))
            for s in sides:
                if p2_a.colliderect(s.image.get_rect(center = (s.x, s.y))):
                    p2.x -= sx2 * dx2
                    p2.y -= sy2 * dy2
            if p2.x >= 894 or p2.x <= 16:
                p2.x -= sx2 * dx2
            if p2.y >= 496 or p2.y <= 16:
                p2.y -= sy2 * dy2
                
                
        p1_r = p1_cp.get_rect(center = (p1.x, p1.y))
        p2_r = p2_cp.get_rect(center = (p2.x, p2.y))
        b1_r = b1_cp.get_rect(center = (b1.x, b1.y))
        b2_r = b2_cp.get_rect(center = (b2.x, b2.y))
            
                
        if p1_r.colliderect(b2_r):
            t = 0.5
            b2.x = -100
            b2.y = -100
            points2 += 1
            ex1.x = p1.x
            ex1.y = p1.y
            p1.rot = False
            p1.mov = False
        if p2_r.colliderect(b1_r):
            t = 0.5
            b1.x = -100
            b1.y = -100
            points1 += 1
            ex2.x = p2.x
            ex2.y = p2.y
            p2.rot = False
            p2.mov = False
                
                
        
        w.fill((0, 0, 0))
        w.blit(background, background_rect)
        b1_r = b1_cp.get_rect(center = (b1.x, b1.y))
        w.blit(b1_cp, b1_r)
        b2_r = b2_cp.get_rect(center = (b2.x, b2.y))
        w.blit(b2_cp, b2_r)
        w.blit(p1_cp, p1_r)
        w.blit(p2_cp, p2_r)
        exb1_r = exb1_cp.get_rect(center = (exb1.x, exb1.y))
        w.blit(exb1_cp, exb1_r)
        exb2_r = exb2_cp.get_rect(center = (exb2.x, exb2.y))
        w.blit(exb2_cp, exb2_r)
        ex1_r = ex1_cp.get_rect(center = (ex1.x, ex1.y))
        w.blit(ex1_cp, ex1_r)
        ex2_r = ex2_cp.get_rect(center = (ex2.x, ex2.y))
        w.blit(ex2_cp, ex2_r)  
        #time.sleep(t)
        
        
        for i in range(len(sides)):
            w.blit(sides[i].image, sides[i].image.get_rect(center = (sides[i].x, sides[i].y)))
            
        
    
        font = pygame.font.Font(None, 30)
        text1 = font.render("Blue: " + str(points1), True, (30, 0, 255))
        text2 = font.render("Red: " + str(points2), True, (255, 0, 0))
        w.blit(text1, (700, 10))
        w.blit(text2, (700, 30))
        w.blit(stop_cp, stop_r)
        w.blit(menu_cp, menu_r)
        if points1 == 10:
            p1.check = True
            p1.run = False
            p2.run = False
            w.blit(win_1_cp, win_1_r)
        elif points2 == 10:
            p2.check = True
            p1.run = False
            p2.run = False
            w.blit(win_2_cp, win_2_r)
        pygame.display.update()
        timer.tick(20)


Start()
