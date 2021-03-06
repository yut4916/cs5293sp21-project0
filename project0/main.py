import argparse

import urllib.request # fetchData()

import PyPDF2 # readData()

import sqlite3 # createDB()

def main():
    
    print("This is main")
    
    url = "https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-21_daily_incident_summary.pdf"
    
    # Download data
    data = fetchData(url)

    # Extract data
    incidents = readData(data)
    
    # Create our SQLite database
    db = createDB()

    # Insert data
    populateDB(incidents)

    # Testing
    f5()

def fetchData(url):
    print("Fetching data...")
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17" 
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()

    # Write the pdf data to a temp file
    tmp_file = open("/tmp/data.pdf", "wb")
    tmp_file.write(data)

    print("Data has been fetched!")

def readData(data):
    print("Reading the PDF...")

    fp = open("/tmp/data.pdf", "rb")

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    page_count = pdfReader.getNumPages()
    print(f"page count: ", page_count)

    # Get the first page
    #page1 = pdfReader.getPage(0).extractText()
    #print(f"page 0 text: ", page1)

    # Loop through each page of the pdf and extract the rows
    for i in range(page_count):
        page_i = pdfReader.getPage(i).extractText()
        #print("Page ", i+1, ":\n", page_i)
        print("Page ", i+1)

        # Clean up the data


def createDB():
    print("Creating a database...")
    
    # Create connection object that represents the database
    con = sqlite3.connect('normanpd.db')
    
    # Create a cursor object
    cur = con.cursor()

    # Delete table if it already exists
    cur.execute('DROP TABLE IF EXISTS incidents')

    # Create table
    cur.execute('''
                    CREATE TABLE incidents (
                        incident_time TEXT,
                        incident_number TEXT,
                        incident_location TEXT,
                        nature TEXT,
                        incident_ori TEXT
                    )
                ''')

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

def populateDB(incidents):
    print("Populating database...")

    # Connect to our database
    con = sqlite3.connect('normanpd.db')

    # Create cursor
    cur = con.cursor()

    # TESTING w/ some fake data
    incidents = [('2/21/2021 0:12', '2021-00010177', '2543 W MAIN ST', 'Disturbance/Domestic', 'OK0140200'),
                 ('2/21/2021 0:20', '2021-00010178', '2543 W MAIN ST', 'Traffic Stop', 'OK0140200'),
                 ('2/21/2021 0:12', '2021-00010179', '2543 W MAIN ST', 'Drunk Driver', 'OK0140200'),
                 ('2/21/2021 0:12', '2021-00010179', '2543 W MAIN ST', 'Drunk Driver', 'OK0140200'),]

    # Insert many rows of data, each with 5 values
    cur.executemany("INSERT INTO incidents VALUES (?,?,?,?,?)", incidents)

    # Don't forget to save and close, dummy!!!!
    con.commit()
    con.close()

def f5():
    print("f5")

    # Group incidents by nature

    # Count number of times each nature occurred

    # Alphabetize by nature

    # Separate fields with pipe (|)

    # Let's write some SQL
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()

    cur.execute('''
                    SELECT nature, count(nature)
                    FROM incidents 
                    GROUP BY (nature)
                    ORDER BY nature
                ''')

    print(cur.fetchall())

    con.commit()
    con.close()

if __name__ == '__main__':
    main()




