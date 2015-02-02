#sets
nouncheck = []
verbcheck = []
goodcheck = []
badcheck = []
words = []

#carries the desired variable from the set
good = ""
bad = ""
noun = ""
verb = ""
dobj = ""

#vocabulary - i.e., words it can understand
timevocab = ['when', 'today', 'yesterday', 'week', 'month', 'day', 'year']
nounvocab = ['pickles', 'cake', 'it', 'food']
goodwords = ['good', 'great', 'wonderful', 'awesome', 'splendidly', 'magnificently', 'splendid', 'magnificent', 'perfectly', 'perfect', 'well']
badwords = ['bad', 'awful', 'awfully', 'terrible', 'terribly', 'poor', 'poorly']
verbvocab = ['run', 'compute', 'eat', 'drink', 'blaze']
questionvocab = ['who', 'what', 'when', 'where', 'why', 'how', 'do']
miscvocab = ['like', 'not']

#the sum of all vocab sets
vocab = timevocab + nounvocab + verbvocab + questionvocab + miscvocab + goodwords + badwords

#used to track if the next input should be a question
question_asked = '0'

#for ease of error messaging
oops = 'Sorry, I couldn\'t understand that. I\'m still learning English!'

#takes the input and breaks it down into constituent words. No caps, no punctuation
def break_words(stuff):
	global words
	words = stuff.split(' ')
	return words
	
#a relic that caused problems, might delete
def intersect(a, b):
	intersection = list(set(a) & set(b))
	return intersection
	
#compares the prompted input to the vocab and returns matches; discards unknown words
def compare():
	global comparison
	comparison = list(set(vocab) & set(break_words(raw_input("What will you say? > "))))
	return comparison
	
#similar to compare(), except it looks exclusively in nounvocab[]
def nounchecker():
	global nouncheck
	global noun
	global dobj
	nouncheck = list(set(words) & set(nounvocab))
	#null sets would otherwise make me sad
	if nouncheck != []:
		noun = nouncheck[0]
		#support for objects of verbs, assuming that the second noun of 2 is the object
		if len(nouncheck) > 1:
			dobj = ' ' + nouncheck[1]
		else:
			dobj = ' ' + noun
			
#see above
def verbchecker():
	global verbcheck
	global verb
	verbcheck = list(set(words) & set(verbvocab))
	if verbcheck != []:
		verb = verbcheck[0]
	
#see above
def timechecker():
	global timecheck
	global time
	timecheck = list(set(words) & set(timevocab))
	if verbcheck != []:
		time = timecheck[0]
	
#see above
def goodchecker():
	global goodcheck
	global good
	goodcheck = list(set(words) & set(goodwords))
	if goodcheck != []:
		good = goodcheck[0]
		
#see above
def badchecker():
	global badcheck
	global bad
	badcheck = list(set(words) & set(badwords))
	if badcheck != []:
		bad = badcheck[0]
	
#easy way of calling all the ___checker() functions
def checkem():
	nounchecker()
	verbchecker()
	goodchecker()
	badchecker()
	#etc
	
def reset():
	#gotta reset all this
	nouncheck = []
	verbcheck = []
	goodcheck = []
	badcheck = []
	words = []
	good = ""
	bad = ""
	noun = ""
	verb = ""
	object = ""

#asks for name and assigns to a variable
print 'What is your name?'
name = raw_input('> ')

#loops while 0 == 0, i.e., forever
while 0 == 0:
	#gets and filters the input
	compare()
	#parses the input
	checkem()
	#quit
	if words == ['quit']:
		quit()
	
	#if no questions have been asked by Chatty
	elif question_asked == '0':	
		if verb and 'to' and 'like' in words:
			print 'Of course I love to %s%s!' % (verb, dobj)
				
		elif 'do' and 'like' and noun in words:
			print "Why yes, I do like %s!" % noun
			print "%s, do you like %s?" % (name, noun)
			question_asked = 'like'
				
		elif 'what' and 'name' in words:
			print 'My name is Chatty!'
		
		elif 'how' and 'you' and 'today' in words:
			print "I'm great, %s. How are you?" % name
			question_asked = 'how are you'
		
		elif 'what' and 'favorite' and 'is' in words:
			if 'do' or 'activity':
				print "I like to play video games."
				print "What do you like?"
				question_asked = 'what do you like'
			elif 'food' or 'thing':
				print "I love chocolate cake!"
				print "What do you like?"
				question_asked = 'what do you like'
		
		elif 'ur' and 'a' in words:
			print "get rekt m8"
		
		else:
			print oops
		reset()
			
	elif question_asked == 'like':
		question_asked = '0'
		if words == ['yes']:
			print 'That\'s wonderful!'
		elif words == ['no']:
			print "That's too bad."
		else:
			print oops
		reset()
			
				
	elif question_asked == 'how are you':
		question_asked = '0'
		if good in words:
			if 'not' in words:
				print "I hope things get better!"
			else:
				print "I'm glad you're happy!"
		elif bad in words:
			if 'not' in words:
				print "That's great!"
			else:
				print "Oh no! Please cheer up soon!"	
		else:
			print oops
		reset()
		
	elif question_asked == 'what do you like':
		print "I like that too!"
									
#~uguu~~