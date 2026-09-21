import random
num=0
while(num!=1):
    pokemon=["Pikachu","Charmandar","Bulbasaur","Squirtle"]
    chosen_poke="none"
    print("Please choose a pokemon: ")
    for i in range(len(pokemon)):
        print(i,pokemon[i])
    choice=int(input("Enter which pokemon u want: "))
    for i in range(len(pokemon)):
        if(choice==i):
            chosen_poke=pokemon[i]
    print("You chose: ",chosen_poke)
    opp_choice=random.randint(0,3)
    opp_poke=pokemon[opp_choice]
    print("Opponenet chose : ",opp_poke)
    my_health=100
    opp_health=100
    while(my_health>=1 and opp_health>=1):
        order=int(input("Press 1 to attack: "))
        dmg=random.randint(1,50)
        opp_health-=dmg
        print("You dealt ",dmg," damage to the opponent now your opponent health is ",opp_health," HP")
        if(opp_health<=0):
            break
        opp_dmg=random.randint(1,50)
        my_health-=opp_dmg
        print("Your opponent did ",opp_dmg," damage to you and now your health is ",my_health," HP")
    if(my_health>opp_health):
        print("You wonn")
    else:
        print("You lost")
    print("Game over")
    num=int(input("Press 0 to play again and 1 to quit: "))
