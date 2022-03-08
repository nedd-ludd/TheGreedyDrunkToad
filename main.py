import random as r

# returns password string of  pseudorandom selected ASCII 33-26
def generatePass(dlen = 12):
    charList = [chr(r.randint(33,126)) for x in range(dlen)]
    return ''.join(charList)

#loops printing generatePass, recursive or end on user input
def main():
    for i in range(10):        
        print(generatePass())
    if input('enter any key to continue, or q to quit:') != 'q':
        main()
    else:
        print('thanks for using passGenerator')
        
if __name__ == '__main__': main()
