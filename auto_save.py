# file = open("main.py", "r")
# file_read = file.readlines()
# print(file_read)
# for i in file_read:
#     print(i, end = "")
# file = open('mafhigri.txt', "w")
# file.write("ifnipfnfi\n")
# file.write("hi\n")
# file.close()
# file = open('mafhigri.txt', "a")
# file.write("apple\n")
import json
# file = open("txt.json", "w")
# slovar = {"Danial":+79118363256, "Tima":+79873642356}
# json.dump(slovar, file)
# file.close()
file = open("txt.json", "r")
slovar = json.load(file)
print(slovar)