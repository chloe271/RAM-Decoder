import requests, re
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def decode(fbga_code):
  url = 'https://www.micron.com/support/tools-and-utilities/fbga'
  params = {'fbga': fbga_code}
  
  response = requests.get(url, params=params)
  
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      part_number_cell = soup.find('td')
      if part_number_cell:
          p_n = part_number_cell.text
      else:
          print('Part number not found')
  else:
      print('Error getting part number')
  return p_n


  
def density(partnum):
  density_dict = {
    "K": " KBit  x",
    "M": " MBit  x",
    "G": " GBit  x"
  }
  str = partnum[5:]
  string = re.findall(r'\d+\w', str)
  string2 = (string[0], string[1])
  string3 = ''.join(string2)
  string4 = string3[:-1]
  for X in string4:
    if X in density_dict:
      density = string4.replace(X, density_dict[X] )
  return density
def version(partnum):
  version_dict = {
    "40": "DDR4 SDRAM",
    "41": "DDR3 SDRAM",
    "42": "Mobile LPDDR2",
    "44": "RLDRAM 3",
    "46": "DDR SDRAM/Mobile LPDDR",
    "47": "DDR2 SDRAM",
    "48": "SDRAM/Mobile LPSDR",
    "49": "RLDRAM 2",
    "51": "GDDR5",
    "52": "Mobile LPDDR3",
    "53": "Mobile LPDDR4 (2x16 ch/die)",
    "58": "GDDR5X",
    "60": "DDR5 SDRAM",
    "61": "GDDR6/GDDR6X",
    "62": "Mobile LPDDR",
    "63": "Mobile LPDDR6"
    
    
  }
  global vers
  vers = partnum[2:4]
  version = version_dict[vers]
  return version


