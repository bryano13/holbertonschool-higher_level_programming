#!/usr/bin/python3
import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nSome more random text")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

os.rename("mydata.txt", "mydata2.txt")
os.chdir("..")
print("Current Directory:", os.getcwd())

#print(myFile.closed)
print(myFile.name)
#print(myFile.mode)
