# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков
#     Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#     Будем считать, что на вход подается только одно слово, которое содержит либо
#     только английские, либо только русские буквы.

#     ноутбук
#     12

one = "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т"
two = "D, G, Д, К, Л, М, П, У"
three = "B, C, M, P, Б, Г, Ё, Ь, Я"
four = "F, H, V, W, Y, Ж, З, Х, Ц, Ч"
five = "K, Ж, З, Х, Ц, Ч"
eight = "J, X, Ш, Э, Ю"
ten = "Q, Z, Ф, Щ, Ъ"

one = one.split(", ")
two = two.split(", ")
three = three.split(", ")
four = four.split(", ")
five = five.split(", ")
eight = eight.split(", ")
ten = ten.split(", ")

dic_of_lists = {1:one, 2:two, 3:three, 4:four, 5:five, 8:eight, 10:ten}

full_dic = {}

for key,value in dic_of_lists.items():
    for i in value:
        full_dic[i] = key

word = input("Please enter your word to score: ").upper()

ans = 0

for i in word:
    ans += full_dic[i]
    
print(ans)