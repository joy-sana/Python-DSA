def convertToBinary(n):
    i = None
    binary = ''
    while (n > 0):
        
        i = n%2
        n = n//2
        binary = str(i) + binary
    print(binary)

for i in range(20):
    convertToBinary(i)