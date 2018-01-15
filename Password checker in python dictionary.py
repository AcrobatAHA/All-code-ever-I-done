dict_of_pas = {0 : 4, 1 : 8, 2 : 15, 3 : 16, 4 : 23, 5 : 42}
print("Enter a 6 elements password :: ")
Pw = [int(input()),int(input()),int(input()),int(input()),int(input()),int(input())]
if Pw[0] == dict_of_pas[0] and Pw[1]== dict_of_pas[1] and Pw[2] == dict_of_pas[2] and Pw[3] == dict_of_pas[3] and Pw [4] == dict_of_pas[4] and Pw [5] == dict_of_pas[5]:
    
    print("YOU ARE WELCOME.")

else:
    print("YOU AREN'T ALLOWED.")
