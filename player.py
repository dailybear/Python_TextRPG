""" Text adventure game
    @insta = @lakshaytalkstocomputer
    @year  = 2018
"""
__author__ = "lakshaytalkstocomputer"

import items
import world
import world2
import world3
import world5
#import trapGame3


class Player:
    def __init__(self):
        self.inventory = [items.HealingPotion(),
                          items.Dagger(),
                          items.run(),
                          items.run(),
                          items.run()]

        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 5
        self.victory = False
            
    def next_stage(self): #g키 누르면 빅토리 값 바뀜
        self.victory=True    

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("[인벤토리]")
        for item in self.inventory:
            print("*" + str(item))
        print("*골드 : {}".format(self.gold))
        best_weapon = self.most_powerful_weapon()
        print("가장 강한 무기 : {} ".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("{}을(를) 사용해 {}를(을)공격했습니다!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("{}를(을) 해치웠습니다!".format(enemy.name))
        else:
            print("{}의 HP가 {}만큼 남았습니다.".format(enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("회복에 사용할 수 있는 아이템이 없습니다.")
            return

        for i, item in enumerate(consumables,1):
            print("회복에 사용할 아이템을 선택하세요 : ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("현재 HP : {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid Choice, try again.")

    def run(self):
        uses = [item for item in self.inventory if isinstance(item, items.use)]
        #uses = player.inventory.
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy

        to_run = uses[0] 
        self.inventory.remove(to_run) 
        print("{}에게서 도망치기에 성공했습니다.".format(enemy.name)) 
        print("남은 도망용 아이템 수 : {}".format(len(uses)-1))
        enemy.nobattle = True
        return

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)


# 함정 게임 함수
    def game_clear(self):
        room = world.tile_at(self.x, self.y) # room에 타일 위치 저장
        #room.world_game_clear(self) # world의 world_gmae_clear(함정게임타일함수) 실행
        check = room.floor1.check_answer()
        
        if check:
            room.floor1.trap = True  # 게임 함수가 실행 되면 T
            room.floor1.noclear=False  #답이 맞았을 때 False로 변환
            return
        else:
            room.floor1.trap = True  # 게임 함수가 실행 되면 T
            room.floor1.noclear=True  # 답이 틀렸을때 True로 변환
            return
# 2층 함정
    def game_clear2(self):
        room = world2.tile_at(self.x, self.y) # room에 타일 위치 저장
        check = room.floor2.check_answer()
        
        if check:
            room.floor2.trap = True  # 게임 함수가 실행 되면 T
            room.floor2.noclear = False  #답이 맞았을 때 False로 변환
            return
        else:
            room.floor2.trap = True  # 게임 함수가 실행 되면 T
            room.floor2.noclear=True  # 답이 틀렸을때 True로 변환
            return 
# 3층 함정
    def game_clear3(self):
        room = world3.tile_at(self.x, self.y) # room에 타일 위치 저장
        #room.world_game_clear(self) # world의 world_gmae_clear(함정게임타일함수) 실행
        check = room.floor3.check_answer()  # 맞추면 T, 틀리면 F
        
        if check:
            room.floor3.trap = True  # 게임 함수가 실행 되면 T
            room.floor3.noclear=False  #답이 맞았을 때 False로 변환
            return
        else:
            room.floor3.trap = True  # 게임 함수가 실행 되면 T
            room.floor3.noclear=True  # 답이 틀렸을때 True로 변환
            return   
# 5층 함정
    def game_clear5(self):
        room = world5.tile_at(self.x, self.y) # room에 타일 위치 저장
        check = room.floor5.check_answer()
        
        if check:
            room.floor5.trap = True  # 게임 함수가 실행 되면 T
            room.floor5.noclear = False  #답이 맞았을 때 False로 변환
            return
        else:
            room.floor5.trap = True  # 게임 함수가 실행 되면 T
            room.floor5.noclear=True  # 답이 틀렸을때 True로 변환
            return 
        
#is_trap : 게임 함수가 처음 실행됐을때 바로 변환시켜서 또 해당 타일에 갔을때 게임 실행 막기
#iss_noclear : 문제에 대한 답에 따라 값 바뀜(맞으면 F, 틀리면 T)