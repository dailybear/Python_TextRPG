

import world
import world2
import world3
import world4
import world5
from player import Player
from collections import OrderedDict
import items



def play(i):
    print()
    print()
    print("동화속 주인공을 도와 탑을 탈출하세요")
    i.parse_world_dsl()
    player = Player()  #플레이어 설정(위치, hp, gold, 인벤토리)
    while player.is_alive() and not player.victory: #플레이어 hp가 0이상이고 victory가 참일때 아래 내용 반복
        room = i.tile_at(player.x, player.y) #룸 = 플레이어 위치(EN인지, TT인지 등)
        print(room.intro_text())#1. 인트로 텍스트 불러옴
        room.modify_player(player)#2. modify_player 불러옴
        if player.is_alive() and not player.victory: #플레이어 hp가 0이상이고 victory가 참일때
            choose_action(room, player,i)  #3. choose_action 함수로 넘어가기
        elif not player.is_alive(): #플레이어 hp가 0이하일때
            print("탑의 탈출에 실패하였습니다. 다시 도전하세요.") #아래 문구 출력
            


def get_available_actions(room, player,i):
    actions = OrderedDict()
    uses = [item for item in player.inventory if isinstance(item, items.use)]
    print("액션을 고르세요: ")
    if player.inventory: #플레이어가 아이템을 가지고 있으면
        action_adder(actions, 'i', player.print_inventory, "인벤토리")
    if isinstance(room, world.TraderTile): 
        action_adder(actions, 't', player.trade, "거래")
    
    if isinstance(room, i.EnemyTile) and room.enemy.is_alive() and not room.enemy.is_nobattle():
        action_adder(actions, 'a', player.attack, "공격")
        if uses:
            action_adder(actions, 'r', player.run, "도망치기")       
            
    elif isinstance(room, world.GameTile) and not room.floor1.is_trap():
        action_adder(actions,'t',player.game_clear,"함정 해결하기")
    elif isinstance(room, world2.GameTile) and not room.floor2.is_trap():
        action_adder(actions, 't', player.game_clear2, "숲을 탈출하자")    
    elif isinstance(room, world3.GameTile) and not room.floor3.is_trap3():
        action_adder(actions,'t',player.game_clear3,"문 열기")
    elif isinstance(room, world5.GameTile) and not room.floor5.is_trap():
        action_adder(actions, 't', player.game_clear5, "라푼젤을 구하라")
    elif isinstance(room,i.VictoryTile) and room.victory_check(): # g키가 뜸 
        action_adder(actions, 'g', player.next_stage,"아이템을 사용하여 탈출하기")

        
         
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'w', player.move_north, "위")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "아래")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'd', player.move_east, "오른쪽")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'a', player.move_west, "왼쪽")
        if player.hp < 100:
            action_adder(actions, 'h', player.heal, "힐")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{} : {}".format(hotkey, name))


def choose_action(room, player,i):
    action = None
    while not action:
        available_actions = get_available_actions(room, player,i)
        action_input = input("액션: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")
            
world_list=[world,world2,world3,world4,world5]
for i in world_list:
    play(i)
    

