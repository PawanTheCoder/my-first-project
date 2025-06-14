def win(my_list,last_value,index):
    if my_list[index] == "X" or my_list[index] == "O":
        print("The space is Occupied!")
        return False
    else:
        my_list[index] = last_value
        print("The table : ")
        for i in range(0,9):
             print(my_list[i],'|',end = " ")
             if i == 2 or i == 5:
                 print()

        if ((my_list[0] == my_list[1] == my_list[2]) and my_list[0]!= " ") or\
        (my_list[0] == my_list[3] == my_list[6] and my_list[0] != " ") or \
        (my_list[6] == my_list[7] == my_list[8] and my_list[6] != " ") or\
        (my_list[2] == my_list[5] == my_list[8] and my_list[2] != " ") or\
        (my_list[0] == my_list[4] == my_list[8] and my_list[0] != " ")  or \
        (my_list[3] == my_list[4] == my_list[5] and my_list[5] != " ") or\
        (my_list[2] == my_list[4] == my_list[6] and my_list[2] != " ") or\
         my_list[1] == my_list[4] == my_list[7] and my_list[1] != " ":
            return last_value
        else:
            return "Nothing"
print("Game begins! ->")
print("User1 -> X")
print("User2 -> O")
count = 0
my_list = []

for i in range(0,9):
    my_list.append(i)
for i in range(0,9):
     print(my_list[i],'|',end = " ")
     if i == 2 or i == 5:
         print()
signal = True
while signal != False and count !=9:
    if count % 2 == 0:
        count += 1
        print("For user1:")
        while True:
             index = int(input("Enter index (0 - 8): "))
             if index not in range(0,9):
                 print("Index out of range! try again")
                 continue
             x = win(my_list,"X",index)
             if  x == False :
                 print("Overwriting is not allowed! choose another index:")
        
             elif index not in range(0,9):
                 print("Enter index in range (0 - 8)")
             else:
                 break
        if count == 9:
            print("Tie!!!!!")
            signal = False
            break
             
       
        if x == "Nothing":
            print("Next Turn : ")
        elif x == 'X':
            print("User1 Won !!!!!!!")
            signal = False
    else:
        count += 1
        print("For user2:")
        
        while True:
             index = int(input(("Enter index (0 - 8): ")))
             if index not in range(0,9):
                 print("Index out of range! try again")
                 continue
             y = win(my_list,'O',index)
             if y == False :
                 print("Overwriting is not allowed! choose another index:")
        
             elif index not in range(0,9):
                 print("Enter index in range (0 - 8)")
             else:
                 break
        if y == "Nothing":
            print("Next Turn : ")
        elif y == 'O':
            print("User2 Won !!!!!!!")
            signal = False
        if count == 9:
            print("Tie!!!!!")
            signal = False
            break
