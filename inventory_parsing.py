import json

def reset_inventory():
    with open("inventory.json", "r+") as f:
        data = json.load(f)
        data["Characters"]["five_stars_chars"] = [

        ]
        data["Characters"]["four_stars_chars"] = [

        ]


        data["Weapons"]["five_stars_weapons"] = [

        ]
        data["Weapons"]["four_stars_weapons"] = [
            
        ]
        data["Weapons"]["three_stars_weapons"] = [
            
        ]

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()



def read_inventory():
    with open("inventory.json", "r") as f:
        #read the "Characters"
        data = json.load(f)
        ret = data["Characters"]
        print(ret)

        #read the "Weapons"
        weps = data["Weapons"]
        print(weps)

def write_to_inventory(item):
    "TODO"
    return

