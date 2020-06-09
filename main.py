from cards import Card, Player

field = []


def field_refresh(playas, n, m, field):
    field = []
    for i in range(n):
        field.append([0] * m)
    for i in players.keys():
        player = playas.get(i)
        for j in player.card.values():
            field[j.y][j.x] = j.name
    for k in field:
        print(k)


def is_cell_empty(x, y, field, players, cardname):
    if field[y][x] == 0:
        return True
    else:
        if players.get(name_player).card.get(field[x][y]).x == x and players.get(name_player).card.get(field[x][y]).y == y:
            print('You cannot stay here, your ally\u0027 already placed this cell')
        else:
            players.get(name_player).card.get(cardname).give_damage(field[x][y])
        return False


def side(inputer, coord):
    if coord == 'x':
        if inputer == 'forward':
            return -1
        if inputer == 'back':
            return 1
        if inputer == 'left' or 'right':
            return 0
    else:
        if inputer == 'forward' or 'back':
            return 0
        if inputer == 'left':
            return -1
        if inputer == 'right':
            return 1


def movement(field, n, m, cardname, action, players):
    used_card = players[name_player].card[cardname]
    true = is_cell_empty(used_card.x+side(action, 'x'), used_card.y+side(action, 'y'), field, players, cardname)
    if true:
        used_card.move(side(action, 'x'), side(action, 'y'))
    else:
        used_card.wait
    field_refresh(players, n, m, field)


card1 = Card("spearman1", 10, [0.1, 0.1, 0.1, 0.1], [1, 1, 1, 1], [1, 1, 1], 2)
card2 = Card("swordsman", 15, [0.3, 0.3, 0.3, 0.3], [2, 2, 2, 2], [0.8, 0.8, 0.8], 3)
card3 = Card("cavalryman", 20, [0.5, 0.5, 0.5, 0.5], [5, 2, 3, 1], [0.6, 0.6, 0.6], 3)
player1 = Player("User", {'spearman': card1, 'swordsman': card2, 'cavalryman': card3})

j = 0

for i in player1.card.values():
    i.setCoord(5, j)
    j += 1
card4 = Card("spearman", 10, [0.1, 0.1, 0.1, 0.1], [1, 1, 1, 1], [1, 1, 1], 2)
card5 = Card("swordsman", 15, [0.3, 0.3, 0.3, 0.3], [2, 2, 2, 2], [0.8, 0.8, 0.8], 3)
card6 = Card("cavalryman", 20, [0.5, 0.5, 0.5, 0.5], [5, 2, 3, 1], [0.6, 0.6, 0.6], 3)
player2 = Player("Enemy", {'spearman': card4, 'swordsman': card5, 'cavalryman': card6})

j = 0
name_player = input('Write down your nick')

for i in player2.card.values():
    i.setCoord(0, j)
    j += 1
players = {"enemy": player2, name_player: player1}


a = True
field_refresh(players, 6, 6, field)


def debugging(deb_mes):
    if deb_mes == 'get_health':
        for i in player1.card:
            print(i.health)
        for i in player2.card:
            print(i.health)



while a:
    player_choose = input('Choose the side')
    unit_choose = input(f'Choose your unit: {player1.card.keys()}')
    action_choose = input('Choose the direction: forward, back, left, right')
    movement(field, 6, 6, unit_choose, action_choose, players)