import requests
import json
import sys

#Takes the Bitcion Address in
print('Check Address: ', end='')
addr = input().rstrip()
#addr = ""

#Currency Code
print("Enter Currency: ", end='')
currencycode = input().rstrip().upper()

#Sets up the websites to grab
r1 = requests.get('https://blockchain.info/en/address/' +
				addr + '?format=json')
r2  = requests.get('http://api.coindesk.com/v1/bpi/currentprice/' +
				currencycode + '.json')

#Stores the requests json
try:
    bitaddrinfo = r1.json()
except:
    sys.exit("Invalid Address")

#Grabs the exchange rate
try:
    bitconvinfo = r2.json()
    rate = bitconvinfo['bpi'][currencycode]['rate'][2:]
    balanceconv = round((bitaddrinfo['final_balance'] * 0.0000001) * float(rate), 2)
except:
    print("Error obtaining conversion rates...")
    balanceconv = "???"

balance = round(bitaddrinfo['final_balance'] * 0.00000001, 4)

#Prints The Account Information
print('Account information')
print('Address:         ' + str(bitaddrinfo['address']))
print('Balance:         ' + str(balance))
print('Balance ('+currencycode+'):   ' + str(balanceconv) + '\n')

print('Transaction History')
print('Total Recieved:  ' + str(float(bitaddrinfo['total_received'] / 100000000)))
print('Total Sent:      ' + str(float(bitaddrinfo['total_sent'] / 100000000)))
