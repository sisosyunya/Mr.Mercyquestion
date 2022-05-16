import random

first_player = []
second_player = []

first_player_bingo =[]
second_player_bingo =[]
for i in range(9):
    first_random_number = random.randint(1,40)
    second_random_number = random.randint(1,40)
    first_player.append(first_random_number)
    second_player.append(second_random_number)
print(first_player)
print(second_player)

bingo = [0,0,0]


for z in range(0,30):
    master_random_number = random.randint(1,40)
    # 数字を開ける処理
    if master_random_number in first_player:
        for search in range(len(first_player)):
            print(first_player[search])
            if search ==  master_random_number:
                first_player[search]=0
                print('０にしたよ')
                
    # 数字を開ける処理
    if master_random_number in second_player:
        for search in range(len(second_player)):
            print(second_player[search])
            if search ==  master_random_number:
                second_player[search]=0
                print('０にしたよ')
print(first_player)
print(second_player)