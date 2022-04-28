from re import L
import pygame as pg 


## 更改这里
## base 是 asset 的上一级目录
base = r'E:\CodeLearning\rf\self-play'


fru_lst = ['','Grape' , 'Cherry' , 'Orange' , 'Lemon', 'Kiwi','Tomato','Peach','Pineapple','Coconut','Semimelon' , 'Melon']

def create_fruit(type , x , y) :
    fruit = None
    try :
        print(fru_lst[type])
        fruit = eval(fru_lst[type]+ '(x,y)')
    except e :
        print(e) 
    finally :
        return fruit


class Fruit():
    def __init__(self , x , y) :
    
        self.load_images()   # init执行
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
        self.angle_degree = 0 
    
   
    def load_images(self) :
        '''
        leave subclass func to imple
        '''
        pass 

    def update_position(self,x,y,angle_degree = 0 ) :
        self.rect.x = x - self.r 
        self.rect.y = y - self.r
        self.angle_degree = angle_degree 

        
    def draw(self,surface) :
        '''
        render a pic 
        '''
        surface.blit(self.image,self.rect) 
    
class Grape(Fruit) :
    
    def __init__(self,x,y) :
        self.r = 20 
        self.type = 1 
        self.size = (self.r * 2 , self.r *2 )   
        Fruit.__init__(self, x-self.r , y - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/01.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)


class Cherry(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 30 
        self.type = 2 
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/02.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
        

class Orange(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 42
        self.type = 3
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/03.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    
    
class Lemon(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 46
        self.type = 4
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/04.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
        
    
class Kiwi(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 58
        self.type = 5
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/05.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    
class Tomato(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 70
        self.type = 6
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/06.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    
class Peach(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 74
        self.type = 7
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/07.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    

class Pineapple(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 100
        self.type = 8
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/08.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    

class Coconut(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 118
        self.type = 9
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/09.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    
class Semimelon(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 120
        self.type = 10
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/10.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)
    
class Melon(Fruit) :
    
    def __init__(self, x,y) :
        self.r = 156
        self.type = 11
        self.size = (self.r  *  2 , self.r * 2) 
        Fruit.__init__(self , x - self.r , y  - self.r) 
        
    def load_images(self):
        self.image = pg.image.load(base + '/asset/11.png') 
        self.image = pg.transform.smoothscale(self.image, self.size)