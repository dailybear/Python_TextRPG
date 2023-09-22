# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:55:34 2022

@author: 박경미
"""
import random

class Trap:
    def __init__(self):
        raise NotImplementedError("Dop not create Trap.")

    def is_trap(self):
        return self.trap
    
    def is_noclear(self):
        return self.noclear
    
class floor2(Trap):
    def __init__(self):
        self.trap=False
        self.noclear=True
        self.gameStatus = False
        
    def check_answer(self):
        answer = False
        game.fairy_intro_text(self)
        ans = game.game_start(self)
        
        if ans == True:
            answer = True
        #print("ans:", ans)
        #print("answer:",answer)    
        return answer
    
class game(Trap):
    def fairy_intro_text(self):
        print("깊은 숲에서 길을 잃었습니다.")
        print(". . . 두 요정이 나타나 당신에게 내기를 걸었습니다.")
        print("""
       ⢠⢄⡀⠀⡠⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⢄⡼⠄⠱⡜⠀⢸⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢄⢸⡀⢤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢱⠂⢌⠲⣄⡛⠀⣮⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣀⠀ ⢠⢖⣕⠅⣊⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⠈⡇⣠⣃⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡖⠐⢾⣿⣿⡿ ⠠⡑⢁⠦⠥⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠱⢄⡀⠄⢱⢹⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣷⠥⠀⠈⢉⣿⣦⣿⡤⠌⣙⡻⡂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⡄⠀⢸⢸⣿⣷⡦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠐⠢⡽⣿⣿⠹⠻⣾⢠⣮⠂⠀⠀⠀⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠈⠱⡙⣼⡇⣏⢿⣖⢌⣙⣿⣶⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣿⣿⣦⣀⠈⣳⣡⣤⣶⣶⣿⠛⠋⠉⠁⠀
