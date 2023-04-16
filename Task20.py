'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
 K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
 Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
 Напишите программу, которая вычисляет стоимость введенного пользователем слова.
 Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12

'''
def Ent_decoder(Eng_letter, word):
    '''
    :param Eng_letter: словарь, ключи словаря - баллы за буквы, значения словаря - буквы
    :param word: слово которое надо разложить и присвоить каждой букве балл
    :return: общая сумма баллов
    '''
    count = 0
    for i in word:
        for j in Eng_letter:
            if i in Eng_letter[j]:
                count += j
    return count

def Rus_decoder(Rus_letter, word):
    '''
    :param Rus_letter: словарь, ключи словаря - баллы за буквы, значения словаря - буквы
    :param word: слово которое надо разложить и присвоить каждой букве балл
    :return: общая сумма баллов
    '''
    count = 0
    for i in word:
        for j in Rus_letter:
            if i in Rus_letter[j]:
                count += j
    return count


Eng_letter = {1: "AEIOULNSTR", 2: "DG", 3: "BCMP", 4:"FHVWY", 5: "K", 8: "JX", 10: "QZ"} # словари со стоимостью букв
Rus_letter = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4:"ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}

word = input().upper() # вводим слово в консоль и сразу переводим его в верхний регистр
if ord(word[0]) >= 65 and ord(word[0]) < 90: # определяю на каком языке было введено слово по первой букве
    print(Ent_decoder(Eng_letter, word))
else:
    print(Rus_decoder(Rus_letter, word))





