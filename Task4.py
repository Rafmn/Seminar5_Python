# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text_deshif = open('file_deshif.txt', 'w')   # Создание первоначального файла с несжатым текстом
text_deshif.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWDDD')
text_deshif.close()

def text_shif(some_text):   # Сжатие текста
    count = 1
    shif_list = ''
    for i in range(len(some_text)-1):
        if some_text[i+1] == some_text[i]:
            count += 1
        else:
            shif_list = shif_list + str(count) + some_text[i]
            count = 1
    return shif_list + str(count) + some_text[-1]

def text_deshif(some_text):  # Распаковка текста
    deshif_text = ''
    count = ''
    for i in range(len(some_text)):
        if some_text[i].isdigit():
            count += some_text[i]
        else:
            num = int(count)
            line = num * some_text[i]
            deshif_text += line
            count = ''
    return deshif_text

text_deshiff = open('file_deshif.txt', 'r') # Открытие и чтение несжатого текста
text_line = text_deshiff.read()
text_deshiff.close()

text_shiff= open('file_shif.txt', 'w')   # Создание первоначального файла с сжатым текстом
text_shiff.write(text_shif(text_line))    # Сжатие и запись текста в файл
text_shiff.close()

text_shiff = open('file_shif.txt', 'r')   # Открытие и чтение сжатого текста
text_line_1 = text_shiff.read()
text_shiff.close()

text_deshiff = open('file_deshif.txt', 'w')   # Перезапись сжатого текста в файл
text_deshiff.write(text_deshif(text_line_1))
text_deshiff.close()






# print(text_shif('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))
# print(text_deshif('12W1B12W3B24W1B14W5E'))