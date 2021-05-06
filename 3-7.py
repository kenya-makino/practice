# question1
movies = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for movie in movies:
    print(movie)


# question2
#for num in range(25, 51):
for num in range(25, 31):
    print(num)


# question3
i = 0

while i <= len(movies) - 1:
    movie = str(i) + ":" + movies[i]
    print(movie)
    i += 1


# queston4
answer = [1919, 4545, 721]

print("数字当てゲーム！数字を入力しろ！！")
print("qで終了するよ。")

while True:
    try:
        number = input()
        if number == 'q':
            print("終了します。")
            break
        elif int(number) in answer:
            print("正解！")
            break
        elif int(number) not in answer:
            print("不正解...")
    except ValueError:
        print("数字を入力するか、qで終了します。")


# question5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
added = []

for i in list1:
    for j in list2:
        added.append(i * j)

print(added)


