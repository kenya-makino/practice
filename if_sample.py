x = int(input("数字を入力してね："))

if x < 0:
	x = 0
	print('0より小さかったので0に直しときました。')
elif x == 0:
	print('Zero')
elif x == 1:
	print('One')
else:
	print('More')
