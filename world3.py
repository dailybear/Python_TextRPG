



# random과 enemies, Characters모듈 불러오기
import random
import enemies
import Characters
import items
import trapGame3

# 타일들의 기본이 되는 상위 클래스
class MapTile:
    def __init__(self, x, y): # 파라미터 두개
        self.x = x # x의 값을 x로 초기화
        self.y = y # y의 값을 y로 초기화

    def intro_text(self): #파라미터 없음
        raise NotImplementedError("Create a subclass instead!")
        '''
        오류를 일부러 발생시키기 위해 사용
        부모 클래스를 상속받는 자식 클래스에서 반드시 intro_text(self)함수를 구현하도록 할 때 사용
        자식 클래스에서 함수를 구현하지 않았을 경우 오류 발생
        "NotImplementedError는 파이썬 내장 오류로, 
        꼭 작성해야하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다."
        '''
    def modify_player(self, player): #파라미터 1개
        pass

# 시작 타일 : 게임 시작 타일
class StartTile(MapTile): # 상위 클래스: MapTile
    def intro_text(self): # intro_text(self)메소드 오버라이딩
        return """
        스테이지3 : 신데렐라\n
        
        신데렐라의 새 엄마와 새 언니들이 신데렐라의 유리구두를 노리고 있습니다.
        신데렐라를 도와 신데렐라가 잃어버린 유리구두를 찾아주세요.
        """
        # 위의 문장 반환

# 지루한 타일 : 아무것도 없음
class BoringTile(MapTile): # 상위 클래스: MapTile
    def intro_text(self):   # intro_text(self)메소드 오버라이딩
        return """
        이 곳에는 아무것도 없네요.
        """
        # 위의 문장 반환

# 게임 승리 타일
class VictoryTile(MapTile): # 상위 클래스: MapTile
    def __init__(self, x, y): # 파라미터 두개
        self.vic=False
        super().__init__(x, y)
        
        
    def intro_text(self): # intro_text(self)메소드 오버라이딩
        return """
        탈출위치에 도착했습니다.
        신데렐라에게 잃어버린 유리구두를 찾아 돌려주고 탈출에 성공하세요!
        
        """
        # 위의 문장 반환
    
        
    def victory_check(self): # vic값 불러옴
        #print(self.vic)
        return self.vic    
    
    def modify_player(self, player): #파라미터 1개
        if GameTile.item in player.inventory: #인벤토리에 카펫이 있는지 검사
            print("유리구두를 신은 신데렐라가 왕자에게 청혼에 성공했습니다. 다음스테이지로 이동합니다.")
            print("[다음 스테이지로 이동시 인벤토리 및 골드는 초기화됩니다.]")
            self.vic=True #있으면 vic를 T로 바꿈

# 적 타일 : 해당 타일에서 적 등장
class EnemyTile(MapTile): # 상위 클래스: MapTile
    def __init__(self, x, y):   #파라미터 2개
        r = random.random() #r에 랜덤값을 저장
        if r < 0.50:    
            self.enemy = enemies.Stepmother()#새엄마
            self.alive_text = "신데렐라의 새 엄마가 당신을 노리고 있습니다. " \
                              "어서 물리치세요!"
            self.dead_text = "신데렐라의 새엄마를 물리쳤습니다." 
                             
            self.run_text = ""
        elif r < 0.80:
            self.enemy = enemies.Stepsister()#새언니
            self.alive_text = "신데렐라의 새언니가 나타났습니다! "
            self.dead_text = "신데렐라의 새언니를 이겼습니다."
            self.run_text = ""
        elif r < 0.95:
            self.enemy = enemies.retinue()#수행원
            self.alive_text = "수행원이 나타났습니다. 신데렐라와 유리구두를 지키세요!"
            self.dead_text = "수행원을 물리치고 무사히 도망쳤습니다."
            self.run_text = ""
        else:
            self.enemy = enemies.guard()
            self.alive_text = "경고. 외부인 침입!" \
                               "경비대원에게 걸렸습니다. 경비대원을 물리치고 도망치세요!"
            self.dead_text = "경비대원에게서 무사히 도망쳤습니다."
            self.run_text = ""
        '''
        r값에 따라 self.enemy에 각각 enemies모듈의 적 정보 클래스를 저장
        self.alive_text와 self.dead_text에 적에 알맞은 문구 저장
        '''
        
        super().__init__(x, y) # 부모 클래스의 __init__을 불러옴
        

    def intro_text(self):   # 파라미터 없음
        if self.enemy.is_nobattle():
            text=self.run_text

        elif self.enemy.is_alive():
            text = self.alive_text

        else:
            text = self.dead_text
         # 살 경우 self.alive_text, 즉은 경우 self.dead_text를 text에 저장
        return text # text 반환

    def modify_player(self, player): # 파라미터 1개
        #uses = [item for item in player.inventory if isinstance(item, items.use)]
        if self.enemy.is_nobattle():
            return
        
        # elif not uses:
        #     player.run()
        
        elif self.enemy.is_alive(): # 살았으면
            player.hp = player.hp - self.enemy.damage   # 플레이어의 hp = hp - damage
            print("적의 hp가 {}만큼 손상되었습니다. 당신은 {} HP가 남았습니다." 
                .format(self.enemy.damage, player.hp))    # "Enemy does {(self.enemy.damage)} damage. You have {(player.hp)} HP remaining." 를 출력
  
