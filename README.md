# Project 0 for Text Analytics
## cs5293sp21-project0

### Steps
1. Setup file structure
	+ create README
	+ paste bare bones code provided in project outline
2. Insert print statements into each function to ensure they are being called/run correctly
3. Try to get the PDF downloaded -- f1() or fetchData()
	+ seems like the code works when in main, so now let's move it to its own function, just called f1 for now
		- for now, just gonna hard code the url into the function
	+ f1 is working, but I'm not sure how to look at the data
		- when I run print(data), it's a long mess of numbers and f\r\n etc
		- when I run print(data.head()) (is that even the syntax in python? I forget) it throws the error "AttributeError: 'bytes' object has no attribute 'head'
	+ now let's rename our function fetchData, more intuitive than f1
	+ cool, now let's try to pass url as a variable to the main function
		- ok, that didn't work
	+ plan b: hard code the url in the main function, and pass it as a variable to the fetchData function
		- that worked! let's keep it like that for now and move on
4. Now that we have the pdf, let's try to actually get the data outta there -- f2() or readData() 
	+ my data seems to be in the wrong format - bytes instead of something more sensible/readable 
	+ ended up writing the pdf into my /tmp folder as "data.pdf" - now I can read in the binary data and make it readable
		- reasoning: it worked

## General Notes
* sudo apt install pipenv -- used this command to give me permission to install pipenv
	+ note: sudo su changes me to the super user, all powerful omniscient being. be careful (type "exit" in command line to become mortal)
	+ note: this is just for installing system files
* pipenv install packageName -- install a python package into virtual python environment
* tmux kill-session -t 0 -- kill a tmux session (0 is the window ID)

## Assumptions


## Functions
### fetchData

### readData


# Citations
Throughout the project my dad, Greg Yut, helped me understand the nuts and bolts, presumably all the stuff I should've known prior to taking this class but didn't learn because I'm not a C S student (i.e. Linux syntax/quirks, troubleshooting tips, etc). 


