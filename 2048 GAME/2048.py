#import the module from the same file 
#named logic
import logic

#run the game 
if __name__ == '__main__':
     matrix= logic.start()
     
#make a loop to run the game until the player wins or fails
     while True:
         #take an entery(direction) from player
         a=input("Enter a key:")
         
        #what to do if the plater enter one of the (a,s,d,w) keys
         if a.lower() == 'w':
             matrix, changed = logic.to_up(matrix)
             game_status= logic.position(matrix)
             print(game_status)

             if game_status == "GAME IS NOT OVER YET.":
                 if changed:
                     logic.add_random_4(matrix)
             else:
                 break

         elif a.lower() == 's':
             matrix, changed = logic.to_down(matrix)
             game_status= logic.position(matrix)
             print(game_status)

             if game_status == "GAME IS NOT OVER YET.":
                 if changed:
                     logic.add_random_4(matrix)
             else:
                 break

         elif a.lower() == 'a':
             matrix, changed = logic.to_left(matrix)
             game_status= logic.position(matrix)
             print(game_status)

             if game_status == "GAME IS NOT OVER YET.":
                 if changed:
                     logic.add_random_4(matrix)
             else:
                 break

         elif a.lower() == 'd':
             matrix, changed = logic.to_right(matrix)
             game_status= logic.position(matrix)
             print(game_status)

             if game_status == "GAME IS NOT OVER YET.":
                 if changed:
                     logic.add_random_4(matrix)
             else:
                 break
        #return the message below if the player enters any other keys than the one which are mentioned
         else:
             print("You can only play with these keys: (a,d,s,w)")
#show the matrix after each change
print(matrix) 