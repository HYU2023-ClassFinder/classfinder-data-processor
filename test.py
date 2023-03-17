# import time

# f = open("text.txt", 'w', encoding='UTF-8')
# for i in range(1, 100):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
import os

for i in range(100000):
    print(i)
    os.system('cls')