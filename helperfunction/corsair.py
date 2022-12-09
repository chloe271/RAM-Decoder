import re

def clean(vers):
  clean = re.sub('\D', '', vers)
  return clean
  
def manu(code):
  version_dict = {
    "2": "Elpida",
    "3": "Micron",
    "4": "Samsung",
    "5": "SK Hynix",
    "7": "Powerchip (PSC",
    "8": "Nanya"
  }
  vers = code[0]
  manu = version_dict[vers]
  return manu

def dens(code):
  version_dict = {
    "2": "4",
    "3": "8",
    "4": "16"
  }
  vers = code[1]
  dens = version_dict[vers]
  return dens

def rev(code):
  vers = code[2]
  rev = chr(65 + int(vers))
  return rev

def check(code):
  code_dict = {
    "431" : "Samsung B die, considered one of\nthe best DDR4 ICs due to its ability\nto scale up to very high voltages.",
    "432" : "C dead lul",
    "330" : "Take this with a grain of salt, corsair version\ncodes for micron 8gbit can be unreliable",
    "331" : "Take this with a grain of salt, corsair version\n codes for micron 8gbit can be unreliable",
  }
  if code in code_dict:
    check = code_dict[code]
    return check