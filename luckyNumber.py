# Rohan enjoys mathematics and has a few favourite numbers. Therefore, 
# Rohan prefers positive integers whose sole lucky digits in the decimal notation are 4 and 7. 
# For instance, lucky numbers are 47, 744, 4, whereas unlucky numbers are 5, 17, 467. 
# If a number can be divided evenly by a lucky number, Rohan considers it to be almost lucky.

# He needs our assistance to determine whether the supplied number N is nearly lucky.

n = int(input("Enter the number: "))
ch = str(n)
luckyNumbers = [4,7]

unlukyNumbers = [5,17,467]

if n in unlukyNumbers:
    print('unlukyNumbers')
else:
    if n in luckyNumbers:
        print('luckyNumbers')
    else:
        for i in ch:
            if int(i) in luckyNumbers:
                flag = True
            else:
                flag = False
                
                break
        if flag == True:
            print('luckyNumbers')
        else:
            if n % 4 == 0 or n % 7 == 0:
                print('NEARLY lUCKY nUMBER')
            else:
                print('not a lucky number145')
            