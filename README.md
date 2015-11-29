# stock-symbols-to-csv
A script that will take one or more stock symbols as input, and provide the 3 files as described in  CSV format
"""A script that will take one or more stock symbols as input, and provide the 3 following files, in CSV format, 
with the header line as described:
 
1)         Symbol-YYYYMMDD-summary:                
Previous Close, Open, Bid, Ask, 1y Target Estimate, Beta, Earnings Date, Day’s Range, 52 week Range, Volume, Average Volume 
(3 months), Market Cap, P/E, EPS, Dividend & Yield.
 
2)         Symbol-YYYYMMDD-calls:                        
For *ALL* the options available that day, provide the following information, one option per line:  
Option Expiration Date, Strike Price, Contract Name, Previous Close, Open, Bid, Ask, Day’s Range, Volume, Open Interest
 
3)         Symbol-YYYYMMDD-puts:             
For *ALL* the options available that day, provide the following information, one option per line:  
Option Expiration Date, Strike Price, Contract Name, Previous Close, Open, Bid, Ask, Day’s Range, Volume, Open Interest
"""