class GameTile(MapTile):
    item=items.GlassShoes()
    def __init__(self, x, y):
        #self.trap = False# 함정 변수에 False 저장
        self.floor3=trapGame3.floor3()  
        
        self.gold = random.randint(1, 50) # 클리어 시 받을 골드 1~50사이 랜덤으로 저장
        #self.item = [items.GlassShoes()]
        self.gold_claimed = False
        self.item_claimed = False
        super().__init__(x, y)
    
    
    
    def intro_text(self): # 입장 시 출력 문구
        if self.floor3.is_trap3(): #trap함수 반환값이 True일때
            if not self.floor3.is_noclear3():
                return """ 함정을 탈출했어요. 계속 나아가세요! """
            else:
                return """ 함정 해결에 실패했습니다. 다시 도전하세요."""
        else:
            return """
            앗, 함정에 빠졌어요! 
            문제를 해결해 함정을 통과하세요!
            """        

    def modify_player(self, player):
        if not self.floor3.is_noclear3(): #문제를 못 풀지 않으면
            if not self.gold_claimed and not self.item_claimed:
                player.gold = player.gold + self.gold # 플레이어의 골드에 랜덤으로 받은 골드 추가
                print("+{}골드가 추가되었습니다.".format(self.gold))
                player.inventory.append(self.item)
                print("스테이지 탈출에 필요한 유리구두를 얻었습니다.\n")
                self.gold_claimed = True  # 타일에 또갔을때 골드 안줄라고 해놓은거
                self.item_claimed = True
                return
        



# 거래장소
class TraderTile(MapTile): # 상위클래스 MapTile
    def intro_text(self): # intro_text(self)메소드 오버라이딩
        return """
        누군가 여러가지 물품을 팔고 있습니다.
        아이템을 구매하거나 물건을 팔 수 있을 것 같습니다.
        """

    def __init__(self,x,y): # 파라미터 2개
        self.trader = Characters.Trader() #self.trade에 Characters모튤의 Trader 클래스 호출
        super().__init__(x, y) # 부모 클래스의 __init__을 불러옴

    def trade(self, buyer, seller): # 파라미터 2개
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {}골드".format(i, item.name, item.value))    #  i. 아이템 이름 - 아이템값(gold) 출력  
    
        while True:
            user_input = input("아이템을 고르세요(나가기: q / Q): ") #  user_input: 아이템 선택을 위한 입력 받기
            if user_input in ['Q', 'q']: #  user_input에 q나 Q가 있으면 창닫기(아이템창 나가기)
                return
            
            else:
                try:
                    choice = int(user_input)    #아이템 번호을 받아서 choice에 저장
                    to_swap = seller.inventory[choice - 1]  # to_swap: 인벤토리 리스트에서 번호에 알맞은 아이템 저장
                    self.swap(seller, buyer, to_swap) # to_swap에 저장된 아이템을  교환
                except ValueError: #위에서 오류 발생시
                    print("Invalid Choice!") # "Invalid Choice!" 문구 출력

    def swap(self, seller, buyer, item):  # 파라미터 3개
        if item.value > buyer.gold:
            print("돈이 부족해요!")   # item.value이 buyer.gold보다 큰경우 "돈이 부족해요!" 문구 출력
            return
        
        buyer.inventory.append(item)    #buyer의 인벤토리에 해당 아이템 추기
        seller.gold = seller.gold + item.value   # seller: gold = gold + value
        buyer.gold = buyer.gold - item.value    # buyer: gold = gold - value
        print("거래 성공")        # "거래 성공" 출력

    def check_if_trade(self, player):
        while True:
            print("거래하시겠습니까? 거래 요청(B) / 나가기(Q)를 누르세요")    # "거래하시겠습니까? 거래 요청(B) / 나가기(Q)를 누르세요" 출력
            user_input = input() # 입력받기
            if user_input in ['q', 'Q']:
                return  # Q 입력시 거래 종료
            elif user_input in ['B', 'b']:
                print("아이템: ")    # B 입력시 아이템 사기
                self.trade(buyer = player, seller = self.trader) # 사는사람 = 사용자, 파는사람 = trader
            else:
                print("Invalid choice!")    # Q, B가 아닌경우 "Invalid choice!" 출력

