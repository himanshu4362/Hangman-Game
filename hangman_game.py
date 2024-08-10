# this is the code of hangman game ,

print("...........................DISCLAIMER......................... ")
print("This is HANGMAN GAME .\n if you can not win you will hang and you will die.\nThis is very dangerous so be VERY CAREFUL.\n....................BEST OF LUCK ............. \n .....LETS BEGIN.")
print("You can know the word by entering the ! sign.")


list_of_word = ["apple","ball","cat","cow","camel","cobra","cobalt","nikil","rust","rush","random","pitch","guage","graphite","gun","powder","lemon","lichi","leaopard","ocean","ostrich","ugly","umbrella","star","parrot","plug","pillow","shield","summer","winter","rainy","leaves","trees","steam","root","rapidly"]
import random as rd
random_word = rd.choice(list_of_word)

random_word_in_list_form = []
for i in random_word:
    random_word_in_list_form.append(i)

copy_of_random_word_in_list_form = random_word_in_list_form.copy()

list_used_in_game_logic = []
for i in range(len(copy_of_random_word_in_list_form)):
    if copy_of_random_word_in_list_form[i] == "a" or copy_of_random_word_in_list_form[i] == "o" or copy_of_random_word_in_list_form[i] == "e" or copy_of_random_word_in_list_form[i] == " i" or copy_of_random_word_in_list_form[i] == "u":
        list_used_in_game_logic += copy_of_random_word_in_list_form[i]
    else:
        list_used_in_game_logic.append("_")

for s in list_used_in_game_logic :
    print(s,end=" ")

attempts_left = 5
while attempts_left > 0 :
    if list_used_in_game_logic == copy_of_random_word_in_list_form :
        print("     You won the HANGMAN GAME.")
        print("You Won")
        print("     congratulation ,You won the game.")
        break
    for i in range(len(list_used_in_game_logic)):
        if list_used_in_game_logic[i] == "_":
            user_input_charector = input("\nEnter a cherector :")
            if user_input_charector == "!":
                print("The Word was : ",random_word)
                attempts_left = 0
                break
            if copy_of_random_word_in_list_form[i] == user_input_charector:
                list_used_in_game_logic[i] = user_input_charector
                print("Your left attempt is :",attempts_left)
                for l in list_used_in_game_logic:
                    print(l,end=" ")
            else:
                for o in list_used_in_game_logic:
                    print(o,end=" ")
                print("You enterd a wrong letter.")
                attempts_left -= 1
                print("Your left attempt is :",attempts_left)
                break
        else:
            continue
          
    if attempts_left <= 0 :
        print("SO SAD \n       YOU LOSE THE HANGMAN GAME \n YOU ARE HAGED AND DIE. \n You can try again. ")