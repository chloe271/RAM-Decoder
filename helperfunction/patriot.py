def patriot_ddr_manufacturer(pat):
  patriot_ddr_dict = {
    "0B": "SK Hynix",
    "11": "Samsung",
    "19": "Micron"
  }
  patriot_ddr_vers = pat[0:2]
  patriot_ddr_manufacturer = patriot_ddr_dict[patriot_ddr_vers]
  return patriot_ddr_manufacturer

def patriot_die_revision(pat):
  patriot_die_revision = pat[-2]
  return patriot_die_revision

def patriot_die_density(pat):
  patriot_die_dict = {
    "C": "4",
    "F": "8",
    "J": "16"
  }
  vers = pat[3]
  patriot_die_density = patriot_die_dict[vers]
  return patriot_die_density
