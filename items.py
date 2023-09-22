

class Weapon:
    def __init__(self):
        raise NotImplementedError("Dop not create raw Weapon objects.")
     
    def __str__(self):
        return self.name   

# 단검(무기)
class Dagger(Weapon):
    def __init__(self):
        self.name = "단검" 
        self.description = "녹이 슬어있는 작은 단검이다. 돌보다 더 위험해 보인다.." 
        self.damage = 10 
       

# 녹슨 검(무기)
class RustySword(Weapon):
    def __init__(self):
        self.name = "러스티 소드"
        self.description = "오래된 검이지만 날이 잘 서있는 것 같다."
        self.damage = 20 
        


# 마젤토브(무기)
class Mazeltov(Weapon):
    def __init__(self):
        self.name = "횃불"
        self.description = "불이 붙은 횃불이다. 적을 태울 수 있을 것 같다." 
        self.damage = 100 
        

# 석궁(무기)
class Crossbow(Weapon):
    def __init__(self):
        self.name = "석궁" 
        self.description = "적을 꿰뚫을 수 있을 것 같은 석궁이다."
        self.damage = 70 
     


# 돌(무기)
class Rock(Weapon):
    def __init__(self):
        self.name = "돌" 
        self.description = "적에게 던져 맞추기 좋은 주먹만한 크기의 돌이다." 
        self.damage = 5


class use:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return self.name # 아이템의 이름 리턴
    
class run(use): #런아이템
    def __init__(self):
        self.name = "도망 아이템" 
        self.description = "보유할 경우 3회까지 도망이 가능하다. 횟수 소모시 아이템이 사라진다."
class carpet(use): #2층
    def __init__(self):
        self.name = "양탄자"
        self.description = "탈출 주요 아이템"
    
class antidote(use): #2층
    def __init__(self):
        self.name = "해독제"
        self.description = "탈출 주요 아이템"    
class GlassShoes(use): #3층
    def __init__(self):
        self.name = "유리구두"
        self.description = "탈출 주요 아이템"

class SpinningWheel(use):#4층
    def __init__(self):
        self.name = "물레"
        self.description = "탈출 주요 아이템"
        
class Hair(use):#5층
    def __init__(self):
        self.name = "라푼젤의 머리카락"
        self.description = "탈출 주요 아이템"


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return self.name # 소모품의 이름 리턴

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "회복포션" # 회복포션
        self.healing_value = 15 # 회복량 : 15
        self.value = 20 # 가격 : 20

class SmallHealingPotion(Consumable):
    def __init__(self):
        self.name = "미니 회복포션" # 미니 회복포션
        self.healing_value = 10 # 회복량 : 10
        self.value = 15 # 가격 : 15

class KingHealingPotion(Consumable):
    def __init__(self):
        self.name = "대왕 회복포션" # 대왕 회복포션
        self.healing_value = 25 # 회복량 : 25
        self.value = 30 # 가격 : 30

class AmazingHealingPotion(Consumable):
    def __init__(self):
        self.name = "놀라운 회복포션" # 놀라운 회복포션
        self.healing_value = 30 # 회복량 : 30
        self.value = 40 # 가격 : 40


