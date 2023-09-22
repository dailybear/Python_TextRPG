# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:05:07 2022

@author: 박경미
"""
#from collections import OrderedDict
#from player import Player


class Trap3():
    def __init__(self):
        raise NotImplementedError("Dop not create Trap.")
        
    def is_trap3(self):
        return self.trap
    
    def is_noclear3(self):
        return self.noclear


# 3층 함정 체크
class floor3(Trap3):
    def __init__(self): 
        self.trap=False #타일에 왔다갔느냐
        self.noclear=True #답을 맞췄느냐
        
    def check_answer(self):
        answer = False    # 함정 클리어 여부 False
        cnt =0
        floor3.floor3_intro_text(self) # 함정타일 인트로텍스트(방이잠겨있다.)
        choose = 'a'
        while (choose not in ['s','S']):
            print("어디를 살펴볼까? ")
            print("s : 금고를 살펴본다.")
            print("b : 바닥을 살펴본다.")
            print("l : 등잔을 살펴본다.")
            choose=input()
            
            if choose=='s' or choose=='S':
                floor3.find_safe(self)
                break
            elif choose=='b'or choose=='B':
                floor3.find_bottom(self)
            elif choose=='l'or choose=='L':
                floor3.find_underLamp(self)
            else:
                print("Invalid action!")
            
        while (answer != True and cnt<5): # 다섯번 돌림
            choice = input("answer : ")
            password = "1242012"
            if choice == password:
                floor3.find_key()
                answer = True
                return answer  #맞추면 True 반환
            else:
                print("비밀번호가 틀렸습니다.")
                cnt+=1
                
        print("기회를 모두 소진해 함정 해결에 실패했습니다.")
        return answer #틀리면 False 반환
        '''
        if floor3.find_safe(self,player) == True: # find클래스에 있는 금고, 바닥, 등잔을 살펴보고 열쇠를 획득하면 True로 바뀐다.
            answer = True # 열쇠 획득시 클리어 여부 True로 적용
            return answer
        '''
#class find(Trap3): # find 클래스(금고, 등잔, 바닥을 살펴본다.)
    def find_safe(self): # 금고를 살핀다.
        print("구석에 금고가 보입니다.")
        print("금고 속에 무언가 있을 것 같습니다.")
        print("자세히 보니 네 자리 수의 숫자로 이루어진 비밀번호를 맞추면 열 수 있을 것 같습니다.")
        print("""
            ⢠⡞⠛⠛⠛⠛⠛⠉⠙⠛⠛⠛⠛⠋⠛⠛⠛⠛⢳⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⠀⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⠀⢈⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⢠⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⠸⣼⠇⠀⣠⠞⣏⣹⣉⡗⢦⡀⢠⡖⡆⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⠀⡇⠀⢰⠛⡶⠋⠀⠈⢳⡚⢣⢸⡇⡇⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⠀⡇⠀⢸⣈⣳⡀⠀⠀⣰⣋⡸⢸⡇⡇⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⢠⢷⡄⠀⠻⣄⡏⢳⠛⣇⡼⠁⠘⢧⠇⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⠘⡾⠃⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢸⠀⠸⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡇⠀⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡼⠀⢠⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠸⣅⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸⠇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠯⠭⠽⠉⠉⠉⠉⠉⠉⠉⠉⠉⠯⠭⠽⠉⠁
              """)
              
        print()
        print(" 자세히 보니 금고의 옆면에 힌트가 적혀있습니다.")
        print(" 힌트 : 우리사이영원히") # 1242012
                                            
        '''          
        keyAnswer = False # 열쇠를 얻기 위한 답 
        cnt = 0 # 답을 입력한 수를 센다.
        while (keyAnswer != True and cnt<5): # 다섯번 돌림
            choice = input("answer : ") # 유저가 선택한 답
            password = "0537" # 금고의 비밀번호
            if choice == password: # 답이 비밀번호와 같다면
                keyAnswer = True # 열쇠가 True
                find.find_key() # 열쇠 도트이미지
                print(" 열쇠를 획득했습니다! ")
                
                return keyAnswer # True 반환
            else:
                print(" 비밀번호가 틀렸습니다! ")
                cnt += 1 # 비밀번호가 틀리면 카운트를 센다.
        print("기회를 모두 소진했네요. . .")
        return keyAnswer # False 반환
        '''        
            
            
    def find_bottom(self): # 바닥을 살펴봄
        
        print("""
              
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿             
              
              """)
        print(" 바닥에는 먼지가 가득합니다. 한동안 청소를 하지 않은 것 같네요.")
        print(". . .바닥에는 아무것도 보이지 않습니다.")
        
    
    def find_underLamp(self): # 등잔 근처를 살펴
       
        print()
        print("""
              ⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⣿⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠐⠲⣿⠖⠂⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⢻⡟⠉⠀⠀⠀⣿⠀⠀⠀⠉⢻⡟⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠚⢩⠋⢹⣿⡏⠙⡍⠓⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢈⣿⡁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢾⣿⣿⣿⡷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⣿⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠁
              """)
              
        print(" 등잔이 불을 환하게 밝히고 있습니다.")
        print(". . .등잔 주변엔 아무것도 보이지 않습니다.")
    
  
  
  
    def floor3_intro_text(self):    # 입장시 나오는 문구
        print()
        print()
        print(" 잠겨 있는 커다란 문에 가로막혀 이 방을 지나갈 수 없습니다. ")
        print(" 이 방을 지나가려면 문을 열 수 있는 열쇠를 찾아야 합니다. ")
        print(" 방을 둘러보고 열쇠를 찾아봅시다. ")
        print("""
            ⢰⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⡆⠀⠀⠀
        ⠀⠀⠀⢸⣿⡇⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⢸⣿⡇⠀⠀⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⢼⡧⡄⠀⠀⠀⣿
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠉⢿⠋⠁⠀⢸⡇⠀⠈⠙⡿⠉
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠹⣀⠠⡤⣸⣇⢤⠄⣀⠏⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⢸⡇⠂⠁⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣇⡀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠺⣿⣿⠗⠂
        ⠀⠀⠀⢸⣿⡇⢸⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣇⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠓
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀
        ⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡇⠀⠀⠀
        ⠀⠀⠀⠸⣿⠇⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
              """)
        
              
    def find_key(): # 열쇠 이미지
        print()
        print("""
              
          ⠀  ⠀⠀⠀⢀⡀⣴⠿⠿⣦⠀
          ⠀  ⠀⠀⣾⠟⠻⣿⡀⢀⣿⠃
          ⠀  ⠀⠈⣿⣀⢀⣼⠟⠛⣷⡀
          ⠀  ⠀⠀⠀⢉⣿⢿⣀⣀⣿⠃
           ⠀ ⠀⠀⢀⣾⡏⠀⠉⠀⠁⠀
          ⠀  ⠀⢀⡞⠻⠀⠀⠀⠀⠀⠀
          ⠀  ⢀⣾⣧⠄⠀⠀⠀⠀⠀⠀
         ⠀   ⠺⡿⡄⠀⠀⠀⠀⠀⠀⠀

              """)
        print(" 열쇠를 획득했습니다! ")
