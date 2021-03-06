import argparse

import urllib.request # fetchData()

import PyPDF2 # f2()

import tempfile # f2()

#import project0

def main():
    
    print("this is main")
    
    url = "https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-21_daily_incident_summary.pdf"
    
    # Download data
    data = fetchData(url)

    print(data == None)

    # Extract data
    incidents = f2(data)
    


    # Testing
    f3()
    f4()
    f5()

def fetchData(url):
    print("Fetching data...")
    
    #url = "https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-21_daily_incident_summary.pdf"

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17" 
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()

    print("Data has been fetched!")

    return data

def f2(data):
    print("f2")

    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data.read())

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    page_count = pdfReader.getNumPages()
    print(f"page count: ", page_count)

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()
    print(f"page 0 text: ", page1)

    # etc


def f3():
    print("f3")

def f4():
    print("f4")

def f5():
    print("f5")



if __name__ == '__main__':
    main()




