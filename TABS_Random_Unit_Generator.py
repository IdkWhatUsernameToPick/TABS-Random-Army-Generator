#Remade by IdkWhatUsernameToPick, original by iCeParadox64

import random

# I know this would be neater as a dictionary rather than two lists, but it works so I won't bother changing it.
unit = ['Clubber (Tribal)', 'Protector (Tribal)', 'Spear Thrower (Tribal)', 'Stoner (Tribal)', 'Bone Mage (Tribal)', 'Chieftan (Tribal)', 'Mammoth (Tribal)', 'Halfling (Farmer)', 'Farmer (Farmer)', 'Hay Baler (Farmer)', 'Potionseller (Farmer)', 'Harvester (Farmer)', 'Wheelbarrow (Farmer)', 'Scarecrow (Farmer)', 'Bard (Medieval)', 'Squire (Medieval)', 'Archer (Medieval)', 'Healer (Medieval)', 'Knight (Medieval)', 'Catapult (Medieval)', 'The King (Medieval)', 'Shield Bearer (Ancient)', 'Sarissa (Ancient)', 'Hoplite (Ancient)', 'Snake Archer (Ancient)', 'Ballista (Ancient)', 'Minotaur (Ancient)', 'Zeus (Ancient)', 'Headbutter (Viking)', 'Ice Archer (Viking)', 'Brawler (Viking)', 'Berserker (Viking)', 'Valkyrie (Viking)', 'Longship (Viking)', 'Jarl (Viking)', 'Samurai (Dynasty)', 'Firework Archer (Dynasty)', 'Monk (Dynasty)', 'Ninja (Dynasty)', 'Dragon (Dynasty)', 'Hwacha (Dynasty)', 'Monkey King (Dynasty)', 'Painter (Renaissance)', 'Fencer (Renaissance)', 'Balloon Archer (Renaissance)', 'Musketeer (Renaissance)', 'Halberd (Renaissance)', 'Jouster (Renaissance)', 'Da Vinci Tank (Renaissance)', 'Flintlock (Pirate)', 'Blunderbuss (Pirate)', 'Bomb Thrower (Pirate)', 'Harpooner (Pirate)', 'Cannon (Pirate)', 'Captain (Pirate)', 'Pirate Queen (Pirate)', 'Skeleton Warrior (Spooky)', 'Skeleton Archer (Spooky)', 'Candlehead (Spooky)', 'Vampire (Spooky)', 'Pumpkin Catapult (Spooky)', 'Swordcaster (Spooky)', 'Reaper (Spooky)', 'Dynamite Thrower (Wild West)', 'Miner (Wild West)', 'Cactus (Wild West)', 'Gunslinger (Wild West)', 'Lasso (Wild West)', 'Deadeye (Wild West)', 'Quick Draw (Wild West)', 'Peasant (Legacy)', 'Banner Bearer(Legacy)', 'Poacher (Legacy)', 'Blowdarter (Legacy)', 'Pike (Legacy)', 'Barrel Roller (Legacy)', 'Boxer (Legacy)', 'Flag Bearer (Legacy)', 'Pharaoh (Legacy)', 'Wizard (Legacy)', 'Chariot (Legacy)', 'Thor (Legacy)', 'Tank (Legacy)', 'Super Boxer (Legacy)', 'Dark Peasant (Legacy)', 'Super Peasant (Legacy)', 'Devout Gauntlet (Fantasy Good)', 'Celestial Aegis (Fantasy Good)', 'Radiant Glaive (Fantasy Good)', 'Righteous Paladin (Fantasy Good)', 'Divine Arbiter (Fantasy Good)', 'Sacred Elephant (Fantasy Good)', 'Chronomancer (Fantasy Good)', 'Shadow Walker (Fantasy Evil)', 'Exiled Sentinel (Fantasy Evil)', 'Mad Mechanic (Fantasy Evil)', 'Void Cultist (Fantasy Evil)', 'Tempest Lich (Fantasy Evil)', 'Death Bringer (Fantasy Evil)', 'Void Monarch (Fantasy Evil)', 'Ballooner (Secret)', 'Bomb on a Stick (Secret)', 'Fan Bearer (Secret)', 'Raptor (Secret)', 'The Teacher (Secret)', 'Jester (Secret)', 'Ball n Chain (Secret)', 'Chu Ko Nu (Secret)', 'Executioner (Secret)', 'Shouter (Secret)', 'Taekwondo (Secret)', 'Raptor Rider (Secret)', 'Cheerleader (Secret)', 'Cupid (Secret)', 'Mace SPinner (Secret)', 'CLAMS (Secret)', 'Present Elf (Secret)', 'Ice Mage (Secret)', 'Infernal Whip (Secret)', 'Bank Robbers (Secret)', 'Witch (Secret)', 'Banshee (Secret)', 'Necromancer (Secret)', 'Solar Architect (Secret)', 'Wheelbarrow Dragon (Secret)', 'Bomb Cannon (Secret)', 'Skeleton Giant (Secret)', 'Cavalry (Secret)', 'Vlad (Secret)', 'Gatling Gun (Secret)', 'Blackbeard (Secret)', 'Samurai Giant (Secret)', 'Ullr (Secret)', 'Lady Red Jade (Secret)', 'Sensei (Secret)', 'Shogun (Secret)', 'Tree Giant (Secret)', 'Artemis (Secret)', 'Ice Giant']
cost = [70, 80, 120, 160, 300, 400, 2200, 50, 80, 140, 340, 500, 1000, 1200, 60, 100, 140, 180, 650, 1000, 1500, 100, 120, 180, 300, 900, 1600, 2000, 90, 160, 220, 250, 500, 1000, 1500, 140, 180, 250, 500, 1000, 1500, 2000, 50, 150, 200, 250, 400, 1000, 4000, 100, 160, 250, 300, 1000, 1500, 2500, 80, 180, 200, 200, 1000, 1000, 2500, 100, 200, 400, 650, 740, 900, 1200, 30, 100, 120, 220, 300, 350, 450, 500, 750, 1200, 1800, 2200, 6000, 10000, 9999999, 9999999, 200, 300, 500, 800, 1000, 2000, 3000, 200, 300, 500, 800, 1000, 2000, 3000, 120, 150, 200, 200, 200, 300, 350, 350, 350, 400, 400, 450, 500, 500, 500, 500, 500, 650, 800, 850, 1000, 1100, 1200, 1200, 1400, 1500, 1700, 1800, 1800, 2000, 2600, 3000, 3000, 3500, 3500, 3500, 4000, 5500, 6000]
FinalTeam = []
budget = 0

