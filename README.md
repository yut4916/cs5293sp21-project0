# Project 0 for Text Analytics
Written by Katy Yut
March 6, 2021

## How to Install and Use This Package
 

### Approach/Steps
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
5. Before trying to figure out how to parse the data, let's move on to creating the SQL database -- f3() or createDB()
	+ not too hard - had to follow the [tutorial](https://docs.python.org/3.8/library/sqlite3.html) to figure out how to combine SQL and python
		- answer: 
			- create a connection (connectionName = sqlite3.connect('databaseName.db'))
			- create a cursor object (cursorName = connectionName.cursor())
			- use the execute() method to perform SQL commands (cursorName.execute(" SQL code goes here "))
			- **important**: don't forget to save (connectionName.commit())
			- **important**: close the connection when done (after saving!!) (connectionName.close())
6. Next, we'll need to insert our data (once we figure step 3 out, oops) into the db from step 5 -- f4() or populateDB()
	+ ran the project again, and it looks like we have an error to deal with--our incidents table already exists (sqlite3.OperationalError: table incidents already exists)
		- idea: maybe we write a conditional statement where if incidents exists, skip, else, create it?
			- Greg says that's an ok idea, but suggested a different approach
		- Greg's idea: use some "drop table" function in SQL to delete any preexisting incidents table before running the create command 
	+ googled it, gonna follow [this](https://www.sqlitetutorial.net/sqlite-drop-table/) tutorial
		- that was easy! just had to add "DROP TABLE IF EXISTS tableName;" to my SQL chunk
	+ okay, back to insertion. the code is running as expected now, i.e. is throwing an error when it gets to the actual insertion call (since I haven't formatted the data yet)
		- **note**: will need the data to be in tuples(?) 
7. Looking ahead to the last function -- f5() or status()
	+ just gonna add some comments/structure for later
8. Before figuring out how to format the data, gonna hard code fake/test data and make sure I can insert it into my database correctly
	+ ran without error! need to open up the database and check to make sure it's in the table
		- it was not in the table...because I forgot to save and close the sqlite connection. silly!
		- fixed it, now we have 3 rows of (fake) data in our database!

## General Notes
* sudo apt install pipenv -- used this command to give me permission to install pipenv
	+ note: sudo su changes me to the super user, all powerful omniscient being. be careful (type "exit" in command line to become mortal)
	+ note: this is just for installing system files
* pipenv install packageName -- install a python package into virtual python environment
* tmux kill-session -t 0 -- kill a tmux session (0 is the window ID)

## Assumptions


## Function Descriptions
### fetchData

### readData


# Citations
Throughout the project my dad, Greg Yut, helped me understand the nuts and bolts, presumably all the stuff I should've known prior to taking this class but didn't learn because I'm not a C S student (i.e. Linux syntax/quirks, troubleshooting tips, etc). 


