#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TITA-DO MIT licance.
"""
#import pickle
from time import sleep
from sys import exit
from models.ask_name import ask_name
from models.enigma import Enigma_starter

print("\n\t :)   You Todo with TITA-DO    (:")
print(" TITA-DO      =.|.=     Hyd_Prime version")
print("\n\n")

if ask_name() == False:
    print("\n\n\t***TITA-DO Ver Hyd 1 ***")
    exit()


def write_file(data, name):
    '''write data for TITA.DO'''
    file_tita = open(name, 'a')
    file_tita.writelines(data)
    file_tita.close()
    return data

def load_file():
    '''load data in TITA.DO'''
    file_tita = open('Temp.txt', 'r')
    file_tita.readline()
    file_tita.close()
    return data


#Hi!




data_base = {}
NUMBER_TODO = 1

data = write_file(str(input("==> pleas enter your todo:")), "Temp.txt")
data_base[load_file()] = "==>", NUMBER_TODO
NUMBER_TODO += 1

if load_file() == 'parseh':
    print("\n Hi Admin! \n")

#it's operator case
OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
while OPERATOR_CASE != "1" and OPERATOR_CASE != "2":
    print("Your answer not found in program")
    print("Enter correct answer please")
    sleep(0.25)
    OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
    if OPERATOR_CASE == "1" or OPERATOR_CASE == "2":
        break

#پاسخ بله

while OPERATOR_CASE == "1":
    try:
        print("-> You Todo with TITA-DO! <-")
    except:
        print("Answer Error")
        print("Your answer is not found in program")
        print("Enter correct answer please")
        sleep(0.5)
        print("Your answer not found in program")
        print("Enter correct answer please")

    data = write_file(input(str("==>pleas enter your todo:")), "Temp.txt")
    data_base[load_file()] = "======>", NUMBER_TODO
    NUMBER_TODO += 1
    OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
while OPERATOR_CASE != "1" and OPERATOR_CASE != "2":
    print("Your answer not found in program")
    print("Enter correct answer please")
    sleep(0.5)
    OPERATOR_CASE = str(input("If you want to continue?  1.Yes    2.No = "))
    if OPERATOR_CASE == "1" or OPERATOR_CASE == "2":
        break
    if OPERATOR_CASE == "2":
        break
#پاسخ خیر
if OPERATOR_CASE == "2":
    print("")
    a = write_file(data_base, "tita.do")
    print(a)
    print("  \n Thanks for using this program  ")
    print("             Goodbye             ")
    print("author", "==> TITA-DO <==", "Komeil Parseh")
#تمام شد!