# 금 발견 장소
class FindGoldTile(MapTile):
    def __init__(self, x, y):   # 파라미터 2개
        self.gold = random.randint(1, 50)   # gold : 1부터 50까지의 랜덤 정수
        self.gold_claimed = False
        super().__init__(x, y)  # 부모 클래스의 __init__을 불러옴

    def modify_player(self, player):    # 파라미터 1개
        if not self.gold_claimed:   # if not self.gold_claimed: 가 True이므로 if문 실행 
            self.gold_claimed = True   # self.gold_claimed을 True로 저장
            player.gold = player.gold + self.gold   # 플레이어의 gold = 원래 gold + 새로 찾은 gold
            print("+{}골드가 추가되었습니다.".format(self.gold)) # "+{}골드가 추가되었습니다." 출력

    def intro_text(self):
        if self.gold_claimed: # self.gold_claimed가 True면 아래 문구 출력
            return"""
            탑의 비밀공간인것 같네요
            앞으로 나아가세요
            """
        else: # False면 아래 문구 출력
            return"""
            누군가 골드를 떨어뜨렸네요. 골드를 주웠습니다.
            """

class WeaponTile(MapTile):
    def __init__(self, x, y):   # 파라미터 2개
        self.weapon_list = [items.Rock(),
                            items.Dagger(),
                            items.RustySword(),
                            items.Mazeltov(),
                            items.Crossbow()]        
        self.weapon = self.weapon_list[random.randint(0, 4)]   # gold : 1부터 50까지의 랜덤 정수
        self.weapon_claimed = False
        super().__init__(x, y)  # 부모 클래스의 __init__을 불러옴

    def modify_player(self, player):    # 파라미터 1개
        if not self.weapon_claimed:   # if not self.gold_claimed: 가 True이므로 if문 실행 
            self.weapon_claimed = True   # self.gold_claimed을 True로 저장
            player.inventory.append(self.weapon)
            print("인벤토리에 {}가 추가되었습니다.".format(self.weapon)) # "+{}골드가 추가되었습니다." 출력

    def intro_text(self):
        if self.weapon_claimed: # self.gold_claimed가 True면 아래 문구 출력
            return"""
            탑의 비밀공간인것 같네요
            앞으로 나아가세요
            """
        else: # False면 아래 문구 출력
            return"""
            쓸만한 무기가 보입니다. 무기를 주웠습니다.
            """

# '|'개수 판단
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:  # dsl에 |ST|가 1번 있지 않으면 
        return False            # False 반환                                            
    if dsl.count("|VT|") == 0:  # dsl에 |VT|가 없으면
        return False            # False 반환                                         
    lines = dsl.splitlines()    # lines : dsl을 줄바꿈을 기준으로 리스트 생성
    lines = [l for l in lines if l] 
    pipe_counts = [line.count("|") for line in lines]   #lines 리스트 각 원소의 '|'의 갯수를 출력
    
    # 리스트 각 원소에 '|'가 없을때만 True 있으면 False로 반환
    for count in pipe_counts:   
        if count != pipe_counts[0]:    
            return False

    return True 
    

# 맵을 분석하는 함수
def parse_world_dsl():
    if not is_dsl_valid(world_dsl): #is_dsl_valid에 world_dsl 넣지 않을경우
        raise SyntaxError("DSL is invalid")    #"DSL is invalid" 출력

    dsl_lines = world_dsl.splitlines()  # dsl_lines : dsl을 줄바꿈을 기준으로 리스트 생성
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):   
        row = []    # row를 빈 리스트로 초기화
        dsl_cells = dsl_row.split("|")  # dsl_row를 '|' 마다 나눠서 dsl_cells에 저장
        dsl_cells = [c for c in dsl_cells if c]     # dsl_cells를 리스트로 저장
        for x, dsl_cell in enumerate(dsl_cells):    
            tile_type = tile_type_dict[dsl_cell]    # tile_type: tile_type_dict 딕셔너리에 dsl_cell들을 하나씩 대입
            if tile_type == StartTile:  # tile_type과 StartTile이 같으면
                global start_tile_location  # 지역변수 start_tile_location를 전역변수로 바꿈
                start_tile_location = x, y  # 위치 설정
            row.append(tile_type(x, y) if tile_type else None)  # tile_type이 존재하면 tile_type(x,y)를 row에 추가

        world_map.append(row)   # world_map에 row 추가

# 맵 오류 막는 함수
def tile_at(x, y):  # 파라미터 두개
    if x < 0 or y < 0:
        return None     # x,y가 0보다 작으면 아무 것도 반환하지 않음
    try:
        return world_map[y][x]  # world_map[y][x] 반환
    except IndexError:
        return None #오류 발생시 아무 것도 반환하지 않는다

# 맵 설정
world_dsl = """
|FG|ST|GT|  |FG|
|WT|EN|  |EN|TT|
|EN|EN|WT|  |EN|
|  |  |FG|EN|EN|
|  |VT|EN|TT|  |
"""

world_map = [] # world_map를 빈 리스트로 초기화

# 딕셔너리 설정
tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "WT": WeaponTile,
                  "GT": GameTile,
                  "  ": None}

# start_tile_location을 None으로 설정
start_tile_location = None