def start():
    while True:
        try:
            global budget
            budget = int(input())
            if budget < 30:
                print("That can't buy anything! Enter a higher budget.")
            break
        except ValueError:
            print("Please enter numbers only!")
            continue

def generate():
    randunit = random.randrange(len(unit))
    global budget
    unitLimit = int(budget / cost[randunit])
    if unitLimit == 0:
        return
    elif unitLimit == 1:
        unitCount = 1
    else:
        unitCount = random.randrange(1, unitLimit)
    FinalTeam.append(str(unit[randunit] + " ×" + str(unitCount)))
    budget -= (cost[randunit] * unitCount)
    unit.pop(randunit)
    cost.pop(randunit)
#    print("Your current team is: " + str(FinalTeam))
#    print("Your remaining budget is " + str(budget))

print("Enter the budget for your team.")

while budget < 30:
    start()

while budget >= 30 and unit:
    generate()

print()
print("YOUR RANDOM TEAM IS:\n~~~~~~~~~~~~~~~~~~~~")
print(*FinalTeam, sep = "\n")
print("~~~~~~~~~~~~~~~~~~~~\n")
if budget == 0:
    print("Your team perfectly fit your budget!")
elif budget > 4000:
    print("Your team came in " + str(budget) + " gold under budget. Perhaps your budget was too high?")
else:
    print("Your team came in " + str(budget) + " gold under budget.")
input("Press Enter to close window.")
