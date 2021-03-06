import argparse

import urllib.request # fetchData()

import PyPDF2 # readData()

def main():
    
    print("This is main")
    
    url = "https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-21_daily_incident_summary.pdf"
    
    # Download data
    data = fetchData(url)

    # Extract data
    incidents = readData(data)
    


    # Testing
    f3()
    f4()
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
    print("f2")

    fp = open("/tmp/data.pdf", "rb")

    # Set the curser of the file back to the begining
    # fp.seek(0)

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



def f3():
    print("f3")

def f4():
    print("f4")

def f5():
    print("f5")



if __name__ == '__main__':
    main()




