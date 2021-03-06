#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Fnkoc"
__VERSION__	= "0.1.8-r5"
__DATE__	= "31/05/2015"

"""
	THIS SCRIPT IS PART OF ORGANON
	(https://github.com/maximozsec/organon)
	
	AUTHORS:	FNKOC
				MAXIMOZ
	LICENSE:	GPL v2

	[UPDATES]
	
	--dependencies argument. Use it to remove the required dependencies of
	certain tool.
	Tools are now installed at /usr/share
	Improve remove feature
	Check if tool already installed
"""

import sys
import argparse
import os

# COLORS #######################################################################
red = "\033[31m"
white = "\33[1;37m"
green = "\033[32m"
default = "\33[1;00m"

# PYTHON 2 E 3 SUPPORT #########################################################
try:
	raw_input
except:
	raw_input = input

# BANNER #######################################################################
banner = """%s
   
   ████▄ █▄▄▄▄   ▄▀  ██      ▄   ████▄    ▄   
   █   █ █  ▄▀ ▄▀    █ █      █  █   █     █  
   █   █ █▀▀▌  █ ▀▄  █▄▄█ ██   █ █   █ ██   █ 
   ▀████ █  █  █   █ █  █ █ █  █ ▀████ █ █  █ 
           █    ███     █ █  █ █       █  █ █ 
          ▀            █  █   ██       █   ██ 
                      ▀                       
%s""" % (white, default)

# ARGUMENTOS ###################################################################

parser = argparse.ArgumentParser(description = "Package manager that focus on \
Pentest tools")
parser.add_argument("-a", "--about", action = "store_true",
	help = "About this tool")
parser.add_argument("-v", "--version", action = "store_true",
	help = "Show version and exit")
parser.add_argument("-i", nargs = "+",
	help = "Install packages")
parser.add_argument("-r", nargs = "+",
	help = "Remove packages")
parser.add_argument("--dependencies", action = "store_true",
	help = "Remove dependencies (use with -r)")
parser.add_argument("--config", action = "store_true",
	help = "Remove configuration files (use with -r)")
parser.add_argument("-u", action = "store_true",
	help = "Update Organon")
parser.add_argument("-s",
	help = "Search for package")
parser.add_argument("-l", action = "store_true",
	help = "List all packages available")
parser.add_argument("--clean", action = "store_true",
	help = "Clean Organon\'s cache")

args = parser.parse_args()

# UPDATE ORGANON FUNCTION ######################################################

def update():
	print(green + "[+] " + default + "Updating Organon")
	up = os.system("git fetch && git pull")

	if up != 0:
		print(red + " [-] " +default + "Couldn\'t retrieve update. Please \
download the latest version from https://github.com/maximozsec/organon")
	else:
		print(green + " [+] " + default + "Organon was successfully updated")

#CHECK IF PATH IS /USR/SHARE/ORGANON
#THIS CHECK HAPPENS BECAUSE WHEN YOU RUN ./INSTALL.SH THE SCRIPT IS MOVED TO
#/USR/SHARE/. INSTALL.SH ALSO INSTALL ALL DEPENDENCIES NEEDED, CREATE THE
#SYMBOLICS LINKS AND .cache DIRECTORY
if os.getcwd() != "/usr/share/organon":
	from time import sleep
		
	os.system("clear")
	print(red + "\n\n\t >> OPS! <<\n\n" + default)
	print(red + " [!] " + white + "Did you run install.sh?\n Please run \
\'./install.sh\' to install dependencies and configure Organon" + default)
	sleep(3)

