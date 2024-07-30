q = 1


def cp(file_name, file_name_copy): 
    file = open(file_name, "r")
    file_read = file.read()
    file.close()
    dot = file_name.rfind(".")
    name = file_name[0:dot]
    type = file_name[dot:]
    file_name = name + " copy" + type
    file = open(file_name_copy, "w")
    file.write(file_read)
    file.close()


# while q == 1:
#     i = int(input("1)показать содержимое файла с нумерацией \n2) Создать файл и записать в него текст \n3) Добавить текст в файл \n4) скопировать файл\n5) выйти из программы\n"))
    
#     if i == 1:
#         r = input("Какой файл вы хотите посмореть\n")
#         file = open(r, "r")
#         file_read = file.readlines()
#         q = 1
#         for c in file_read:
#             print(str(q)+" "+c, end = "")
#             q = q + 1
#         file.close()

#     if i == 2:
#         r1 = input("Введиет название файла")
#         r2 = input('Введите текст\n')
#         file = open(r1, "w")
#         file.write(r2+"\n")
#         file.close()

#     if i == 3: 
#         r1 = input("Введите название файла\n")
#         r2 = input('Введите текст\n')
#         file = open(r1, "a")
#         file.write(r2+"\n")
#         file.close()

#     if i == 4:
#         r1 = input('Введите название файла который хотите скопировать\n')
#         cp(r1)

#     if i == 5:
#         q=0

# file = open("numbers.txt", "r")
# file_read = file.readlines()
# print(file_read)
# file_read2 = []
# for i in file_read:
#     file_read2.append(int(i))
# file_read2.sort()
# print(file_read2)
# file = open("numbers.txt", "w")
# for i in file_read2:
#     file.write(str(i)+"\n")




def search(file_name, symbol):
    file = open(file_name, "r")
    file_read = file.readlines()
    r = 0
    for i in file_read:
        if symbol in i:
            r = r + 1 
    return r
s = search("main.py", "import")    
print(s)      
























