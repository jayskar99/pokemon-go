# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jayden Cox
# Section:      568
# Assignment:   Lab13a 
# Date:         23 11 2021
#

# imports
import random
from math import cos, tan, radians, sqrt
import matplotlib.pyplot as plt

# functions
def start():
    game_login(input("Please enter your username: "))
    
def pokedex(num) :
    with open("PokeList.csv", "r") as pokelist :
        allpokemon = pokelist.read().split("\n")
        return allpokemon[num]

def gen_poke(dexnum, lvl = {}) :
    p = pokedex(dexnum+1).split(",")
    if lvl == 5 :
        pass
    else :
        lvl = random.randint(3,30)
    cp = random.randint(int(p[2]),int(p[3]))
    poke = [p[0],p[1],lvl,cp]
    return poke
    
def caught(new_pokemon,n = {}) :
    if n == 2 :
        user_poke2.append(new_pokemon)
    else :
        user_poke.append(new_pokemon)

def new_candies() :
    x = random.randint(1,100)
    if x < 40 :
        x = 1
    elif x < 65 :
        x = 3
    elif x < 85 :
        x = 5
    else :
        x = 10
    return x 
    
    
def game_login(username) :
    global usn
    usn = username
    global user_poke 
    user_poke = []
    global active_poke
    global candies
    try :
        with open("{}.csv".format(username),"r") as user :
            user.readline()
            candies = int(user.readline().strip())
            pokemons = user.readlines()
            for pokemon in pokemons :
                pokemon = pokemon.split(",")
                user_poke.append(pokemon)
        active_poke = user_poke[0]
        
    except :
        candies = 1
        with open("{}.csv".format(username),"w") as user :
            user.write("{}\n".format(username))
            user.write(str(candies).ljust(10," ")+"\n")
        choose_starter()
    main_menu()
    
def choose_starter(n = {}) :
    global active_poke
    global active_poke2
    print("\n----- Starter Selection -----\n")
    print("1. Bulbasaur\n2. Charmander\n3. Squirtle\n")
    print(d)
    try:
        choice = int(input("Please choose your starting pokemon (1-3): "))
        if choice == 1 :
            choice = 0
        elif choice == 2 :
            choice = 3
        elif choice == 3 :
            choice = 6
        pokemon = gen_poke(choice,5)
        caught(pokemon,n)
        if n == 2 :
            active_poke2 = user_poke2[0]
        else :
            active_poke = user_poke[0]
    except:
        print("invalid input: please try again")
        choose_starter(n)

def active(num = {}) :
    global active_poke
    global user_poke
    options = user_poke
    if num == "start" :
        act = 0
    else :
        print("\n---- Pokemon Selection Menu ----\n")
        print("Active Pokemon:\n{}\nCP: {}\nLevel: {}\nCandies: {}\n".format(active_poke[1],active_poke[3],active_poke[2],candies))
        print("Your Pokemon: ")
        for i in range(len(options)) :
            print("{}. {} // CP:{} // Level:{}".format(i+1, options[i][1],options[i][3],options[i][2]))
        print(d)
        try:
            act = int(input("Please choose your active pokemon(1-{}): ".format(len(options)))) - 1
            if not (act >=0 and act < len(options)) :
                int("0.1")
        except:
            print("invalid input: please try again")
            active(num)
    active_poke = user_poke[act]
    if num == 2 :
        battle_menu()
    else :
        active_menu()
    
def main_menu() :
    global usn
    global user_poke
    print("\n--------- MAIN MENU ---------\n")
    print("1. View active pokemon\n2. Catch a new pokemon\n3. Switch user\n4. Battle\n5. Save game\n6. Exit game\n")
    print(d)
    try:
        choice = int(input("Choose an option (1-6): "))
    except:
        choice = " "
    if choice == 1 :
        active_menu()
    elif choice == 2 :
        catch_game()
    elif choice == 3 :
        print(d)
        print("Thank you for playing!")
        start()
    elif choice == 4 :
        battle()
    elif choice == 5 :
        save()
        print(d)
        print("Game saved!")
        main_menu()
    elif choice == 6 :
        save()
        print(d)
        print("Thank you for playing!")
    else :
        print("invalid input: please try again")
        main_menu()

