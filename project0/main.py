# -*- coding: utf-8 -*-
# Example main.py
import argparse

import project0

def main(url):
    # Download data
    incident_data = project0.fetchincidents(url)

    # Extract data
    incidents = project0.extractincidents(incident_data)
	
    # Create new database
    db = project0.createdb()
	
    # Insert data
    project0.populatedb(db, incidents)
	
    # Print incident counts
    project0.status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)



def fetchincidents(url):
    import urllib

    url = ("https://www.normanok.gov/sites/default/files/documents/"
           "2021-02/2021-02-21_daily_incident_summary.pdf")

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()


def extractincidents(incident_data):
    import tempfile
    fp = tempfile.TemporaryFile()

    import PyPDF2

    # Write the pdf data to a temp file
    fp.write(data.read())

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pdfReader.getNumPages()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()
    # ...


def createdb():
    CREATE TABLE incidents (
        incident_time TEXT,
        incident_number TEXT,
        incident_location TEXT,
        nature TEXT,
        incident_ori TEXT
    );



