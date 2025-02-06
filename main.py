"""
READ - rf
WRITE - wf
OPEN - r+

binary
rb
wb
ab

python muutujad camel_case nt: inimese_vanus

"""
import requests
import zipfile
import os

for i in range(10, 200):
    if i == 148:
        continue
    filename = "file%d" % i
    # print(filename)
    f = open("random_files/" + filename, "rb").read(3)

    # print(f)
    if f == b"\xff\xd8\xff":
        print("jpeg found")
        os.rename("random_files/" + filename, "random_files/" + filename + ".jpeg")

    else:
        os.remove("random_files/" + filename)

# f = open("README.md")
# print(f.read())
