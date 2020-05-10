suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod
from enum import IntEnum




class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    @property
    def rank(self):
        return self.card[0]

    @property
    def suit(self):
        return self.card[1]
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()

class PKCard(Card):
    """Card for Poker game
    """
    VALUES = dict(zip(ranks, range(2, 2+len(ranks))))
    def value(self):
        #for 문        
        if(self.card[0] == '2'):
            return 2
        elif(self.card[0] == '3'):
            return 3
        elif(self.card[0] == '4'):
            return 4
        elif(self.card[0] == '5'):
            return 5
        elif(self.card[0] == '6'):
            return 6
        elif(self.card[0] == '7'):
            return 7
        elif(self.card[0] == '8'):
            return 8
        elif(self.card[0] == '9'):
            return 9
        elif(self.card[0] == 'T'):
            return 10
        elif(self.card[0] == 'J'):
            return 11
        elif(self.card[0] == 'Q'):
            return 12
        elif(self.card[0] == 'K'):
            return 13
        elif(self.card[0] == 'A'):
            return 14
        
    def __getitem__(self, index):
        return self.card[index]

if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')

    # comparison
    print(c1 > c2 == c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)


import random
class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(cls(rank + suit))
        
                
    def shuffle(self):
        random.shuffle(self.deck)
    
    def pop(self):
        return self.deck.pop()
    
    def __getitem__(self, index):
        return self.deck[index]
    
    def __str__(self):
        return str(self.deck[:])
    
    def __len__(self):
        return len(self.deck)
    