def main():
	# UPDATE ORGANON ###########################################################
	if args.u:
		update()

	# INSTALL PACKAGE ##########################################################

	elif args.i:

		# PRINT PACKAGES TO BE INSTALL #########################################
		print("\n Packages (" + str(len(args.i)) + ") " + " ".join(args.i))
		choice = raw_input(green + "\n [+] " + default +"Continue the \
installation? [Y/n] ").lower()

		# CHECK IF USER WANT TO CONTINUE #######################################
		if choice != "y" and len(choice) != 0:
			print(red + " [-] " + default + "Aborted")
			sys.exit()
		else:
			# INSTALL PROCESS ##################################################
			
			for package in args.i:
				# CHECK IF ALREADY INSTALLED ###################################
				if package in (os.listdir("/usr/share") or os.listdir("/usr/\
local/share") or os.listdir("/opt")):
					print(red + " [!] " + default + "%s already installed" % \
package)

				else:
					db = os.system("ruby src/DB/database_connector.rb install \
\"SELECT url, dependencias, nome FROM debian WHERE nome LIKE '%s'\"" % \
package)
					if db == 0:
						install = os.system("python src/installer.py %s" % \
package)
					else: print(red + "[-]" + default + "Something went wrong")

					# CHECK IF SUCCESS #########################################
					if db == 0 and install == 0: print(" [+] Success!\n \
Source files can be found at .cache")

	# REMOVE PACKAGE ###########################################################

	elif args.r:
		# PRINT PACKAGES TO BE REMOVE ##########################################
		print("\n Packages (" + str(len(args.r)) + ") " + " ".join(args.r))
		choice = raw_input(green + "\n [+]" + default + " Remove these packages\
? [Y/n] ").lower()

		# CHECK IF USER WANT TO CONTINUE #######################################
		if choice != "y" and len(choice) != 0:
			print(red + " [-] " + default + "Aborted")
			sys.exit()

		else:
			# REMOVE PROCESS ###################################################
			for package in args.r:
				print(green + " [+] " + default + "Deleting source files...")
				try:
					if package in os.listdir("/usr/share"):
						os.system("sudo rm -rf /usr/share/%s" % package)
					elif package in os.listdir("/usr/local/share"):
						os.system("sudo rm -rf /usr/local/share/%s" % \
						package)
					elif package in os.listdir("/opt"):
						os.system("sudo rm -rf /opt/%s" % package)
					else:
						print(red + " [-] " + default + "%s doesn\'t seem to be\
 installed" % package)
						break
				except Exception as e:
					print(e)

				print(green + " [+] " + default + "Deleting symlink...")
				try:
					if package in os.listdir("/usr/bin"):
						os.system("sudo rm -rf /usr/bin/%s" % package)
					elif package in os.listdir("/usr/local/bin"):
						os.system("sudo rm -rf /usr/local/bin/%s" % package)
				except Exception as e:
					print(e)

				if args.config == True:
					if package in os.listdir("/etc/"):
						print(green + " [+] " + default + "Removing \
configuration files...")
						os.system("sudo rm -rf /etc/%s" % package)
					else:
						print(red + " [!] " + default + "No configuration file \
found")

				if args.dependencies == True:
					print(green + " [+] " + default + "Removing dependencies...")
					os.system("ruby src/DB/database_connector.rb remove \"\
SELECT dependencias FROM debian WHERE nome LIKE '%s'\"" % package)

	# SEARCH FOR PACKAGE #######################################################

	elif args.s:
		print(args.s)
		result = os.system("ruby src/DB/database_connector.rb list \"SELECT \
nome, versao, descricao FROM debian WHERE nome LIKE '%s'\"" % args.s)

	# LIST ALL PACKAGES ########################################################

	elif args.l:
		os.system("ruby src/DB/database_connector.rb list \"SELECT nome, versao\
, descricao FROM debian\" | more")

	# PRINT VERSION ############################################################

	elif args.version:
		print("Version: ", __VERSION__)
		print("Last update: ", __DATE__)

	# OPEN README FILE #########################################################

	elif args.about:
		os.system("cat README.md | more")

	# CLEAN ORGANON CACHE ######################################################

	elif args.clean:
		os.system("rm -rf .cache/*")

if __name__ == "__main__":
	#IF NULL
	if len(sys.argv) == 1:
		os.system("clear")
		print(banner)
		parser.print_help()

	#IF NOT NULL
	else:
		main()
