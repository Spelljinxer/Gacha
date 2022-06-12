import sys, random, time

standard_five_stars = [
    "Diluc",
    "Jean",
    "Keqing",
    "Mona",
    "Qiqi"
]

five_star_weapons = [
    "Amos' Bow",
    "Skyward Harp",
    "Lost Prayer to the Sacred Winds",
    "Skyward Atlas",
    "Skyward Pride",
    "Wolf's Gravestone",
    "Skyward Spine",
    "Aquila Favonia",
    "Skyward Blade"
]

limited_banner = [

]

def exec_gacha(charname, banner, pull_num):
    pull_counter = 0
    soft_pity = 0
    hard_pity = 0
    pull_banner = []
    if(banner == "s"):
        soft_pity = 75
        pull_banner = standard_five_stars
    if(banner == "l"):
        soft_pity = 75
        pull_banner = limited_banner
    if(banner == "w"):
        soft_pity = 65
        pull_banner = five_star_weapons

    hard_pity = soft_pity + 15

    while(pull_counter < pull_num):
        time.sleep(0.85)
        print("Pulling...")
        gacha_rate = random.uniform(0.0000, 1.000)
        

        #going to need to fix these to correspond with the actual genshin rates (math dansgame):
            #https://www.reddit.com/r/Genshin_Impact/comments/jo9d9d/the_5_rate_is_not_uniform_06_there_is_a_soft_pity/
            #https://genshin-impact.fandom.com/wiki/Cumulative_Probability 
        if(gacha_rate <= 0.0006):
            print("Congratulations! You got: ", random.choice(pull_banner))
            break

        pull_counter += 1
        if(pull_counter == hard_pity):
            print("You've reached Hard Pity. You got: ", random.choice(pull_banner))
            break
        
    
    pass #is this really needed??

def print_usage():
    return("Usage: python3 main.py [-s, -l charname, -w]  <number of rolls>\n\n(-s for standard, -l for limited, -w for weapon) ")
     
def main():
    try:
        if (not len(sys.argv) >= 3 or len(sys.argv) > 4):
            print_usage()
            sys.exit(1)
        charname = ""
        pull_num = 0
        if(sys.argv[1] == "-l"):
            charname = sys.argv[2]
            pull_num = int(sys.argv[3])
        else:
            pull_num = int(sys.argv[2])
        banner = sys.argv[1][1]
        print(exec_gacha(charname, banner, pull_num))

        sys.exit(0)
    except:
        print_usage()
        sys.exit(1)
    
    #print("number of arguments : ", len(sys.argv))
    #print("arguments : ", str(sys.argv))
    #print(str(sys.argv[1]))

if __name__ == "__main__":
    main()