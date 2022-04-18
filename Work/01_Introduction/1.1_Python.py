# 1. using python as a calculator
print((711.25 - 235.14) * 75)

# use the undercore (_) variable to use the result of the previous calculation
# only works with the shell environment
# print( _ * 0.80 )

# 2. getting help
help(abs)
help(round)
# help("for")
# type help() without value to enter the interative help viewer
# help()

# 4. where is my bus?
# find out how long people waiting on the corner of Clark street and Balmoral in Chicago will 
# have to wait for the next northbound CTA #22 bus
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)
    
# setting proxy
import os
os.environ['http_proxy'] = 'http://proxy.example.com:8080'
