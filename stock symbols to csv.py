from bs4 import BeautifulSoup
import requests
import csv
import sys
from datetime import datetime

def getdoc(quote):
    summary_url = "http://finance.yahoo.com/q?s=%s" % quote
    options_url = "http://finance.yahoo.com/q/op?s=%s+Options" % quote
    summ_resp = requests.get(summary_url)
    option_resp = requests.get(options_url)
    doc1 = BeautifulSoup(summ_resp.content, 'html.parser')
    doc2 = BeautifulSoup(option_resp.content, 'html.parser')
    summary(quote, doc1)
    calls(quote, doc2)
    puts(quote, doc2)

def summary(quote, doc):
    table1 = doc.find(id="table1")
    header = []
    values = []
    for item in table1.find_all('tr'):
        h, v = item.text.split(":")
        header.append(h)
        values.append(v)
    table2 = doc.find(id="table2")
    for item in table2.find_all('tr'):
        h, v = item.text.split(":")
        header.append(h)
        values.append(v)

    fname = "%s-%s-summary" % (quote, datetime.now().strftime("%Y%m%d"))
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        writer.writerow(values)

headers = ["Strike Price", "Contract Name", "Previous Close", "Open", "Bid", "Ask", "Day's Range", "Volume", "Open Interest"]

def calls(quote, doc):
    calls_div = doc.find(id="optionsCallsTable").find('tbody').find_all('tr')
    fname = "%s-%s-calls" % (quote, datetime.now().strftime("%Y%m%d"))
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        for tr in calls_div:
            writer.writerow([item.text.strip() for item in tr.find_all('td')]) 

def puts(quote, doc):
    puts_div = doc.find(id="optionsPutsTable").find('tbody').find_all('tr')
    fname = "%s-%s-puts" % (quote, datetime.now().strftime("%Y%m%d"))
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        for tr in puts_div:
            writer.writerow([item.text.strip() for item in tr.find_all('td')])

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Please provide at least one quote"
    else:
        quotes = sys.argv[1:]
        for q in quotes:
            try:
                print "Processing quote:%s" % q
                getdoc("OWW")
            except Exception as e:
                print str(e)
                print "Failed to get the details for quote: %s" % q
