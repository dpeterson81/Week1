from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp
# Load Config Into Variable
config = CiscoConfParse("cisco_ipsec.txt")
#Parse for all Crypto Maps named "Crypto"
crypto_maps = config.find_objects(r"^crypto map CRYPTO")
#Iterate through Maps Print Map Contents
print "Crypto Map CRYPTO Entries and Child Configurations"
for obj in crypto_maps:
  print obj.text
  pp(obj.all_children)
#Print out all maps that use PFS Group 2
group2_policy = config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", \
  childspec=r"set pfs group2")
print "\nCrypto Policies with DH Group 2 Configured"
pp(group2_policy)


