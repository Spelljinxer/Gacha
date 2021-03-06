# ---------------------------------------------------------------------------
"""
main.py: The main source file to execute the gacha

This program is designed to be used as a command line tool to execute a "gacha" using characters and weapons from the Genshin Impact universe.
For compilation and execution of this program:

    $ python3 main.py [-s, -l charname, -w]  <number of rolls>

    - where:
        -s = standard banner
        -l charname = limited banner with character name given
        -w = weapon banner
    
    Example:
        $ python3 main.py -s 40
        $ python3 main.py -l Yelan 50
        $ python3 main.py -w 60

@Author: Spelljinxer
@Credit: The name of the characters, weapons and other related assets do not belong to me. They are the sole property of Hoyoverse and respective owners.
@Status: Development
"""
# ---------------------------------------------------------------------------


import sys, random, time, json
from banners import five_stars_chars, five_stars_weapons, four_stars_chars, four_stars_weapons, three_stars_weapons
from inventory_parsing import read_inventory, reset_inventory, write_to_inventory


def exec_gacha(charname, banner, pull_num):
    pull_counter = 0
    soft_pity = 0
    hard_pity = 0
    pull_banner = []
    banner_type = ""
    if(banner == "s" or banner == "l"):
        soft_pity = 75
        pull_banner = five_stars_chars
        banner_type = "Characters"
    if(banner == "w"):
        soft_pity = 65
        pull_banner = five_stars_weapons
        banner_type = "Weapons"

    hard_pity = soft_pity + 15

    if(charname):
        five_stars_chars[-1] = charname
    
    four_star_pity = 10

    while(pull_counter < pull_num):
        print("Pulling...")
        time.sleep(0.25)
        gacha_rate = random.uniform(0.0000, 1.00)
        
        #going to need to fix these to correspond with the actual genshin rates (math dansgame):
            #https://www.reddit.com/r/Genshin_Impact/comments/jo9d9d/the_5_rate_is_not_uniform_06_there_is_a_soft_pity/
            #https://genshin-impact.fandom.com/wiki/Cumulative_Probability 
            #https://genshin-impact.fandom.com/wiki/Wishes/Expanded_Wish_Probabilities

        if(gacha_rate <= 0.0006):
            print("Congratulations! You got: ", random.choice(pull_banner))
            break
        
        if(gacha_rate <= 0.027):
            print("four star pulled\n")
            pass
        
       

        if(pull_counter == hard_pity):
            character = random.choice(pull_banner)
            print("You've reached Hard Pity. You got: ", character)
            
            write_to_inventory(str(banner_type), "five_stars_chars", character)
            break
        
        else:
            write_to_inventory("Weapons", "three_stars_weapons", random.choice(three_stars_weapons))
        
        pull_counter += 1
    
    pass 

def print_usage():
    return("Usage: python3 main.py [-s, -l charname, -w]  <number of rolls>\n\n(-s for standard, -l for limited, -w for weapon) ")


def main():
    if (not len(sys.argv) >= 3 or len(sys.argv) > 4):
        print(print_usage())
        sys.exit(1)
    if(sys.argv[1] == "-s" or sys.argv[1] == "-l" or sys.argv[1] == "-w"):
        charname = ""
        pull_num = 0
        if(sys.argv[1] == "-l"):
            charname = sys.argv[2]
            pull_num = int(sys.argv[3])
        else:
            pull_num = int(sys.argv[2])
        banner = sys.argv[1][1]
        print(exec_gacha(charname, banner, pull_num))
       
        s = input("Do you wish to see your current inventory? (y/n)\n")

        if(s == "y"):
            print("\n")
            read_inventory()
        else:
            pass

        d = input("Do you wish to reset your inventory? (y/n)\n")
        if(d == "y"):
            print("\n")
            reset_inventory()
            time.sleep(0.5)
            print("Inventory reset.")
            print("\n")
            read_inventory()
        else:
            pass
       
        # ------------------- testing writing/reading to inventory.json -------------------
        # write_to_inventory("Characters", "five_stars_chars", random.choice(five_star_chars))
        # write_to_inventory("Weapons", "five_stars_weapons", random.choice(five_star_weapons))
        # print("\n")
        # read_inventory()

        sys.exit(0)
    else:
        print(print_usage())
        sys.exit(1)

if __name__ == "__main__":
    main()