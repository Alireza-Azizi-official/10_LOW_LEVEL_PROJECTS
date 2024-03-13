# <<  FLAMES GAME  >>


import time

#make a dictionary to take the key and value at the end of the game to give the result
flames={
    "f":"friend",
    "l":"love",
    "a":"affection",
    "m":"marriage",
    "e":"enemy",
    "s":"sibling"
}

#first part
#take two players name and then remove the same letters of both then count the letters which left.
name_1=(list(input('PLAYER 1 : ENTER YOUR NAME:')))
name_2=(list(input('PLAYER 2 :ENTER YOUR NAME:')))

for i in name_1:
    for j in name_2:
        if i==j:
            if i in name_1:
                name_1.remove(i)
            name_2.remove(j)
            if i in name_1:
                name_2.append(i)
        else:
            name_2.append(i)

# print(len(name_2))

#take flames and use the number which we count as an eliminator.
eliminator=len(name_2)-1  #=2
d=list("flames")
# print(len(d))           #=6

#make a loop to repeat the code till it finishes. 
while len(d)>1:
    #put a timer here  for fun!! it's not important.
    for i in range(2,0,-1):
        print(i)
        time.sleep(i)
    #count the letter which must be removed and then remove it and then show it.
    eliminator=eliminator % len(d)
    eliminated_letter=d.pop(eliminator)
    print('the eliminated letter is :',eliminated_letter)
    #if one letter left at the end then return the letter and check it.
    if len(d)==1:
        print('the remained letter is :',d[0])
        #return the remained letter and check it with the key value in dict then return the result.
        if d[0] in flames:
            print('WOW YOUR RESULT IS : <<',flames[d[0]],'>>')
        
    else:
        # Reset eliminator to a valid index
        eliminator = eliminator % len(d)
        eliminated_letter=d.pop(eliminator)
        print('\n'+'the eliminated letter is :',eliminated_letter)

    for i, letter in enumerate(d):
        if letter== eliminated_letter:
            eliminator=i
            break
