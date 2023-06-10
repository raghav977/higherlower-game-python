import random
import os 
people = [
    {
        "name": "lionel messi",
        "nationality": "argentina",
        "profession": "footballer",
        "followers" : 120
        
    },
    {
        "name": "Neymar",
        "nationality": "brazil",
        "profession": "footballer",
        "followers" : 80
    },
    {
        "name": "cr ronaldo",
        "nationality": "portugal",
        "profession": "footballer",
        "followers" : 100
    },
    {
        "name": "ed sheeren",
        "nationality": "usa",
        "profession": "singer",
        "followers" : 20
        
    },
    {
        "name": " zaltan",
        "nationality": "sweeden",
        "profession": "footballer",
        "followers" : 10
    },
    {
        "name": "instagram",
        "nationality": "world",
        "profession": "nothing",
        "followers": 200
    }
]
score = 0
def format_account(account):
    account_name = account["name"]
    account_nationality = account["nationality"]
    account_profession = account["profession"]
    return f"{account_name}, a {account_profession}, from {account_nationality}"

account_b = random.choice(people)

should = True
while should:
    account_a = account_b
    account_b = random.choice(people)
    if account_a == account_b:
        account_b = random.choice(people)

    def check(ask, a_follower, b_follower):
        if a_follower > b_follower:
            return ask=='a'
        else:
            return ask=='b'
            

    print(f"compare A: {format_account(account_a)}")
    print(f"against B : {format_account(account_b)}")

    ask = input("who has more followers? type'A' or 'B': ").lower()
    a_follower = account_a["followers"]
    b_follower = account_b["followers"]

    correct = check(ask,a_follower,b_follower)
    if correct:
        score +=1
        print(f"you are correct your score is {score}")
        os.system('cls')
        
    else:
        print(f"you are wrong. final score {score}")
        should = False