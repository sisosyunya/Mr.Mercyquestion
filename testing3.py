import random
import numpy as np


# first_player = []
# second_player = []

jubge_first_player_bingo = [i*0 for i in range(9)]
jubge_second_player_bingo = [i*0 for i in range(9)]

first_player = [i for i in range(1,41)]
second_player = [i for i in range(1,41)]


second_player_bingo =[]
for i in range(9):
    first_random = random.randint(1,40)
    second_random_number = random.randint(1,40)
    first_player.append(first_player[i]) 
    second_player.append(second_player[i])
    # first_player.append(first_random_number)
    # second_player.append(second_random_number)
    # first_player = np.arange(first_random_number).reshape
# print(first_player)
# print(second_player)
test =[i*0 for i in range(9)]

# def checking(player):
    # check_lefttop = player[0] == player[1] ==player[2]==0  or  player[0]==player[4]==player[8]==0 or player[0]==player[3]==player[6]==0
    # check_body =player[3]==player[4]==player[5] or player[6]==player[7]==player[8]
    # check_vertical = player[1]==player[4]==player[7]
    # check_righttop = player[2]==player[4]==player[6] or player[2]==player[5]==player[8]
    # if(check_lefttop or check_body or check_vertical or check_righttop):
    #     return print('ビンゴ')
def judgment(player):    
    for z in range(0,1000):
    # while True:
        master_random_number = random.randint(1,40)
        # 数字を開ける処理
        if master_random_number in player:
            for search in range(len(player)):
                if search ==  master_random_number:
                    player[search]=0
                    # print('０にしたよ')
        if len(player)-np.count_nonzero(player) >=3:
            print('調査開始！！')
            # checking(player)
            check_lefttop = player[0] == player[1] ==player[2]==0  or  player[0]==player[4]==player[8]==0 or player[0]==player[3]==player[6]==0
            check_body =player[3]==player[4]==player[5] or player[6]==player[7]==player[8]
            check_vertical = player[1]==player[4]==player[7]
            check_righttop = player[2]==player[4]==player[6] or player[2]==player[5]==player[8]
            if(check_lefttop or check_body or check_vertical or check_righttop):
                print('ビンゴ')
                break
        judgment(first_player)
        judgment(second_player)


print(first_player)
print(second_player)