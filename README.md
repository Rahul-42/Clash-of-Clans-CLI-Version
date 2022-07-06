# Clash of Clans

Implemented the clash of clans 2d version in python3 using the concepts of OOPS.
## Troops
For each variety of troop, three troops can be spawned.Each troop will have the following attributes:
* Damage - the amount of damage it will yield per attack
* Health - the hitpoints it has - The health of the troop would be depicted by the colour of barbarian … the colour changes from dark to light with a change in health.
* Movement speed- Number of blocks each troop can go in a single move. 
### Barbarians
* Spawning keys of barbarians: 
 - "b": On clicking "b", the first spawning location of the barbarian gets activated and a barbarian is spawned from there
 - "2": On clicking "2", the second spawning location of the barbarian gets activated and a barbarian is spawned from there
 - "3": On clicking "3", the third spawning location of the barbarian gets activated and a barbarian is spawned from there
### Archer
Archer has an additional attribute called range, that determines the maximum distance an archer can a building from.
* Spawning keys of barbarians: 
 - "4": On clicking "4", the first spawning location of the archer gets activated and an archer is spawned from there
 - "5": On clicking "5", the second spawning location of the archer gets activated and an archer is spawned from there
 - "6": On clicking "6", the third spawning location of the archer gets activated and an archer is spawned from there
### Balloon
Balloon only attacks defensive buildings.
* Spawning keys of barbarians: 
 - "7": On clicking "7", the first spawning location of the balloon gets activated and a balloon is spawned from there
 - "8": On clicking "8", the second spawning location of the balloon gets activated and a balloon is spawned from there
 - "9": On clicking "9", the third spawning location of the balloon gets activated and a balloon is spawned from there
## King and Queen 
The user needs to decide if he wants to operate the king or the queen at the start of the game.
* Controls of king/queen:
 - " ": King or Queen performs attack
 - "v": Special attack of the queen
 - "w": moves king or queen up
 - "s": moves king or queen down
 - "a": moves king or queen to the left
 - "d": moves king or queen to the right
## Spells
* Rage Spell:
 - The Rage spell affects every troop alive in the game and the King.
 - It doubles damage and movement speed.
* Heal Spell:
 - The Heal spell affects every troop alive in the game and the King.
 - It increases their health to 150% of the current health (capped at the maximum health)
## Replay
The replay.py file replays the most recent game played.
## Cannon
* Cannons attack a single troop at any given time.
* It has a range and a damage value.It can't attack aerial troops.
* Upon getting hit, its health decreases, which is shown by a change in the colour of the cannon icon.
## Wizard tower
* It can attack aerial troops.
* The wizard tower deals AoE damage in a 3x3 tile area around the troop it is attacking.
 - In case you have many troops stacked on one another, if the wizard tower were to target and attack one of them, all of them would take damage due to the AoE damage of the wizard tower.
## Game Endings
* Each game can end in either victory or defeat.
 - Victory: All buildings (excluding walls) have been destroyed.
 - Defeat: All troops and the King have died without destroying all buildings.
* Once either of these conditions is satisfied, the game would end.
* The result of the game is displayed once it ends.
## Levels
* If the player wins a particular level, he can either opt to go to the next level or replay the same level.
* If the player loses a particular level, he has to play the same level until he wins it.
* There are three levels of difficulty in the game
 - Level 1: 2 cannons and 2 wizard towers
 - Level 2: 3 cannons and 3 wizard towers
 - Level 3: 4 cannons and 4 wizard towers

 