def save(num = {}) :
    if num == 2 :
        with open("{}.csv".format(usn2),"w") as user :
                user.write(usn2+"\n"+str(candies2)+"\n")
                for poke_list in user_poke2 :
                    for pp in range(len(poke_list)) :
                        if (pp + 1) == len(poke_list) :
                            user.write(str(poke_list[pp]).strip()+"\n")
                        else :
                            user.write(str(poke_list[pp])+",")
    else :
        with open("{}.csv".format(usn),"w") as user :
                user.write(usn+"\n"+str(candies)+"\n")
                for poke_list in user_poke :
                    for pp in range(len(poke_list)) :
                        if (pp + 1) == len(poke_list) :
                            user.write(str(poke_list[pp]).strip()+"\n")
                        else :
                            user.write(str(poke_list[pp])+",")
                            
def active_menu() :
    global active_poke
    global candies
    print("\n------- Active Pokemon -------")
    try:
        print("{}\nCP: {}\nLevel: {}\nCandies: {}\n".format(active_poke[1],int(active_poke[3].strip()),active_poke[2],candies))
    except:
        print("{}\nCP: {}\nLevel: {}\nCandies: {}\n".format(active_poke[1],int(float(active_poke[3])),active_poke[2],candies))
    print("1. Choose new active pokemon\n2. Level up active pokemon\n3. Return to main menu\n")
    print(d)
    try:
        choice = int(input("Choose an option (1-3): "))
    except:
        choice = " "
    if choice == 1 :
        active()
    elif choice == 2 :
        evolve_check()
    elif choice == 3 :
        main_menu()
    else :
        print("invalid input: please try again")
        active_menu()

def evolve_check() : 
    global candies
    if int(active_poke[2]) < 31 :
        req = 1
    elif int(active_poke[2]) < 41 :
        req = 2
    else :
        print("This pokemon is already max level!")
    if candies >= req :
        evolve(req)
    else :
        print("You don't have enough candy!")
        active_menu()
        
def evolve(minus) :
    global active_poke
    global candies
    if int(active_poke[2]) <= 30 :
        active_poke[3] = int(float(active_poke[3]) + (int(float(active_poke[3]))) * 0.0093 / (0.094 * sqrt(int(active_poke[2]))))
    else :
        active_poke[3] = int(float(active_poke[3]) + (int(float(active_poke[3]))) * 0.0044 / (0.094 * sqrt(int(active_poke[2]))))
    active_poke[2] = int(active_poke[2]) + 1
    candies -= minus
    active_menu()

def catch_game() :
    global candies
    wild = gen_poke(random.randint(0,149))
    target = (random.randint(10, 1000), random.randint(0, 50), random.randint(10, 50))
    initial_plot(target)
    print(d)
    print("A wild level {} {} appeared!\nTry and hit it with one of your pokeballs! Be careful though, you only have 5 throws!".format(wild[2],wild[1]))
    v_guess, theta_guess = get_guesses() 
    x, y = trajectory(v_guess, theta_guess) 
    for i in range(4) :
        if not hit(x, y, target):
            print("Try again,{} attempts remaining-".format(4-i))
            game_plot(x, y, target)
            v_guess, theta_guess = get_guesses() 
            x, y = trajectory(v_guess, theta_guess)
            print(d)
    if hit(x, y, target) :
        print('Got it!\nWild {} was caught!'.format(wild[1]))
        z = new_candies()
        candies += z
        caught(wild)
        print("You recieved {} candies".format(z))
        
    else :
        print("The wild {} ran away!".format(wild[1]))
    game_plot(x, y, target, True)
    main_menu()
   
def battle() :
    print(d)
    choose_opponent(input("Enter username of player 2: "))
    battle_menu()
   
# battle
def battle_menu() :
    print("\n--------- BATTLE MENU ---------\n")
    print("1. Player 1 choose active pokemon\n2. Player 2 choose active pokemon\n3. Begin battle\n4. Change opponent\n5. Exit to main menu\n")
    print(d)
    try:
        choice = int(input("Choose an option (1-5): "))
    except:
        choice = " "
    if choice == 1 :
        active(2)
    elif choice == 2 :
        active2()
    elif choice == 3 :
        fight()
    elif choice == 4 :
        battle()
    elif choice == 5 :
        main_menu()
    else :
        print("invalid input: please try again")
        battle_menu()
        
def choose_opponent(username) :
    global candies2
    global usn2
    usn2 = username
    global active_poke2
    global user_poke2
    user_poke2 = []
    try :
        with open("{}.csv".format(username),"r") as user2 :
            user2.readline()
            candies2 = int(user2.readline().strip())
            pokemons = user2.readlines()
            for pokemon in pokemons :
                pokemon = pokemon.split(",")
                user_poke2.append(pokemon)
        active_poke2 = user_poke2[0]
        
    except :
        candies2 = 1
        with open("{}.csv".format(username),"w") as user2 :
            user2.write("{}\n".format(username))
            user2.write(str(candies2).ljust(10," ")+"\n")
        choose_starter(2)
        save(2)
 
