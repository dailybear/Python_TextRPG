""" Text adventure game
    @insta = @lakshaytalkstocomputer
    @year  = 2018
"""
__author__ = "lakshaytalkstocomputer" #author: 패키지 작성자

import items #items이라는 모듈을 호출


class NonPlayableCharacter(): #NonPlayableCharacter라는 틀 생성

    def __init__(self): #__init__를 이용하여 생성자를 만든다.
 
        raise NotImplementedError("Do not create raw Non Playable Character objects.") 
        #NotImplementedError("Do not create raw Non Playable Character objects.") 라는 에러를 일부로 발생시킨다.
 

    def __str__(self):
        return self.name #self.name를 반환한다.



class Trader(NonPlayableCharacter): #Trader를 정의한다.
    def __init__(self): #self 속성에 값을 할당한다.
        self.name = "탑의 상인" #name에 Trader 할당
        self.gold = 100 #gold에 100 할당
        self.description = "힐 아이템 파는 사람"
        self.inventory = [items.SmallHealingPotion(),
                          items.KingHealingPotion(),
                          items.AmazingHealingPotion(),
                          items.HealingPotion()] 
        