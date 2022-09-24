import re, os
from urllib.request import urlopen
def version(partnumber):
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
  vers = partnumber[2:4]
  version = version_dict[vers]
  return version

def revision(partnumber):
  revision = partnumber.split(':')[1]
  return revision
  
def density(partnumber):
  density_dict = {
    "K": " KBit  x",
    "M": " MBit  x",
    "G": " GBit  x"
  }
  str = partnumber[5:]
  string = re.findall(r'\d+\w', str)
  string2 = (string[0], string[1])
  string3 = ''.join(string2)
  string4 = string3[:-1]
  for X in string4:
    if X in density_dict:
      density = string4.replace(X, density_dict[X] )
  return density

def modtype(partnumber):
  if vers == "40":
    ddr4_dict = {
      "A": "288-pin UDIMM (unbuffered)",
      "H": "260-pin SODIMM",
      "L": "288-pin LRDIMM",
      "P": "288-pin RDIMM",
      "N": "84-pin DDIMM",
      "X": "84-pin DDIMM (w/out registers)"
    }
    split = partnumber.split('-')[0]
    letter = split[-1]
    modtype = ddr4_dict[letter]
     
  elif vers == "41":
    ddr3_dict = {
      "A": "240-pin unbuffered DIMM",
      "H": "204-pin SODIMM ",
      "L": "240-pin LRDIMM",
      "P": "240-pin parity RDIMM",
    }
    split = partnumber.split('-')[0]
    letter = split[-2]
    modtype = ddr3_dict[letter]

  elif vers == "47":
    ddr2_dict = {
      "A": "240-pin unbuffered DIMM",
      "H": "200-pin SODIMM",
      "F": "240-pin fully buffered DIMM",
      "P": "240-pin Parity RDIMM",
    }
    split = partnumber.split('-')[0]
    letter = split[-2]
    modtype = ddr2_dict[letter]

  elif vers == "60":
    ddr5_dict = {
      
    }
    split = partnumber.split('-')[0]
    letter = split[-1]
    #modtype = ddr5_dict[letter] 
    modtype = "Awaiting DDR5 Information"

  else: 
    modtype = "Inconclusive Information"
    
  return modtype


def voltage(partnumber):
  volts_dict = {
    "A": "1.2V VDD",
    "B": "1.1V VDD",
    "C": "5.0V VDD",
    "D": "1.1V 0.6V VDDQ",
    "E": "1.1V 0.6/1.1V VDDQ",
    "F": "1.05V 0.5V VDDQ",
    "G": "3.0V VDD",
    "H": "1.8V VDD",
    "J": "1.5V VDD",
    "K": "1.35V VDD",
    "L": "1.2V VDD",
    "M": "1.25V VDD",
    "N": "1.0V VDD",
    "R": "1.55V VDD",
    "V": "2.5V VDD"

  }
  volt = partnumber[4]
  voltage = volts_dict[volt]
  return voltage

def misc(partnumber):
 if "ES" in partnumber:
   misc = "Engineering Sample"
 elif "MS" in partnumber:
   misc = "Mechanical Sample"
 else: 
  misc = "⠀"
 return misc


def micron(fbga):
  url= (f"https://www.micron.com/support/tools-and-utilities/fbga?fbga={fbga.upper()}#pnlFBGA")
  page = urlopen(url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  title_index = html.find("<tbody>")
  start_index = title_index + len("theResults")
  end_index = html.find("</tbody>")
  title = html[start_index:end_index]
  title = (title.replace(" ", "").replace("<tr>", "").replace("</tr>", "").replace("<td>", "").replace("</td>", ""))
  text = os.linesep.join([s for s in title.splitlines() if s])
  partnumber,fbga = text.split('\n', 1)
  return partnumber