def active2(num = {}) :
    global active_poke2
    global user_poke2
    options = user_poke2
    if num == "start" :
        active = 0
    else :
        print("\n---- Pokemon Selection Menu ----\n")
        print("Active Pokemon:\n{}\nCP: {}\nLevel: {}\nCandies: {}\n".format(active_poke[1],active_poke[3],active_poke[2],candies))
        print("Your Pokemon: ")
        for i in range(len(options)) :
            print("{}. {} // CP:{} // Level:{}".format(i+1, options[i][1],options[i][3],options[i][2]))
        print(d)
        try:
            active = int(input("Please choose your active pokemon(1-{}): ".format(len(options)))) - 1
            if not (active >=0 and active < len(options)) :
                int("0.1")
        except:
            print("invalid input: please try again")
            active2(num)
    active_poke2 = user_poke2[active]
    battle_menu()

def fight() :
    global end
    end = False
    global health1
    global health2
    health1 = int(active_poke[2])
    health2 = int(active_poke2[2])
    while not end :
        p_move(1,int(active_poke[2]))
        if not end :
            p_move(2,int(active_poke2[2]))
    main_menu()

def p_move(turn,lvl) :
    att = move(turn)
    if att == 1 :
        m = 75
        dam = .5*lvl
    elif att == 2 :
        m = 50
        dam = .75*lvl
    luck = random.randint(0,100)
    try:
        if luck < m :
            print("Player {}'s attack hit!".format(turn))
            health(turn,dam)
        else :
            print("Player {}'s attack missed!".format(turn))
    except:
        print("invalid input: please try again")
    display_health()
    
def move(player) :
    print("\n--------- Move List ---------\n")
    print("1. Weak Move (more likely to hit)\n2. Strong Move (less likely to hit)\n")
    print(d+"\n")
    try:
        attack = int(input("Player {} choose a move (damage based on pokemon's level): ".format(player)))
        return attack
    except:
        print("invalid input: please try again")
        move(player)
def health(player,damage) :
    global health1
    global health2
    if player == 1 :
        health2 -= damage
    elif player == 2 :
        health1 -= damage
    
def display_health() :
    global end
    print("Player 1's pokemon's health: {}".format(health1))
    print("Player 2's pokemon's health: {}".format(health2))
    if health1 <= 0 :
        print("Player 1's pokemon fainted! Player 2 wins!")
        end = True
    elif health2 <= 0 :
        print("Player 2's pokemon fainted! Player 1 wins!")
        end = True
    
# game
def get_guesses():
    '''Parameters: None;Return values: float;Gets guesses'''
    try:
        v_guess = float(input("Velocity guess: "))
        theta_guess = float(input("Theta guess: "))
    except:
        print("invalid input: please try again")
        get_guesses()
    return v_guess,theta_guess

def trajectory(vo,angle):
    """Parameters: floats;Return values: lists;Calculate the trajectory of bird"""
    g = 9.807
    xvals = []
    yvals = []
    for x in range(1000) :
        xvals.append(x)
        yvals.append(int(trajectory_y(x,g,vo,angle)))   
    return xvals, yvals

def trajectory_y(x, g, vo, angle):
   """Returns (y-value) of the trajectory for a given x-val, gravity, initial velocity,and angle."""
   angle = radians(angle)
   return (x*tan(angle))-(g*x**2)/(2*(vo**2)*cos(angle)**2)

def initial_plot(t):
    plt.plot(t[0],t[1],"ko",markersize = t[2])
    plt.xlim(0,1000)
    plt.ylim(0,100)
    plt.show()
    
def game_plot(xvals,yvals,t,b = {}):
    """Parameters: lists;Return values: None;Plots the trajectory and target"""
    plt.plot(xvals,yvals,"k--")
    plt.plot(t[0],t[1],"ko",markersize = t[2])
    if b :
        plt.plot(t[0],t[1],"wo",markersize = t[2]+1.5)
        plt.plot(t[0],t[1],"x",markersize = t[2], color = "red")
    plt.xlim(0,1000)
    plt.ylim(0,100)
    plt.show()

def hit(xvals,yvals,t):
    """Parameters: integers;Return values: boolian;Determines if its a hit or not"""
    for x in range(len(xvals)) :
        if xvals[x] > (t[0]-(t[2])/1.5) and xvals[x] < (t[0]+(t[2])/1.5) and yvals[x] > (t[1]-(t[2])/1.5) and yvals[x] < (t[1]+(t[2])/1.5) :
            hit = True
            break
        else :
            hit = False
    return hit

# code body
d = "------------------------------"
start()
















