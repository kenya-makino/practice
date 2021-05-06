# question1
with open("textfile.txt", "r", encoding="utf-8")as f:
    print(f.read())


# question2
x = input("あなたの名前は？:")

with open("name.txt", "+w", encoding="utf-8")as fs:
    fs.write(x)


# question3
import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], 
          ["Titanic", "The Revenant", "Inception"], 
          ["Traning Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline="") as fss:
    w = csv.writer(fss, delimiter=",")
    w.writerow(movies[0])
    w.writerow(movies[1])
    w.writerow(movies[2])


movies2 = [["トップガン", "リスキー・ビジネス", "マイノリティー・レポート"],
           ["タイタニック", "ザ・レヴェナント", "インセプション"],
           ["筋トレの日", "その男、火に入る", "戦士"]]

with open("movies2.csv", "w", encoding="utf-8" ,newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(movies2[0])
    w.writerow(movies2[1])
    w.writerow(movies2[2])