⠀⠀⠀⠀⠀⣀⣔⣉⣠⣿⣇⢸⢸⣿⣾⠀⡟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣯⣿⣿⣿⣿⣿⣿⡿⠿⣿⢋⠬⢀⠀⠀⠀⠀⠀⠀
⣀⡤⣴⣿⠿⠿⠟⠛⡿⠕⠉⢿⠇⠸⡉⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⢯⣈⠫⣿⡟⠁⣀⠤⣝⡬⠭⡜⠀⠀⠀⠀⠀⠀
⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡗⡘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⣿⢨⣿⣾⣿⠠⠿⡟⡈⠁⡱⠈⠙⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡊⠺⡶⣀⣟⣵⠟⢅⠈⡷⠲⠶⠖⡊⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⢧⡆⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠒⠒⠛⠉⠈⠠⠕⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              """)
        print("우리와 내기를 해서 이기면 이 숲을 빠져나갈 수 있는 방법을 알려줄게.")
        print("대신 너가 지면 이 곳에서 평생 우리와 놀아줘야 해!")
        print("어때? 우리와 내기를 하겠어?")
        
    
    def game_start(self):
        result = False
        if game.question(self) == True:
            result = True
        return result
        
        
    def question(self):
        game_answer = False
        YESorNO = input("내기에 응할까?(yes or no) :")
        if YESorNO in ['yes', 'Yes', 'y', 'Y']:
            #game_answer = True
            if game.answer_yes(self):
                game_answer = True
            
        elif YESorNO in ['No', 'no', 'N', 'n']:
            game.answer_no(self)
        else:
            print("뭐라고? 다시 얘기해줘.\n")
        #print("game_answer:", game_answer)
        return game_answer
                
            
                
    def answer_yes(self):
        print(". . . 좋아! 잘 생각했어!")
        print("게임은 간단해. 먼저 네가 스스로와 끝말잇기를 해 10번 이상 이어진다면 통과야.")
        print("끝말잇기를 통과한다면 나와 가위바위보 대결을 하는거야! 네가 가위바위보를 5번 중 3번을 이긴다면 네 승리야!")
        print("이 게임을 모두 이긴다면 이 숲을 나갈 수 있도록 해줄게. 대신 진다면 약속대로 우리와 함께 이 숲에 머물러야해.")
        print()
        print("그럼 끝말잇기를 시작하도록 하자")
        game.endword(self)
        return game.check_rsp(self)

        
    def answer_no(self):
        print("아쉽지만 이 내기에서 이기지 않으면 우리는 널 돕지 않을거야.")
        print("다시 한 번 물어볼게. 내기에 응하겠어?")
        game.question(self)
        
# 끝말잇기        
    def endword(self):
        endword = False
        cnt = 0 # 변수 count 0으로 초기화
        #while endword or cnt == 2: # endword가 True라면 반복
        while cnt <10: # endword가 True라면 반복
            firstword = input("첫 번째 단어 : ") # 첫 단어 입력받음
            print("좋아. 다음 단어는?")
            for i in range(0, 100): # i를 0~100까지 반복
                secondword = input("다음 단어 : ") # 두 번째 단어(다음 단어)를 입력받는다.
                if firstword[-1] == secondword[0]: # 만약 처음 입력 받은 단어의 마지막 글자(뒤에서 첫번째)와
                    print("맞아. 잘 하는데?")                # 다음에 입력받은 글자의 첫 번째 단어가 같다면
                    cnt += 1      # 카운트 + 1
                    firstword = secondword # 두 번째로 입력받은 단어를 firstword(첫 번째) 변수에 저장
                else:
                    print("단어가 이어지지 않잖아. 실패야. 넌 이제 이 숲에서 나갈 수 없어.") # 만약 맨 끝 글자와 첫 글자가 같지 않다면 틀린 단어 출력
                    endword = False
                    break   # 반복문 탈출
                if cnt == 9: # 카운트가 5 이상이 되면 통과 출력
                    print("끝말잇기는 통과야! 마지막으로 2와 가위바위보 대결을 하도록 해.")
                    endword = True
                    break
            break
        if endword is True: # 끝말잇기 변수가 True면(끝말잇기를 통과했다면)
            game.RSP_game(self) # 가위바위보 함수 호출
            
            
        else: # 끝말잇기를 통과하지 못했다면
            game.retry(self) # 재도전 함수 호출
        return endword
          
    def retry(self):
        print("다시 도전할래?")

# 가위바위보 함수                
    def RSP_game(self):
        print("가위바위보")
        rsp_list = ['가위', '바위', '보'] # 가위바위보 리스트
        self.gameStatus = False
        cnt = 0 # 가위바위보 횟수 
        while self.gameStatus is False and cnt < 5:
            fairyHand = random.choice(rsp_list) # 요정이 선택한 것을 랜덤으로 받음
            
            myHand = input("가위바위보 중 선택하자 : ") # 내가 낼 손을 선택
            result = ""
            print(f"""
                 ┌─────────────────────────────────┐
                   나:{myHand} 요정:{fairyHand}
                 └─────────────────────────────────┘  
                   """)
            
            if myHand == "가위": # 내가 가위를 냈을 때
                if fairyHand == "가위": # 컴퓨터가 가위면
                    result = "onemore" # 다시(비김)
                elif fairyHand == "바위": # 컴퓨터가 바위면
                    result = "fail" # 게임 패배
                elif fairyHand == "보": # 컴퓨터가 보 면
                    result = "win" # 승리
            elif myHand == "바위": # 내가 바위를 냈을 때
                if fairyHand  == "가위":
                  result = "win"
                elif fairyHand == "바위":
                  result = "onemore"
                elif fairyHand == "보":
                  result = "fail"
            
            elif myHand == "보": # 내가 보를 냈을 때
                if fairyHand  == "가위":
                  result = "fail"
                elif fairyHand == "바위":
                  result = "win"
                elif fairyHand == "보":
                  result = "onemore"       
            else:
                print("가위, 바위, 보 중에 골라야지!")
            if result == "fail":
                print("내가 이겼어~!")
               # print("내가 이겼어! 앞으로 우리와 함께 즐겁게 놀자~!")
            elif result == "win": # 가위바위보를 이긴다면
                print("너가 이겼어! 약속대로 이 숲을 나갈 수 있게 해줄게.")
                self.gameStatus = True
                break 
                
            elif result == "onemore":
                print("이런, 비겼잖아. 한 번 더 해!")
                
            cnt+=1
        return self.gameStatus
        
    def check_rsp(self):
        return self.gameStatus

                    