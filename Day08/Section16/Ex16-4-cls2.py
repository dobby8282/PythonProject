class HoldemPlayer:
    card3 = ''
    card4 = ''
    card5 = ''
    card6 = ''
    card7 = ''

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def get_card_info(self):
        print('card1 : {}'.format(self.card1))
        print('card2 : {}'.format(self.card2))
        print('card3 : {}'.format(self.card3))
        print('card4 : {}'.format(self.card4))
        print('card5 : {}'.format(self.card5))
        print('card6 : {}'.format(self.card6))
        print('card7 : {}'.format(self.card7))

    @classmethod
    def set_card3(cls, card):
        cls.card3 = card

    @classmethod
    def set_card4(cls, card):
        cls.card4 = card

    @classmethod
    def set_card5(cls, card):
        cls.card5 = card

    @classmethod
    def set_card6(cls, card):
        cls.card6 = card

    @classmethod
    def set_card7(cls, card):
        cls.card7 = card


player1 = HoldemPlayer('SpadeA', 'SpadeK')
player2 = HoldemPlayer('Dia2', 'Dia7')
player3 = HoldemPlayer('Hear10', 'HearJ')

print('1Round Plyaer 1 카드정보 >>>>  ')
player1.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

print('1Round Plyaer 2 카드정보 >>>>  ')
player2.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

print('1Round Plyaer 3 카드정보 >>>>  ')
player3.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')


HoldemPlayer.set_card3('DiaK')


print('2Round Plyaer 1 카드정보 >>>>  ')
player1.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

print('2Round Plyaer 2 카드정보 >>>>  ')
player2.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

print('2Round Plyaer 3 카드정보 >>>>  ')
player3.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')


HoldemPlayer.set_card4('Spade6')

print('3Round Plyaer 1 카드정보 >>>>  ')
player1.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

print('3Round Plyaer 2 카드정보 >>>>  ')
player2.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

print('3Round Plyaer 3 카드정보 >>>>  ')
player3.get_card_info()
print('>>>>>>>>>>><<<<<<<<<<<<')

