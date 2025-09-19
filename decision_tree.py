import random as rand

deaths = ["You got shot.", "You got smushed by oncoming traffic.", "You have a heart attack and die.", "You are murdered in your sleep.", "He gives you an air embolism."]
goods = ["You go on with your life.", "You convince him to give you a ride home.", "The police arrive and take you home."]

def bad():
    print(rand.choice(deaths))
    choice = str(input("Would you like to play again? (yes/no) ")).lower()
    if choice == "yes":
        story()
    else:
        print("Thanks for playing!")
        exit()

def good():
    print(rand.choice(goods))
    choice = str(input("Would you like to play again? (yes/no) ")).lower()
    if choice == "yes":
        story()
    else:
        print("Thanks for playing!")
        exit()

def story():
    situation = print("A car pulls up next to you.")
    choice = str(input("Should you get in? (yes/no) ")).lower()
    if choice == "yes":
        situation = print("The driver offers you a bottle of water.")
        choice = str(input("Do you dirnk it? (yes/spit it out/no) ")).lower()
        if choice == "yes":
                situation = print("You get VERY tired.")
                choice = str(input("Should you fight it and stay awake, or give in and sleep? (fight/give in) ")).lower()
                if choice == "fight":
                    situation = print("You get taken to a warehouse but you cant fight back or escape due to being tired.")
                    choice = str(input("Should you cooperate, try and fight, or make a plan to escape? (cooperate/fight/plan) ")).lower()
                    if choice == "cooperate":
                        situation = print("They thank you for cooperating but dont want to let you go incase you go to the police.")
                        bad()
                    elif choice == "fight":
                        situation = print("You attempt to fight back but you exert all your energy leaving yourself vulnerable.")
                        bad()
                    else:
                        situation = print("You make a plan to escape and wait for the right moment.")
                        situation = print("He forgets about you and you escape.")
                        choice = str(input("Should you go about your life or go to the police? (life/police) ")).lower()
                        if choice == "life":
                            good()
                        else:
                            bad()
                else:
                    situation = print("You wake up in your bed with no memory of how you got there.")
                    choice = str(input("Do you go about your life or go to the police? (life/police) ")).lower()
                    if choice == "life":
                        good()
                    else:
                        situation = print("You go to the police, but your kidnappers have already covered their tracks.")
                        bad()
        elif choice == "spit":
            situation = print("He gets mad about his car getting wet.")
            choice = str(input("Should you apologize or tell him its his fault? (apologize/his fault) ")).lower()
            if choice == "apologize":
                situation = print("He is angry but forgives you.")
                choice = str(input("Tell him it was a joke or try and gain his trust? (joke/trust) ")).lower()
                if choice == "joke":
                    situation = print("He doesnt find it funny.")
                    bad()
                else:
                    situation = print("He starts to trust you.")
                    choice = str(input("Go home and live your life or go to the police? (life/police) ")).lower()
                    if choice == "life":
                        good()
                    else:
                        situation = print("You go to the police, but your kidnappers have already covered their tracks.")
                        bad()
        else:
            situation = print("He pressures you.")
            choice = str(input("Do you give in or refuse? (give in/refuse) ")).lower()
            if choice == "give in":
                situation = print("You get VERY tired.")
                choice = str(input("Should you fight it and stay awake, or give in and sleep? (fight/give in) ")).lower()
                if choice == "fight":
                    situation = print("You get taken to a warehouse but you cant fight back or escape due to being tired.")
                    choice = str(input("Should you cooperate, try and fight, or make a plan to escape? (cooperate/fight/plan) ")).lower()
                    if choice == "cooperate":
                        situation = print("They thank you for cooperating but dont want to let you go incase you go to the police.")
                        bad()
                    elif choice == "fight":
                        situation = print("You attempt to fight back but you exert all your energy leaving yourself vulnerable.")
                        bad()
                    else:
                        situation = print("You make a plan to escape and wait for the right moment.")
                        situation = print("He forgets about you and you escape.")
                        choice = str(input("Should you go about your life or go to the police? (life/police) ")).lower()
                        if choice == "life":
                            good()
                        else:
                            bad()
                else:
                    situation = print("You wake up in your bed with no memory of how you got there.")
                    choice = str(input("Do you go about your life or go to the police? (life/police) ")).lower()
                    if choice == "life":
                        good()
                    else:
                        situation = print("You go to the police, but your kidnappers have already covered their tracks.")
                        bad()
            else:
                situation = print("He gets mad")
                bad()
    else:
        situation = print("He follows you slowly.")
        choice = str(input("Should you tell him off, get in, or ignore him? (tell/get in/ignore) ")).lower()
        if choice == "tell":
            situation = print("He gets out and forces you in.")
            choice = str(input("Should you fight back or cooperate? (fight/cooperate) ")).lower()
            if choice == "fight":
                situation = print("You attempt to fight back but you get overpowered.")
                bad()
            else:
                situation = print("You get in the car and start getting uncomfortable.")
                choice = str(input("Ask for food or stay quiet and start squirming? (food/quiet) ")).lower()
                if choice == "food":
                    situation = print("He gets angry.")
                    bad()
                else:
                    situation = print("Turns out he is schizophrenic and thinks you are plotting to escape.")
                    bad()
        elif choice == "get in":
            situation = print("He's glad you came to your senses.")
            choice = str(input("Say nothing or talk to him? (nothing/talk) ")).lower()
            if choice == "nothing":
                situation = print("He thinks you're plotting something.")
                bad()
            else:
                situation = print("He gets upset with you.")
                bad()
        else:
            situation = print("He starts shouting at you.")
            choice = str(input("Should you shout back or keep walking? (shout/walk) ")).lower()
            if choice == "shout":
                situation = print("You convince him to leave you alone.")
                good()
            else:
                situation = print("He gets angrier and angrier.")
                bad()
story()