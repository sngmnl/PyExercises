import random
import contextlib
print('''
*****************************************************************************************************************************************************************************

 ######                              ######                                      #####                                                  ####                             ### 
 #     #  ####   ####  #    #        #     #   ##   #####  ###### #####         #     #  ####  #  ####   ####   ####  #####   ####     #      #    #  ####   ####  ##### ### 
 #     # #    # #    # #   #         #     #  #  #  #    # #      #    #        #       #    # # #      #      #    # #    # #         #      #    # #    # #    #   #   ### 
 ######  #    # #      ####          ######  #    # #    # #####  #    #         #####  #      #  ####   ####  #    # #    #  ####      ####  ###### #    # #    #   #    #  
 #   #   #    # #      #  #   ###    #       ###### #####  #      #####  ###          # #      #      #      # #    # #####       #         # #    # #    # #    #   #       
 #    #  #    # #    # #   #  ###    #       #    # #      #      #   #  ###    #     # #    # # #    # #    # #    # #   #  #    #    #    # #    # #    # #    #   #   ### 
 #     #  ####   ####  #    #  #     #       #    # #      ###### #    #  #      #####   ####  #  ####   ####   ####  #    #  ####      ####  #    #  ####   ####    #   ### 
                              #                                          #

*****************************************************************************************************************************************************************************                                                                                                                           
''')
with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt
    
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rpc = [rock, paper, scissors]
computer = random.randint(0,2)
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
match = [rpc[player],rpc[computer]]
if player == 0 or player == 1 or player == 2:
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 0):
        print(f"You chose: \n {rpc[player]}")
        print(f"Computer chose: \n {rpc[computer]}")
        print("You win!")
    elif player == computer:
        print(f"You chose: \n {rpc[player]}")
        print(f"Computer chose: \n {rpc[computer]}")
        print("It's a draw")
    else:
        print(f"You chose: \n {rpc[player]}")
        print(f"Computer chose: \n {rpc[computer]}")
        print("You lose...")
else:
    print("You've entered an invalid value")
