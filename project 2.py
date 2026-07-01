"""
#Foot weare
if m/f
m
 -- formal shoes
 -- casual shoes
 -- sports shoes
 -- slippers
 -- boots
 -- sneakers
 
SIZES --  6,7,8,9,10

f
 -- heels
 -- casual shoes
 -- sports shoes
 -- boots
 -- slippers
 -- sneakers

SIZES -- 4,5,6,7

kids
  -- school shoes
  -- sports shoes
  -- casual shoes
  -- slippers
  -- baby shoes

SIZES -- 1,2,3,4,5


BRANDS
 -- bata === heels,formal shoes,casual shoes,sportsshoes,sneakerws,boots,school shoes,slippers,baby shoes
 -- adidas === casual shoes, sports shoes, sneakers, slippers
 -- nike === casual shoes, sports shoes, sneakers, slippers
 -- puma === casual shoes , sports shoes ,sheakers ,boot,slippers
 -- campus == casual shoes, sports shoes, 
 -- vkc === slippers
 -- paragn== slippers,casual shoes, sports shoes,sneaker


                     ####  OUT PUT ####


you can check the foot weare of the brand is avaliable or not 
Enter your gender (M/F): m
what foot weare want to buy 
1 -- formal shoes
 2-- casual shoes
3 -- sports shoes
 4-- slippers
5 -- boots
 6-- sneakers
enter the number of the foot weare  want to buy: 2
what is you <casual shoes> size: 8
the avalable brand in 8 size:
    the avaliable brands are:
    1-bata
    2-adidas
    3-nike
    4-puma
    5-campus
    6-paragon
which brand you want to buy: 3
the <casual shoes is sold out!! in 8 size>

Enter your gender (M/F): m
what foot weare want to buy 
1 -- formal shoes
 2-- casual shoes
3 -- sports shoes
 4-- slippers
5 -- boots
 6-- sneakers
enter the number of the foot weare  want to buy: 2
what is you <casual shoes> size: 8
the avalable brand in 8 size:
    the avaliable brands are:
    1-bata
    2-adidas
    3-nike
    4-puma
    5-campus
    6-paragon
which brand you want to buy:1
the  <casual shoes > size 8 avaliable 
"""
class FootWear:

    def __init__(self):
        self.mens = {
            1: "formal shoes",
            2: "casual shoes",
            3: "sports shoes",
            4: "slippers",
            5: "boots",
            6: "sneakers"
        }

        self.womens = {
            1: "heels",
            2: "casual shoes",
            3: "sports shoes",
            4: "boots",
            5: "slippers",
            6: "sneakers"
        }

        self.kids = {
            1: "school shoes",
            2: "sports shoes",
            3: "casual shoes",
            4: "slippers",
            5: "baby shoes"
        }

        self.brand = {
            "bata": ["heels","formal shoes","casual shoes","sports shoes","slippers","boots","sneakers","school shoes","baby shoes"],
            "adidas": ["casual shoes","sports shoes","sneakers","slippers"],
            "nike": ["casual shoes","sports shoes","sneakers","slippers"],
            "puma": ["casual shoes","sports shoes","boots","sneakers","slippers"],
            "campus": ["casual shoes","sports shoes","sneakers"],
            "vkc": ["slippers"],
            "paragon": ["casual shoes","sports shoes","sneakers","slippers","formal shoes"]
        }

    def buy(self):

        gender = input("Enter your who want to buy (MALE/FEMAL/KIDS): ")

        if gender == "male" or "Male" or "MALE":
            items = self.mens
            sizes = [6,7,8,9,10]

        elif gender == "female" or "Female" or "FEMALE":
            items = self.womens
            sizes = [4,5,6,7]

        elif gender == "kids" or "Kids" or "KIDS":
            items = self.kids
            sizes = [1,2,3,4,5]

        else:
            print("Invalid ")
            return

        print("\nWhat footwear do you want to buy?\n")

        for i in items:
            print(i,"--",items[i])

        choice = int(input("Enter your choice: "))

        footwear = items[choice]

        size = int(input(f"What is your {footwear} size: "))

        if size not in sizes:
            print("Size Not Available")
            return

        print("\nAvailable Brands:")

        available = []

        num = 1

        for b in self.brand:

            if footwear in self.brand[b]:
                print(num,"-",b)
                available.append(b)
                num += 1

        ch = int(input("\nWhich brand do you want to buy: "))

        selected = available[ch-1]

        if selected == "nike":
            print(f"\nThe {footwear} is SOLD OUT in size {size}")
        else:
            print(f"\nThe {footwear} size {size} is AVAILABLE in {selected}")


obj = FootWear()

obj.buy()


        
    







 

   
