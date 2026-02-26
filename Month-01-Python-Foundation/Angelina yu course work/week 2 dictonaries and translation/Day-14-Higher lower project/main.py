
data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 180,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 175,
        "description": "Reality TV personality",
        "country": "United States"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 155,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Beyoncé",
        "follower_count": 145,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "National Geographic",
        "follower_count": 137,
        "description": "Magazine",
        "country": "United States"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 136,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 133,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Neymar",
        "follower_count": 131,
        "description": "Footballer",
        "country": "Brazil"
    },
    {
        "name": "NASA",
        "follower_count": 67,
        "description": "National Aeronautics and Space Administration",
        "country": "United States"
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 107,
        "description": "Musician",
        "country": "Trinidad and Tobago"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 102,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 97,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 107,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Cardi B",
        "follower_count": 80,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Zendaya",
        "follower_count": 66,
        "description": "Actress and musician",
        "country": "United States"
    },
    {
        "name": "Kevin Hart",
        "follower_count": 75,
        "description": "Comedian and actor",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 168,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Ellen DeGeneres",
        "follower_count": 79,
        "description": "TV host",
        "country": "United States"
    },
    {
        "name": "FC Barcelona",
        "follower_count": 79,
        "description": "Football club",
        "country": "Spain"
    },
    {
        "name": "Real Madrid C.F.",
        "follower_count": 67,
        "description": "Football club",
        "country": "Spain"
    },
    {
        "name": "Khloe Kardashian",
        "follower_count": 100,
        "description": "Reality TV personality",
        "country": "United States"
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 130,
        "description": "Model and reality TV personality",
        "country": "United States"
    },
    {
        "name": "Drake",
        "follower_count": 76,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Billie Eilish",
        "follower_count": 62,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Katy Perry",
        "follower_count": 66,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Rihanna",
        "follower_count": 88,
        "description": "Musician and actress",
        "country": "Barbados"
    }
]      

Game_over = True
while Game_over:
    print("Welcome to the Higher lower project")
    import random 
    pick1 = random.choice(data)
    pick2 = random.choice(data)

    print(f"compare A :{pick1["name"]} a {pick1["description"]} from {pick1["country"]} ")

    print("vs")
    print(f"Against B :{pick2["name"]} a {pick2["description"]} from {pick2["country"]} ")

    user_answer = input("Who has more instagram followers ").lower()

    def is_correct( pick1 , pick2,user_answer):
        if pick1["follower_count"]>pick2["follower_count"]:
            return user_answer  == "a"
        else:
            return user_answer  == "b"
        


    True_answer = is_correct(pick1, pick2, user_answer)


    if True_answer:
        print("you are right")
    else:
        print("sorry better luck next time ")

    cont = input("Do you want to continue the game type 'y' for yes and 'n' for no  ").lower()
    if cont == "y":
        continue
    else:
        Game_over = False









