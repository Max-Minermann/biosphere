class thing:	
	def __init__(self, bc, fc, char):
		self.char = char
		self.bc = bc
		self.fc = fc
		
	def saybc(self):
		return self.bc

	def sayfc(self):
		return self.fc
		
	def saychar(self):
		return self.char

class block(thing):
	def __init__(self, bc, fc, char):
		super().__init__(bc, fc, char)

class living(thing):
	def __init__(self, bc, fc, char):
		super().__init__(bc, fc, char)

class creature(living):
	def __init__(self, bc, fc, char):
		super().__init__(bc, fc, char)
		
#####things
nothing = thing(0, 0, " ")

####blocks
stone = block(7, 7, " ")
dirt = block(3, 3, " ")

####Living

###Creature
nobody = living(0, 0, " ")
human = living(0, 7, "☺")
cat = living(0, 1, "C")

#List
blocknummer = [stone, dirt]
creaturenummer = [nobody, human, cat]
livingnummer = [creaturenummer]
thingnummer = [nothing, blocknummer, livingnummer]
