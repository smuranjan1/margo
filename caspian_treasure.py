#Choose Your Own Adventure

#Introduction and Choosing Weapons

def main():
    weapon = 0
    print("Once upon a time,")
    print("you were getting ready for a quest to search for the Great Caspian hidden Treasure.")
    print("It was said to be hidden by the Great Pirate Caspian in hopes of keeping for younger generations.")
    print("You set out to be the one who claims the treasure and the glory.")
    print("You found the map on June 7th and are ready to set out on your quest.")
    print("You can only bring one weapon because it is all that fits in your satchel")
    print("You can choose from a spear and a hatchet for weapons. What do you choose?")
    weapon = int(input("1-Spear\n2-Hatchet\n"))
    if weapon == 1:
        print("Now with your spear and your intellect you set out on your mission")
        path(weapon)
    elif weapon == 2:
        print("Now with your hatchet and your intellect you set out on your mission")
        path(weapon)

#This Function gives you the choice of what path to take
def path(weapon):
    trail =0
    print ("You set out on the path your map is telling you but then there is a fork in the path.")
    print("One of the paths goes through the Forest of Dreams  and the other goes through the Cave of Illusion. Where will you go?")
    trail = int(input("1-Forest Path\n2-Cave Path\n"))
    if weapon == 1 and trail == 1:
        print ("You then set out with you spear and go into the Forest of Dreams")
        forest(weapon)
    elif weapon == 1 and trail == 2:
        print ("You then set out with you spear and go into the Cave of Illusion")
        cave (weapon)
    elif weapon ==2 and trail == 1:
        print ("You then set out with you hatchet and go into the Forest of Dreams")
        forest(weapon)
    elif weapon == 2 and trail == 2:
        print ("You then set out with you hatchet and go into the Cave of Illusion")
        cave (weapon)

# This Function gives you the choice of what Potion to Take
def forest(weapon):
    potion=0

    print("You enter the Forest of dreams and you start to get dreary.")
    print("Is it the air or the animals in front of you spinning round an round so fast it's, making you  a bit dizzy?")
    print("Before you almost blackout you spot 2 potions in front of you, a gray one and a blue one. Which do you choose to drink?")
    potion=int(input("1-Gray Potion\n2-Blue Potion\n"))
    if potion==1:
        print("The gray potion was a strong sleeping potion putting you in eternal sleep choices away from the treasure")
        print("Restart to change the outcome of your adventure or accept your fate right before the treasure.")
    elif potion == 2:
        print("The blue potion revives you from your cloudy self and gives you energy to keep searching for the treasure.")
        companion()

#This is the Cave Function
def cave (weapon):
    if weapon == 1:
        print ("As you went into the cave everything looked odd")
        print("Cotton Candy trees, frog and bird hybrids, and Venus Fly Traps the height of school buses ")
        print("Then the Dragon of Illusion comes and is ready to attack. You attempt to stand your ground using you spear but it was no use compared to his Fiery Breath.")
        print("Your mind couldn't take the mind boggling things all around you and your body couldn't take all your battle wounds and the heat.")
        print("You die steps away from the hidden treasure.")
    elif weapon == 2:
        print ("As you went into the cave everything looked odd")
        print("Cotton Candy trees, frog and bird hybrids, and Venus Fly Traps the height of school buses ")
        print("Then the Dragon of Illusion comes and is ready to attack. You attempt to stand your ground using you hatchet but it was no use compared to his Fiery Breath.")
        print("Your mind couldn't take the mind boggling things all around you and your body couldn't take all your battle wounds and the heat.")
        print("You die steps away from the hidden treasure.")
        print("Restart your adventure to potentially reach the hidden treasure or accept your defeat in the Cave of Illusions.")

#Animal Function
def companion():
    guide=0
    print ("With your newfound strength you venture on through the Forest of Dreams.")
    print("You walk for what seems like an eternity until you find three animals in front of you")
    print("A sign next to them tells you that one of them will guide you to the Caspian's Treasure and the others will lead you to your death.")
    print("There is a Dalmatian, a Sphinx Cat, and a Parrot")
    print("What will you choose to hopefully guide you to your victory?")
    guide = int(input("1-Dalmatian\n 2-Sphinx Cat \n 3- Parrot\n"))
    if guide == 1:
        print("The Dalmation lead you with it's head up high and with his eyes closed.")
        print("You followed him blindly and you start to daydream of you swimming through gold and then you walk right into a 10 ft 4 in Cactus with foot long spikes.")
        print("You would've been fine but one spike somehow was able to reach your heart killing you instantly.")
        print("Try again with your adventure or accept your piercing fate.")
    elif guide == 2:
        print ("The sphinx Cat is quick to lead the way. ")
        print("You follow carefully but after what seemed like 2 hours you get kind of tired of checking.")
        print("You then come along to the Cliff of Bear Traps. ")
        print("Now you see, in a forest of dreams there are things you'll find in many people's dreams but a lot of things from people's nightmares.")
        print("So you follow the cat and fall 46 feet of the cliff and hope that the landing will be not injure you horribly, until you meet your fate 4 feet later in a Bear Trap.")
        print("You can restart and attempt to claim your Treasure or accept your Fate 50 feet down under.")
    elif guide == 3:
        print("The Parrot flies just low enough for you to still see it and you follow it with caution")
        print("The Parrot leads you into a cave with a Vault in no time at all.")
        vault()

    
def vault ():
    answer=0
    print ("Their is one final sign giving you a riddle saying, 'What has cities but no houses, forests but no trees, and water but no fish'")
    print("The sign continues to say,'When you are ready, answer away, if it is right, Casppian's Treasure will be yours today.' ")
    print("'Your choices are idea, map, car, bat. What will you choose to put another feather in your hat?'")
    answer= int(input("1-idea\n2-map\n3-car\n4-bat\n"))
    if answer == 2:
        print("The vault creaked open and then loads of gold, diamonds, sapphires, and money came flooding out all for you to take home.")
        print("Animals from all over, including the parrot who took you here, worked together to bring the gold, money, and valuable items to your home.")
        print("You went to your hometown with a MASSIVE grin on your face, as you are now known as the'Succesful Seeker of the Caspian Treasure.")
        print("The End")
    else:
        print("You hear a creak above you. You hope money will come flooding down but it is very unlikely.")
        print("You wince at the sound of creaking once again.")
        print("Then a Boulder comes falling swiftly down to the very place you stand. ")
        print ("In seconds your crushed, internally and very much physically. You frown as you could've been the bearer of the Great Caspian Treasure")
        print("You can restart your adventure to the Great Caspian Treasure or accept your crushing fate.")
if __name__ == '__main__':
    main()