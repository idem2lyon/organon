![Image of organon](https://i.imgur.com/VvoUkMP.jpg)

This program focuses on automating the download, installation and compilation of pentest tools from source

# ATTENTION!

This tool is in development phase and **may does not work properly**.
Tool developed for Debian systems (apt)

Authors:
--------
* [Fnkoc](https://github.com/fnk0c)
* [Maximoz](https://github.com/maximozsec)

Requirements
-------------
1. Python >=2.7 or >=3.4    
2. Ruby >=1.9
3. [**bundler**](http://bundler.io/)
4. **Gems**: [mysql](https://rubygems.org/gems/mysql), [colorize](https://rubygems.org/gems/colorize), [nokogiri](https://rubygems.org/gems/nokogiri)
5. GNU/Linux system based on Debian and Arch

Install
-------
	git clone https://github.com/maximozsec/organon.git
	cd organon
	./install.sh

Tested on:
----------
* Ubuntu 14.04 x86_64
* Ubuntu 14.10 x86_64
* Debian 7.8 Wheezy
* Debian 8 Jessie
* Elementary OS Luna
* Linux Mint 17.1
* Manjaro (Unstable)

Screenshot
----------
![Screenshot](https://i.imgur.com/C4BvEh3.png)

Help
----
	* Listing available tools  
	        organon -l  
	* Searching for tools  
	        organon -s <package>
	* Installing tool  
	        organon -i <package> <package>
	* Update Organon  
	        organon -u
	* Remove tool
	        organon -r <package> <package>  
	* Remove tool and its dependencies and configuration files
	        organon -r <package> <package> --dependencies --config  
	* Clean .cache directory
	        organon --clean 
	* Current Version
	        organon -v

BUGS
----
Since it's still on development phase bugs are expected. Please, **report to us!** or open an **Issue**
* fb.com/fnkoc.a
* fb.com/maxsecur1ty
* fb.com/cienciahacker

Be Part of development
----------------------
Send us a message on facebook

About current version
---------------------

#### `v0.1.8-beta`

- **Goal**
 - Install tools and its dependences from a MySQL database

- **MySQL**
 - Server version: 5.5.41-0+wheezy1 (Debian)

 - Ruby code to connect to the database

 - Python script to execute the SQL commands and run the program

- **PKGBUILD**
 - The installation scripts were replaced by pkgconfig files, similar to pacman pkgbuild. These files are hosted on the organon server.


About previous version
---------------------
##### `v0.1.7-beta`

- **Goal**
 - Install tools and its dependences from a MySQL database

- **MySQL**
 - Server version: 5.5.41-0+wheezy1 (Debian)

- Ruby code to connect to the database

- Python script to execute the SQL commands and run the program
