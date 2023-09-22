
class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def is_nobattle(self):
        return self.nobattle


#st1,st2
class wizard(Enemy): #wizard를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "마법사" #name은 마법사이다.
        self.hp = 60 #hp는 60이다.
        self.damage = 10 #damage는 10이다.
        self.nobattle = False
#st1,st2
class wizard_subordinate(Enemy): #wizard_subordinate를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "마법사의 부하" #name은 마법사 부하이다.
        self.hp = 25 #hp는 25이다.
        self.damage = 5 #damage는 5이다.
        self.nobattle = False
#st1,st5
class bandit(Enemy): #bandit를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "도적" #name은 강도이다.
        self.hp = 20 #hp는 20이다.
        self.damage = 5 #damage는 5이다.
        self.nobattle = False
#st1,st2,st3
class guard(Enemy): #guard를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "경비원" #name은 경비이다.
        self.hp = 30 #hp는 30이다.
        self.damage = 5 #damage는 5이다.
        self.nobattle = False
        
#st 2
class Hunter(Enemy): #Hunter를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "사냥꾼" #name은 사냥꾼이다.
        self.hp = 35 #hp는 35이다.
        self.damage = 5 #damage는 5이다.

#st3
class Stepmother(Enemy): #Stepmother를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "새 엄마" #name은 새엄마이다.
        self.hp = 60 #hp는 60이다.
        self.damage = 10 #damage는 10이다.
#st3
class Stepsister(Enemy): #Stepsister를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "새 언니" #name은 새언니이다.
        self.hp = 20 #hp는 20이다.
        self.damage = 3 #damage는 3이다.
#st3
class retinue(Enemy): #retinue를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "수행원" #name은 수행원이다.
        self.hp = 25 #hp는 25이다.
        self.damage = 5 #damage는 5이다.
#st4,st5   
class witch(Enemy): #witch를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "마녀" #name은 마녀이다.
        self.hp = 80 #hp는 80이다.
        self.damage = 10 #damage는 12이다.
#st4, st5
class witch_subordinate(Enemy): #witch_subordinate를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "마녀의 부하" #name은 마녀 부하이다.
        self.hp = 20 #hp는 20이다.
        self.damage = 6 #damage는 6이다.
#st4, st5
class Oldwoman(Enemy): #Oldwoman를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "노파" #name은 노파이다.
        self.hp = 20 #hp는 20이다.
        self.damage = 7 #damage는 7이다.