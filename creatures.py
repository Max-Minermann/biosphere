class creature:
	
	def __init__(self, symbol, color):
		self.symbol = symbol
		self.color = color
		
	def saychar(self):
		return self.symbol

	def sayfc(self):
		return self.color

nobody = creature(" ", 0)
human = creature("☺", 7)

creaturenummer = [nobody, human]

