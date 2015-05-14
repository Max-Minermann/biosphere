class block:
	
	def __init__(self, bc):
		self.bc = bc
	
	def saybg(self):
		return self.bc
		

nothing = block(0)
stone = block(7)

blocknummer = [nothing, stone]
