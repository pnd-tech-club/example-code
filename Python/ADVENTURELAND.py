#todo - more interactive combat (rock/paper/scissors?)
import random
#for ease of prompting
p = "> "
encount = 0

#Here are the functions for encounters

def make_a_choice():
	global wounds
	global weapon
	global max_wounds
	global boots
	print """
	What will you do?
	1. Turn back and find another way
	2. Fight
	3. Attempt to sneak past
	"""
	encounter_choice = raw_input(p)
	if encounter_choice == "1":
		go_back()
	elif encounter_choice == "2":
		fight()
	elif encounter_choice == "3": 
		sneak()
	elif encounter_choice == "weapon":
		print "You have a +%d weapon." % weapon
		make_a_choice()
	elif encounter_choice == "wounds":
		print "You have %d out of %d wounds remaning." % (wounds, max_wounds)
		make_a_choice()
	elif encounter_choice == "boots":
		print "You have a pair of +%d boots." % boots
		make_a_choice()
	elif encounter_choice == "help":
		print """
		Additional commands:
		weapon - returns the quality of your weapon
		wounds - returns you remaining wounds
		boots  - returns the quality of your boots
		
		Make it through the dungeon to reach the lost treasure!
		"""
		make_a_choice()
	elif encounter_choice == "quit":
		quit()
		
	else:
		print "Which choice was that, again? 1, 2, or 3?"
		make_a_choice()		

def go_back():
	print "You decide to backpedal, and successfully find another door"
	encounter()
	
def nextroom():
	print "You plow on through to the next room."
	if encount >= 10:
		print "You did it! You found the lost treasure room!"
	else:
		encounter()

def encounter():
	global encount
	enemyf()
	print "You enter room #%d. In the room, there is a%s." % (encount + 1, enemy)
	make_a_choice()
	
#combat
def fight():
	print "You have decided to fight the%s!" % enemy
	combat()
	if combatresult == 1:
		fightresult = "you defeat the%s!" % enemy
	elif combatresult == 0:
		fightresult = "the%s injures you!" % enemy
		wound()
	else:
		combat()
	print "After a short scuffle, %s!" % fightresult
	combat_result()
			
def combat():
	global combatresult
	global encount
	global weapon
	enemy_result = random.randrange(0,9)
	player_result = random.randrange(0,9)
	player_result += weapon
	enemy_result += (encount / 5)
	if player_result >= enemy_result:
		combatresult = 1
	elif player_result < enemy_result:
		combatresult = 0
	else:
		combat()
	
#resolving combat/sneak	
def combat_result():
	global encount
	global combatresult
	if combatresult == 1:
		loot()
		nextroom()
	else:
		make_a_choice()

def sneak_result():
	global encount
	global sneakresult
	if sneakresult == 1:
		loot()
		nextroom()
	else:
		make_a_choice()

#Functions for sneaking
def sneak():
	global stealthresult
	print "You attempt to sneak past the%s." % enemy
	didsneak()
	if sneakresult == 1:
			stealthresult = "you sneak past the%s!" % enemy
	elif sneakresult == 0:
		stealthresult = "the%s injures you!" % enemy
		wound()
	else:
		didsneak()
	print "After a minute of sneaking, %s!" % stealthresult
	sneak_result()
	
def didsneak():
	global sneakresult
	global encount
	global enemy
	global boots
	enemy_result = random.randrange(0,9)
	player_result = random.randrange(0,9)	
	enemy_result += (encount / 5)
	player_result += boots
	player_result += 2
	if player_result >= enemy_result:
		sneakresult = 1
		stealthresult = "you manage to slip past"
	elif player_result < enemy_result:
		sneakresult = 0
		stealthresult = "the%s catches and wounds you" % enemy

#Wound/end
def wound():
	global wounds
	wounds -= 1
	if wounds == 0:
		end()	

def end():
	print "YOU DIED"
	print "Well, you survived %d encounters. Good job." % encount
	quit()

#loot
def loot():
	global wounds
	global max_wounds
	global weapon
	global boots
	global encount
	encount += 1
	lootrand = random.randrange(0,9)
	if lootrand == 1:
		if max_wounds > wounds:
			wounds += 1
			print "You find a magic potion! You drink it, and it heals you of a wound!\n"
		else:
			print "You find a magic potion! Better safe then sorry, though.\n"
	elif lootrand == 2:
		weapon += 1
		print "Oh! You spy a weapon that looks much better than what you are using.\n"
	elif lootrand == 3:
		boots += 1
		print "You find a pair of comfier boots! These should let you move more silently.\n"
	else:
		print "There is nothing of interest in the room. Let's move on.\n"		

#Enemy finder/maker
enemylist = [" bear", " kobold", " slime", " werepig"
, " wolf", " mimic", " golem", " earth elemental", 
" fire elemental", " water elemental", " air elemental", " grue"]

def enemyf():
	global enemy
	enemyrand = random.randrange(0, len(enemylist))
	enemy = enemylist[enemyrand]
		
#character creation
def classes():
	global wounds
	global player
	global weapon
	global max_wounds
	global boots
	print """
	Choose your class:
	1. Fighter - better in combat
	2. Thief - better at sneaking
	3. Paladin - more health
	"""
	character = raw_input(p)
	if character == "1":
		player = "fighter"
		max_wounds = 4
		weapon = 2
		boots = 0
	elif character == "2":
		player = "thief"
		max_wounds = 3
		weapon = 0
		boots = 2
	elif character == "3":
		player = "paladin"
		max_wounds = 7
		weapon = 0
		boots = 0
	else:
		classes()
	wounds = max_wounds
	
#starting prompts
print "Welcome to Adventureland!"
max_wounds = 0
classes()
encounter()