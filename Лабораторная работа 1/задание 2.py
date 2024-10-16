# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44
stranitsa = 100
stroka = 50
symbol = 25
hranenie = 4

bite = V * 1024 * 1024 # объём дискеты в байтах
symbols_in_book = symbol*stroka*stranitsa # кол-во символов в книге
bait_in_book = symbols_in_book * hranenie # память, требующуяся для хранения одной книги
kol = int(bite // bait_in_book)
print("Количество книг, помещающихся на дискету:", kol)
