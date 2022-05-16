import random

ryunosuke= []
syunki  = []
ryunosuke_point =[]
syunki_point =[]
#10以上はミスです

for i in range(10):
  ryunosuke.append(random.randint(1,20))
  syunki.append(random.randint(1,20))
print("しゅんき",syunki)
print("りゅうのすけ",ryunosuke)

#ここから下に書いてな
syunki_result = 0
ryunosuke_result = 0
for i in range(0,10):
    random_number = random.randint(0,10)
    if random_number in syunki:
        print('しゅんき成功です')
        syunki_result += random_number
        if random_number in syunki_point:
            syunki_result -= random_number
        syunki_point.append(random_number)
    else:
        print('しゅんき失敗です')
    if  random_number in ryunosuke:
        print('りゅうのすけ成功です')
        ryunosuke_result += random_number
        if random_number in ryunosuke_point:
            syunki_result-=random_number
        ryunosuke_point.append(random_number)
    else:
        print('りゅうのすけ失敗です')
print('しゅんきくんの点数は'+str(syunki_result))
print('りゅうのすけの点数は'+str(ryunosuke_result))

if int(syunki_result) > int(ryunosuke_result):
    print('しゅんきの勝ちです')
elif int(ryunosuke_result) > int(syunki_result):
    print('龍之介の勝ちです')
else:
    print('引き分けです')