# Mohammad Mishal S. Noroña | BSCPE 1-5 | PROBLEM 2 – DECRYPTION
# add Color to the program
import colorama
from colorama import Fore, Back, Style
colorama.init()
# add introduction
print("")
print(Fore.LIGHTYELLOW_EX + "WELCOME TO THE PROGRAM".center(40," ") )
print(Fore.LIGHTYELLOW_EX + "By: Mishal Noroña".center(40," ") )
# ask user for input
letter_input = input(Fore.CYAN + "Enter the text you want to decrypt:")
letter_output = ""
# check each character
for x in range(len(letter_input)):
# if *, change to a
    if letter_input[x] == "*":
        letter_output += "a"
# if &, change to e
    elif letter_input[x] == "&":
        letter_output += "e"
# if #, change to i
    elif letter_input[x] == "#":
        letter_output += "i" 
# if +, change to o
# if !, change to u
# add loading time
# add animation
# print output