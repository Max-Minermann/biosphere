import subprocess

class tcbc:
	black = subprocess.check_output("tput setab 0".split()).decode()
	red = subprocess.check_output("tput setab 1".split()).decode()
	green = subprocess.check_output("tput setab 2".split()).decode()
	orange = subprocess.check_output("tput setab 3".split()).decode()
	blue = subprocess.check_output("tput setab 4".split()).decode()
	pink = subprocess.check_output("tput setab 5".split()).decode()
	magenta = subprocess.check_output("tput setab 6".split()).decode()
	grey = subprocess.check_output("tput setab 7".split()).decode()
	
class tcfc:
	black = subprocess.check_output("tput setaf 0".split()).decode()
	red = subprocess.check_output("tput setaf 1".split()).decode()
	green = subprocess.check_output("tput setaf 2".split()).decode()
	orange = subprocess.check_output("tput setaf 3".split()).decode()
	blue = subprocess.check_output("tput setaf 4".split()).decode()
	pink = subprocess.check_output("tput setaf 5".split()).decode()
	magenta = subprocess.check_output("tput setaf 6".split()).decode()
	grey = subprocess.check_output("tput setaf 7".split()).decode()
	 
class tcfo:
	bold = subprocess.check_output("tput bold".split()).decode()
	dim = subprocess.check_output("tput dim".split()).decode()
	smul = subprocess.check_output("tput smul".split()).decode()
	rmul = subprocess.check_output("tput rmul".split()).decode()
	rev = subprocess.check_output("tput rev".split()).decode()
	smso = subprocess.check_output("tput smso".split()).decode()
	rmso = subprocess.check_output("tput rmso".split()).decode()
	sgr0 = subprocess.check_output("tput sgr0".split()).decode()

tbc = [tcbc.black, tcbc.red, tcbc.green, tcbc.orange, tcbc.blue, tcbc.pink, tcbc.magenta, tcbc.grey]

tfc = [tcfc.black, tcfc.red, tcfc.green, tcfc.orange, tcfc.blue, tcfc.pink, tcfc.magenta, tcfc.grey]
