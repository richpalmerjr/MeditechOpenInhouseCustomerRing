############################
#    Read and run MTADs    #
#                          #
#        RPALMER           #
#        07/30/19          #
############################

import os
i = 0
unv = []
ring = []
arr = []

#############################################################################################################################
# function to setup arr with the path it's given
def list_directory(path):
    print (path)
    return os.listdir(path)

# function to ask which choice
# returns choice - 1 for the array
def ask_choice(arg):
    print()
    return int(input('What ' + arg + "? "))-1
#############################################################################################################################


# loop on the directory, add the directory to the array if it's a universe, and print it to the screen
arr = list_directory('C:\Program Files (x86)\MEDITECH')
for dir in arr:
    if '.Universe' in dir:
        i += 1
        unv.append(dir)
        print(i,'.',dir)
        
# ask which one you want to open and display the choice
unvchoice = ask_choice('Universe')
print()
print('Rings in',unv[unvchoice] + ':')

# list the rings in the choice that was made
i = 0
arr = list_directory('C:\Program Files (x86)\MEDITECH\\'+unv[unvchoice])
for dir in arr:
    i += 1
    ring.append(dir)
    print(" ",i,'.',dir)
ringchoice = ask_choice('Ring')

# return the file we want to run next
mtad = ('C:\Program Files (x86)\MEDITECH\\' + unv[unvchoice] + '\\' + ring[ringchoice] + '\\' + 'Client.mtad')
print('Opening ' + unv[unvchoice] + '\\' + ring[ringchoice] + '.')
print('Please wait...')

# open the mtad
os.startfile(mtad, 'open')


