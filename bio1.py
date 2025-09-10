from Bio.Seq import Seq
from Bio import Restriction

ba = Restriction.BamHI.site
xb = Restriction.XbaI.site
sp = Restriction.SpeI.site
bs = Restriction.BsaI.site

s = Seq('GGTTAGCAGCGATTACGCTCAGGATCA').reverse_complement()
print(s)