class Ranking(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class Hands:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards)
        
    def is_flush(self):#flush조건에 맞으면 ?flush 리턴 아니면 false
        count = 0
        kind_of_suit = self.cards[0][1]
        
        list_num=[]
        for i in range(5):
            list_num.append(self.cards[i][0])
            list_num.sort(reverse = True)
        
        for card in self.cards:
            if kind_of_suit == card[1]:
                count += 1
                
        if count == 5:
            return True #list_num[0]+' flush'  
        else:
            return False

    def is_straight(self):#straight면 ?straight 리턴 아니면 false
        
        cur_list = []
        for i in range(5):
            cur_list.append(self.cards[i][0])
        for i in range(5):
            if cur_list[i]=='A':
                cur_list[i] = '14'
            elif cur_list[i]=='K':
                cur_list[i] = '13'
            elif cur_list[i]=='Q':
                cur_list[i] = '12'
            elif cur_list[i]=='J':
                cur_list[i] = '11'
            elif cur_list[i]=='T':
                cur_list[i] = '10'
        cur_list = [int (i) for i in cur_list]
        if (cur_list[0]+1==cur_list[1] and 
            cur_list[1]+1==cur_list[2] and 
            cur_list[2]+1==cur_list[3] and 
            cur_list[3]+1==cur_list[4]):
            return True #str(cur_list[4])+' straight'
        else:
            return False

    def straightflush(self): #straightflush면 ?straightflush 리턴
        cur_list = []        #아니면 false
        for i in range(5):
            cur_list.append(self.cards[i][0])
        for i in range(5):
            if cur_list[i]=='A':
                cur_list[i] = '14'
            elif cur_list[i]=='K':
                cur_list[i] = '13'
            elif cur_list[i]=='Q':
                cur_list[i] = '12'
            elif cur_list[i]=='J':
                cur_list[i] = '11'
            elif cur_list[i]=='T':
                cur_list[i] = '10'
        cur_list = [int (i) for i in cur_list]
        if Hands.is_flush(self) and Hands.is_straight(self):
            return True #str(cur_list[4])+' straightflush'
        else:
            return False
        
    def find_a_kind(self): #스트레이트 플러쉬를 제외한 족보
        sslist=[]          #찾는 함수 ex) 4 four of kinds
        valList=[]
        num = []
        for card in range(5):
            valList.append(self.cards[card][0])
        for i in range(0, 5):
            if valList[i] == 'A':
                valList[i] = 14
            elif valList[i] == 'K':
                valList[i] = 13
            elif valList[i] == 'Q':
                valList[i] = 12
            elif valList[i] == 'J':
                valList[i] = 11
            elif valList[i] == 'T':
                valList[i] = 10
        valList = [int (i) for i in valList]
        
        for i in range(1, 15):
            a = valList.count(i)
            sslist.append(a)
        sslist.reverse()
        #[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0]
    #14 high card
        #return sslist
        for i in range(len(sslist)):
            if sslist[i] == 1:
                del sslist[i]
                for j in range(len(sslist)):
                    if sslist[j] == 1:
                        del sslist[j]
                        for x in range(len(sslist)):
                            if sslist[x] == 1:
                                del sslist[x]
                                for z in range(len(sslist)):
                                    if sslist[z] == 1:
                                        num.append(14-i)
                                        return Ranking.HIGH_CARD #str(num[0])+' High card'
                                    #11111
                                    elif sslist[z] == 2:
                                        num.append(11-z)
                                        return Ranking.ONE_PAIR#str(num[0])+' One pair'
                                    #11112
                            elif sslist[x] == 2:
                                num.append(12-x)
                                return Ranking.ONE_PAIR#str(num[0])+' One pair'
                            #1121
                            elif sslist[x] == 3:
                                num.append(12-x)
                                return Ranking.THREE_OF_A_KIND #str(num[0])+' Three of a kind'
                    
                            #113
                    elif sslist[j] == 2:
                        del sslist[j]
                        for x in range(len(sslist)):
                            if sslist[x] == 1:
                                num.append(14-j)
                                return Ranking.ONE_PAIR #str(num[0])+' One pair'
                            #1211
                            elif sslist[x] == 2:
                                num.append(14-j)
                                return Ranking.TWO_PAIRS #str(num[0])+' Two pair'
                            #122
                    elif sslist[j] == 3:
                        num.append(13-j)
                        return Ranking.THREE_OF_A_KIND #str(num[0])+' Three of a kind'
                    #131
                    elif sslist[j] == 4:
                        num.append(14-j)
                        return Ranking.FOUR_OF_A_KIND #str(num[0])+' Four of a kind'
                    #14
             
            elif sslist[i] == 4:
                num.append(14-i)
                return Ranking.FOUR_OF_A_KIND #str(num[0])+' Four of a kinds'
            #41
            #[0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
            elif sslist[i] == 2:
                del sslist[i]
                for j in range(len(sslist)):
                    if sslist[j] == 1:
                        del sslist[j]
                        for x in range(len(sslist)):
                            if sslist[x] == 1:
                                num.append(14-i)
                                return Ranking.ONE_PAIR #str(num[0])+' One pair'
                            #2111
                            elif sslist[x] == 2:
                                num.append(14-i)
                                return Ranking.TWO_PAIRS #str(num[0])+' Two pair'
                            #212
                    elif sslist[j] == 2:
                        num.append(14-i)
                        return Ranking.TWO_PAIRS #str(num[0])+' Two pair'
                    #221
                    elif sslist[j] == 3:
                        num.append(14-j)
                        return Ranking.FULL_HOUSE #str(num[0])+' Full house'
                    #23
            
            elif sslist[i] == 3:
                del sslist[i]
                for j in range(len(sslist)):
                    if sslist[j] == 1:
                        num.append(14-i)
                        return Ranking.THREE_OF_A_KIND #str(num[0])+' Three of a kind'
                    #311
                    elif sslist[j] == 2:
                        num.append(14-i)
                        return Ranking.FULL_HOUSE #str(num[0])+' Full house'
                    #32
    def tell_hand_ranking(self): #족보를 취합해 알려주는 함수
        rank_a = Hands.straightflush(self)
        rank_b = Hands.is_flush(self)
        rank_c = Hands.is_straight(self)
        rank_d = Hands.find_a_kind(self)
        if rank_a != False:
            return Ranking.STRAIGHT_FLUSH
        elif rank_b != False:
            return Ranking.FLUSH
        elif rank_c != False:
            return Ranking.STRAIGHT
        else:
            return rank_d
        
        
        
        
        
    def compare_user(self, other):#두 유저의 족보를보여주고
        a = Hands.numd(self)      #승자를 가리는 코드
        b = Hands.numd(other)     #tie-break 추가
        c = Hands.tell_hand_ranking(self)
        d = Hands.tell_hand_ranking(other)
        e = Hands.tie_break_compare(self, other)
        print(c, d)
        if a>b:
            return 'player1 win'
        elif a<b:
            return 'player2 win'
        elif a==b:
            return e
        
    def numd(self):#족보의 랭크를 숫자로 매김
        
        rank_a = Hands.straightflush(self)
        rank_b = Hands.is_flush(self)
        rank_c = Hands.is_straight(self)
        rank_d = Hands.find_a_kind(self)
        for i in range(2,15):
            if rank_a == True: #str(i)+' straightflush':
                return int(i+160)
            elif rank_b == True: #str(i)+' flush':
                return int(i+100)
            elif rank_c == True: #str(i)+' straight':
                return int(i+80)
            elif rank_d == Ranking.FOUR_OF_A_KIND: #str(i)+' Four of a kind':
                return int(i+140)
            elif rank_d == Ranking.FULL_HOUSE: #str(i)+' Full house':
                return int(i+120)
            elif rank_d == Ranking.THREE_OF_A_KIND: #str(i)+' Three of a kind':
                return int(i+60)
            elif rank_d == Ranking.TWO_PAIRS: #str(i)+' Two pair':
                return int(i+40)
            elif rank_d == Ranking.ONE_PAIR:#str(i)+' One pair':
                return int(i+20)
            elif rank_d == Ranking.HIGH_CARD: #str(i)+' High card':
                return int(i)
            
    def tie_break(self):#리스트를 만들어 만약 2D 2H 3S 4S 5H면
        sslist=[]       #one pair인패를 제외하고 리스트에 
        valList=[]      #[3,4,5]를 추가하여 리턴
        num = []
        for card in range(5):
            valList.append(self.cards[card][0])
        for i in range(0, 5):
            if valList[i] == 'A':
                valList[i] = 14
            elif valList[i] == 'K':
                valList[i] = 13
            elif valList[i] == 'Q':
                valList[i] = 12
            elif valList[i] == 'J':
                valList[i] = 11
            elif valList[i] == 'T':
                valList[i] = 10
        valList = [int (i) for i in valList]
        
        for i in range(1, 15):
            a = valList.count(i)
            sslist.append(a)
        
        list_a = []
       
        for i in range(len(sslist)):
            if sslist[i]==1:
                sslist[i]=0
                list_a.append(i)
                for j in range(len(sslist)):
                    if sslist[j]==1:
                        sslist[j]=0
                        list_a.append(j)
                        for x in range(len(sslist)):
                            if sslist[x]==1:
                                sslist[x]=0
                                list_a.append(x)
                                for y in range(len(sslist)):
                                    if sslist[y]==2:
                                        return list_a
                            elif sslist[x]==2:
                                sslist[x]=0
                                for y in range(len(sslist)):
                                    if sslist[y]==1:
                                        list_a.append(y)
                                        return list_a
                            elif sslist[x]==3:
                                return list_a
                    elif sslist[j]==2:
                        sslist[j] = 0
                        for x in range(len(sslist)):
                            if sslist[x]==1:
                                sslist[x] = 0
                                list_a.append(x)
                                for y in range(len(sslist)):
                                    if sslist[y]==1:
                                        list_a.append(y)
                                        return list_a
                            elif sslist[x]==2:
                                return list_a
                    elif sslist[j]==3:
                        sslist[j] = 0
                        for x in range(len(sslist)):
                            if sslist[x]==1:
                                list_a.append(x)
                                return list_a
                    elif sslist[j]==4:
                        return list_a
            elif sslist[i]==2:
                sslist[i] = 0
                for j in range(len(sslist)):
                    if sslist[j]==1:
                        sslist[j] = 0
                        list_a.append(j)
                        for x in range(len(sslist)):
                            if sslist[x]==1:
                                sslist[x] = 0
                                list_a.append(x)
                                for y in range(len(sslist)):
                                    if sslist[y]==1:
                                        list_a.append(y)
                                        return list_a
                            elif sslist[x]==2:
                                return list_a
                    elif sslist[j]==2:
                        sslist[j] = 0
                        for x in range(len(sslist)):
                            if sslist[x]==1:
                                list_a.append(x)
                                return list_a
                    elif sslist[j]==3:
                        list_a.append(i)
                        return list_a
            elif sslist[i]==3:
                sslist[i] = 0
                for j in range(len(sslist)):
                    if sslist[j]==1:
                        sslist[j] = 0
                        list_a.append(j)
                        for x in range(len(sslist)):
                            if sslist[x]==1:
                                list_a.append(x)
                                return list_a
                    elif sslist[j]==2:
                        list_a.append(j)
                        return list_a
            elif sslist[i]==4:
                sslist[i] = 0
                for j in range(len(sslist)):
                    if sslist[j]==1:
                        list_a.append(j)
                        return list_a
    def tie_break_compare(self, other):#tie-break를 받아서
        a = Hands.tie_break(self)      #앞서받은 리스트를 역순으로
        b = Hands.tie_break(other)     #하여 비교하여 승자 결정
        if a == None:
            return 'No tie-break'
        if b == None:
            return 'No tie-break'
        if a != None:
            a.sort(reverse = True)
        if b != None:
            b.sort(reverse = True)
       
        if a[0]>b[0]:
            return 'tie-break 1player win'
        elif a[0]<b[0]:
            return 'tie-break 2player win'
        elif a[0]==b[0]:
            if a[1]>b[1]:
                return 'tie-break 1player win'
            elif a[1]<b[1]:
                return 'tie-break 2player win'
            elif a[1]==b[1]:
                if a[2]>b[2]:
                    return 'tie-break 1player win'
                elif a[2]<b[2]:
                    return 'tie-break 2player win'
        
    
