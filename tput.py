import subprocess

class cbc:
	black = subprocess.check_output("tput setab 0".split()).decode()
	red = subprocess.check_output("tput setab 1".split()).decode()
	green = subprocess.check_output("tput setab 2".split()).decode()
	orange = subprocess.check_output("tput setab 3".split()).decode()
	blue = subprocess.check_output("tput setab 4".split()).decode()
	pink = subprocess.check_output("tput setab 5".split()).decode()
	magenta = subprocess.check_output("tput setab 6".split()).decode()
	grey = subprocess.check_output("tput setab 7".split()).decode()
	
class cfc:
	black = subprocess.check_output("tput setaf 0".split()).decode()
	red = subprocess.check_output("tput setaf 1".split()).decode()
	green = subprocess.check_output("tput setaf 2".split()).decode()
	orange = subprocess.check_output("tput setaf 3".split()).decode()
	blue = subprocess.check_output("tput setaf 4".split()).decode()
	pink = subprocess.check_output("tput setaf 5".split()).decode()
	magenta = subprocess.check_output("tput setaf 6".split()).decode()
	grey = subprocess.check_output("tput setaf 7".split()).decode()
	 
class cfo:
	bold = subprocess.check_output("tput bold".split()).decode()
	dim = subprocess.check_output("tput dim".split()).decode()
	smul = subprocess.check_output("tput smul".split()).decode()
	rmul = subprocess.check_output("tput rmul".split()).decode()
	rev = subprocess.check_output("tput rev".split()).decode()
	smso = subprocess.check_output("tput smso".split()).decode()
	rmso = subprocess.check_output("tput rmso".split()).decode()
	sgr0 = subprocess.check_output("tput sgr0".split()).decode()

bc = [cbc.black, cbc.red, cbc.green, cbc.orange, cbc.blue, cbc.pink, cbc.magenta, cbc.grey]

fc = [cfc.black, cfc.red, cfc.green, cfc.orange, cfc.blue, cfc.pink, cfc.magenta, cfc.grey]
