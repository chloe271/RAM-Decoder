def ddr(o42):
  ddr_dict = {
    "04": "DDR4 SDRAM",
    "03": "DDR3 SDRAM",
    "0M": "DDR5 SDRAM",
    "0R": "DDR5 SDRAM"
  }
  gk = o42[0:2]
  ddr = ddr_dict[gk]
  return ddr


def die_revision(o42):
  die_revision = o42[-1]
  return die_revision

def gskill_manuf(o42):
  ddr_dict = {
    "1": "Samsung",
    "2": "SK Hynix",
    "3": "Micron",
    "4": "PSC",
    "5": "Nanya",
    "9": "JHICC"
  }
  position = o42[-3]
  gskill_manuf = ddr_dict[position]
  return gskill_manuf
def die_density(o42):
  die_density_dict = {
    "1": "1",
    "2": "2",
    "4": "4", 
    "8": "8",
    "S": "16",
  }
  gk_die_density_pos = o42[-5]
  die_density = die_density_dict[gk_die_density_pos]
  return die_density

def GK_die_organisation(o42):
  GK_die_organisation_dict = {
    "4": "x4", 
    "8": "x8",
    "6": "x16"
  }
  gk_die_org_position = o42[-4]
  GK_die_organisation = GK_die_organisation_dict[gk_die_org_position]
  return GK_die_organisation