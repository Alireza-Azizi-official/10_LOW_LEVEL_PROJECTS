import logic
if __name__ == '__main__':
     matrix= logic.start()

     while True:
         a=input("Enter a key:")

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

         else:
             print("You can only play with these keys: (a,d,s,w)")

print(matrix) 