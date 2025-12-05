print(r"""
************************************************************
                            _.--.
                        _.-'_:-'|| 
                    _.-'_.-::::'|| 
               _.-:'_.-::::::'  || 
             .'`-.-:::::::'     || 
            /.'`;|:::::::'      ||_ 
           ||   ||::::::'     _.;._'-._ 
           ||   ||:::::'  _.-!oo @.!-._'-. 
           \'.  ||:::::.-!()oo @!()@.-'_.| 
            '.'-;|:.-'.&$@.& ()$%-'o.'\U|| 
              `>'-.!@%()@'@_%-'_.-o _.|'|| 
               ||-._'-.@.-'_.-' _.-o  |'|| 
               ||=[ '-._.-\U/.-'    o |'|| 
               || '-.]=|| |'|      o  |'|| 
               ||      || |'|        _| '; 
               ||      || |'|    _.-'_.-' 
               |'-._   || |'|_.-'_.-' 
            jgs '-._'-.|| |' `_.-' 
                    '-.||_/.-' 
************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?
""")

cross_road = input('    Type "left" or "right"\n')

if cross_road.lower() == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake.\n   Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if lake.lower() == "wait":
        doors = input("You arrive at the island unharmed. There is a house with 3 doors.\n  One red, one yellow and one blue. Which colour do you choose?\n")
        if doors.lower() == "red":
            print("Mighty flames consume you. You die. GAME OVER\n")
        elif doors.lower() == "blue":
            print("The room is full of unknown beasts. You die. GAME OVER\n")
        elif doors.lower() == "yellow":
            print("CONGRATULATIONS!\n The room ravels in riches, full of gold.\n YOU WIN!\n")
    elif lake.lower() == "swim":
        print("You get attacked by a shark. GAME OVER\n")
elif cross_road.lower() == "right":
    print("You fell into a hole. GAME OVER\n")