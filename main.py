import sys, random

standard_five_stars = [
    "Diluc",
    "Jean",
    "Keqing",
    "Mona",
    "Qiqi"
]


    

def exec_gacha(banner, pull_num):
    pull_counter = 0
    soft_pity = 0
    hard_pity = 0

    if(banner == "s" or "l"):
        soft_pity = 75
        hard_pity = 90
    if(banner == "w"):
        soft_pity = 65
        hard_pity = 80



    while(pull_counter < pull_num):
        gacha_rate = random.uniform(0.0000, 1.000)
        #print("gacha_rate: " + str(gacha_rate))
        if(gacha_rate <= 0.0006):
            print("Congratulations! You got: ", random.choice(standard_five_stars))
            break
        pull_counter += 1
        if(pull_counter == hard_pity):
            print("You've reached Hard Pity. You got: ", random.choice(standard_five_stars))
            break
    
    pass

     
def main():
    if(len(sys.argv) != 3):
        print("Usage: python3 gacha.py [-s, -l, -w]  <number of rolls>\n\n(-s for standard, -l for limited, -w for weapon) ")
        sys.exit(1)

    pull_num = int(sys.argv[2])
    banner = sys.argv[1][1]
    print(exec_gacha(banner, pull_num))
    
    #print("number of arguments : ", len(sys.argv))
    #print("arguments : ", str(sys.argv))
    #print(str(sys.argv[1]))

if __name__ == "__main__":
    main()