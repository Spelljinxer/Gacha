import sys, random

def exec_gacha(pull_num):
    return pull_num

     
def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 gacha.py <number of rolls>")
        sys.exit(1)

    pull_num = int(sys.argv[1])
    print(exec_gacha(pull_num))
    #print("number of arguments : ", len(sys.argv))
    #print("arguments : ", str(sys.argv))
    #print(str(sys.argv[1]))

if __name__ == "__main__":
    main()