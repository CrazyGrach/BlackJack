import random
while True:
    newCard = 0
    card1 = random.randint(2, 11)
    card2 = random.randint(2, 11)
    isPerebor = False
    DealerPerebor = False
    if (card1 == 10 and card2 == 11) or (card2 == 10 and card1 == 11) or (card1 == 11 and card2 == 11):
        print(f'Ваши карты: {card1} {card2}')
        print('БЛЭКДЖЕК')
        dealerCard1 = random.randint(2, 11)
        dealerCard2 = random.randint(2, 11)
        if dealerCard1 == 10 and dealerCard2 == 11 or dealerCard1 == 11 and dealerCard2 == 10 or dealerCard1 == 11 and dealerCard2 == 11:
            print(f'Карты дилера: {dealerCard1} {dealerCard2}')
            print('БЛЭКДЖЕК')
            isPerebor = True
        else:
            print(f'Карты дилера: {dealerCard1} {dealerCard2}')
            print('Победа!')
    else:
        dealerCard1 = random.randint(2, 11)
        dealerCard2 = random.randint(2, 11)
        cardSum = card1 + card2
        prevCardSum = cardSum
        print(f'Ваши карты: {card1} {card2}')
        print(f'Карты дилера: {dealerCard1} ?')
        print(f'\n\nХватит или еще? (0/1)', end='')
        more = int(input())
        if more == 1:
            while True:
                newCard = random.randint(2, 11)
                cardSum += newCard
                print(f'Ваши новые карты: {prevCardSum} + {newCard}')
                if cardSum > 21:
                    print('ПЕРЕБОР')
                    break
                if cardSum == 21:
                    print('БЛЭКДЖЕК')
                    break
                prevCardSum = cardSum
                print(f'Хватит или еще? (0/1)', end='')
                more = int(input())
                if more == 0:
                    break
        print(f'Сумма карт: {cardSum}')
        if cardSum > 21:
            isPerebor = True
        print(f'\nКарты дилера: {dealerCard1} {dealerCard2}')
        dealerCardSum = dealerCard1 + dealerCard2
        while True:
            if dealerCardSum < 17:
                newdealerCard = random.randint(2, 11)
                print(f'Карты дилера: {dealerCardSum} + {newdealerCard}')
                dealerCardSum += newdealerCard
                if dealerCardSum > 21:
                    print('Перебор')
                    DealerPerebor = True
            else:
                break
    if isPerebor == False:
        if DealerPerebor == True:
            print('Выигрыш')
        else:
            if cardSum > dealerCardSum:
                print('Выигрыш')
            if cardSum < dealerCardSum:
                print('Проигрыш')
            if cardSum == dealerCardSum:
                print('Ничья')
    input('НАЖМИТЕ ENTER ЧТОБЫ ПРОДОЛЖИТЬ')
    for i in range(5):
        print()