if __name__ == '__main__':
    import sys
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

    # your test cases here
    
deck = Deck(PKCard)
deck.shuffle()
my_hand = [PKCard('2D'),PKCard('2D'),PKCard('4D'),PKCard('6H'),PKCard('7D')]
your_hand = [PKCard('2S'),PKCard('2H'),PKCard('8C'),PKCard('7S'),PKCard('6S')]
#a = Hands(deck[:5])  <ㅡㅡㅡㅡㅡ 이용하면 랜덤출력 가능합니다
#b = Hands(deck[-5:]) <ㅡㅡㅡㅡㅡ 이용하면 랜덤출력 가능합니다
c = Hands(my_hand)
d = Hands(your_hand)
# print(c.tell_hand_ranking())
# print(d.tell_hand_ranking())
# print(c.numd())
# print(d.numd())
# print(c.tie_break())
# print(d.tie_break())
# print(c.tie_break_compare(d))
# print(c.compare_user(d))

a1=Hands([PKCard('3S'),PKCard('4S'),PKCard('5S'),PKCard('6S'),PKCard('7S')])
b1=Hands([PKCard('3D'),PKCard('4H'),PKCard('KD'),PKCard('6C'),PKCard('7D')])
# a1 = Hands(a1)
# b1 = Hands(b1)
# a2=[PKCard('3S'),PKCard('3H'),PKCard('3C'),PKCard('3D'),PKCard('7S')]
# b2=[PKCard('7H'),PKCard('7D'),PKCard('3D'),PKCard('TS'),PKCard('KS')]
# a2 = Hands(a2)
# b2= Hands(b2)
# a3=[PKCard('3S'),PKCard('5S'),PKCard('8S'),PKCard('KS'),PKCard('6S')]
# b3=[PKCard('QS'),PKCard('7C'),PKCard('KS'),PKCard('5H'),PKCard('8H')]
# a3 = Hands(a3)
# b3 = Hands(b3)
# a4=[PKCard('3S'),PKCard('2H'),PKCard('4C'),PKCard('6D'),PKCard('5S')]
# b4=[PKCard('3H'),PKCard('QH'),PKCard('6S'),PKCard('7D'),PKCard('2S')]
# a4 = Hands(a4)
# b4 = Hands(b4)
# a5=[PKCard('3S'),PKCard('3H'),PKCard('3C'),PKCard('2D'),PKCard('2S')]
# b5=[PKCard('4S'),PKCard('6H'),PKCard('QC'),PKCard('2D'),PKCard('JS')]
# a5 = Hands(a5)
# b5 = Hands(b5)
# a6=[PKCard('2S'),PKCard('2H'),PKCard('3C'),PKCard('3D'),PKCard('7S')]
# b6=[PKCard('4H'),PKCard('7H'),PKCard('2C'),PKCard('3H'),PKCard('KC')]
# a6 = Hands(a6)
# b6 = Hands(b6)
# a7=[PKCard('3S'),PKCard('3H'),PKCard('6C'),PKCard('8C'),PKCard('TC')]
# b7=[PKCard('4S'),PKCard('4H'),PKCard('3C'),PKCard('2D'),PKCard('7S')]
# a7 = Hands(a7)
# b7 = Hands(b7)
# a8=[PKCard('3S'),PKCard('5H'),PKCard('2C'),PKCard('KD'),PKCard('AS')]
# b8=[PKCard('4S'),PKCard('2H'),PKCard('5C'),PKCard('QD'),PKCard('TS')]
# a8 = Hands(a8)
# b8 = Hands(b8)
# a9=[PKCard('3S'),PKCard('3H'),PKCard('7C'),PKCard('6D'),PKCard('KS')]
# b9=[PKCard('3D'),PKCard('3C'),PKCard('6C'),PKCard('2D'),PKCard('7S')]
# a9 = Hands(a9)
# b9 = Hands(b9)
# a10=[PKCard('2D'),PKCard('2D'),PKCard('4D'),PKCard('6H'),PKCard('7D')]
# b10=[PKCard('2S'),PKCard('2H'),PKCard('8C'),PKCard('7S'),PKCard('6S')]
# a10 = Hands(a10)
# b10 = Hands(b10)
# a11=[PKCard('JC'),PKCard('JS'),PKCard('3S'),PKCard('3D'),PKCard('JH')]
# b11=[PKCard('JD'),PKCard('2C'),PKCard('JH'),PKCard('7C'),PKCard('7S')]
# a11 = Hands(a11)
# b11 = Hands(b11)
# a12=[PKCard('JC'),PKCard('6S'),PKCard('KS'),PKCard('3S'),PKCard('JH')]
# b12=[PKCard('2D'),PKCard('6D'),PKCard('3D'),PKCard('2S'),PKCard('7S')]
# a12 = Hands(a12)
# b12 = Hands(b12)
# a13=[PKCard('JC'),PKCard('6S'),PKCard('6H'),PKCard('5S'),PKCard('JH')]
# b13=[PKCard('4D'),PKCard('JS'),PKCard('JD'),PKCard('6C'),PKCard('6S')]
# a13 = Hands(a13)
# b13 = Hands(b13)
# a14=[PKCard('8C'),PKCard('9S'),PKCard('TS'),PKCard('JS'),PKCard('QS')]
# b14=[PKCard('AD'),PKCard('7S'),PKCard('JH'),PKCard('JC'),PKCard('7S')]
# a14 = Hands(a14)
# b14 = Hands(b14)
# a15=[PKCard('AD'),PKCard('KD'),PKCard('JD'),PKCard('3D'),PKCard('7D')]
# b15=[PKCard('5C'),PKCard('TS'),PKCard('QS'),PKCard('KS'),PKCard('JH')]
# a15 = Hands(a15)
# b15 = Hands(b15)
# a16=[PKCard('4D'),PKCard('6D'),PKCard('5D'),PKCard('8D'),PKCard('7D')]
# b16=[PKCard('9D'),PKCard('9H'),PKCard('8S'),PKCard('5D'),PKCard('9C')]
# a16 = Hands(a16)
# b16 = Hands(b16)
# a17=[PKCard('4D'),PKCard('6D'),PKCard('5D'),PKCard('9D'),PKCard('8D')]
# b17=[PKCard('2S'),PKCard('3S'),PKCard('4S'),PKCard('6S'),PKCard('7S')]
# a17 = Hands(a17)
# b17 = Hands(b17)
# a18=[PKCard('JD'),PKCard('AD'),PKCard('KD'),PKCard('QD'),PKCard('TD')]
# b18=[PKCard('6D'),PKCard('2S'),PKCard('4H'),PKCard('5C'),PKCard('3S')]
# a18 = Hands(a18)
# b18 = Hands(b18)
# a19=[PKCard('JC'),PKCard('6S'),PKCard('KS'),PKCard('3S'),PKCard('JH')]
# b19=[PKCard('AD'),PKCard('KH'),PKCard('JD'),PKCard('JS'),PKCard('7S')]
# a19 = Hands(a19)
# b19 = Hands(b19)
# a20=[PKCard('JC'),PKCard('6S'),PKCard('KC'),PKCard('3S'),PKCard('JH')]
# b20=[PKCard('KD'),PKCard('KS'),PKCard('JS'),PKCard('JD'),PKCard('7S')]
# a20 = Hands(a20)
# b20 = Hands(b20)
print(a1.compare_user(b1))
print()
# print(a2.compare_user(b2))
# print()
# print(a3.compare_user(b3))
# print()
# print(a4.compare_user(b4))
# print()
# print(a5.compare_user(b5))
# print()
# print(a6.compare_user(b6))
# print()
# print(a7.compare_user(b7))
# print()
# print(a8.compare_user(b8))
# print()
# print(a9.compare_user(b9))
# print()
# print(a10.compare_user(b10))
# print()
# print(a11.compare_user(b11))
# print()
# print(a12.compare_user(b12))
# print()
# print(a13.compare_user(b13))
# print()
# print(a14.compare_user(b14))
# print()
# print(a15.compare_user(b15))
# print()
# print(a16.compare_user(b16))
# print()
# print(a17.compare_user(b17))
# print()
# print(a18.compare_user(b18))
# print()
# print(a19.compare_user(b19))
# print()
# print(a20.compare_user(b20))
