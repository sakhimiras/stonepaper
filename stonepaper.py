import random 
num = random.randrange(1,4)

while(True):

    user_str = input("\033[34m{}".format('выберите из списка: \n1)камень \n2)ножницы \n3)бумага \n'))

    if(user_str != "1" or user_str != "2" or user_str != "3" ): 
        print("\033[31m{}".format('\nerror: введите что то из списка:'))
        continue

    user = int(user_str)
    
    if user == 1:
        if(num == 1): print("\033[33m{}".format('ничья:'))
        if(num == 2): print("\033[32m{}".format('ты выиграл'))
        if(num == 3): print("\033[31m{}".format('ты проиграл'))
        
        inp = input("\033[34m{}".format('\nХотите продолжить? y/n \n'))
        if inp == 'n': break
        elif inp == 'y': continue

    if user == 2:
        if(num == 1): print("\033[31m{}".format('ты проиграл'))
        if(num == 2): print("\033[33m{}".format('ничья:'))
        if(num == 3): print("\033[32m{}".format('ты выиграл'))
        inp = input("\033[34m{}".format('\nХотите продолжить? y/n \n'))
        if inp == 'n': break
        elif inp == 'y': continue
    if user == 3:
        if(num == 1): print("\033[32m{}".format('ты выиграл'))
        if(num == 2): print("\033[31m{}".format('ты проиграл'))
        if(num == 3): print("\033[33m{}".format('ничья:'))
        inp = input("\033[34m{}".format('\nХотите продолжить? y/n \n'))
        if inp == 'n': break
        elif inp == 'y': continue

    if(inp != 'y' or'n'):
        print("\033[31m{}".format('\nerror: введите y/n: \n'))
        continue

    
  

