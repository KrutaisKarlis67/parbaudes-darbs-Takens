# ----------------------------------------------------------------------
# C2. Nauda un griezieni
# ----------------------------------------------------------------------

# Lietotājam ir 20 eiro, viens grieziens maksā 3 eiro. Izvadi, cik griezienu viņš var atļauties un cik naudas paliek pāri. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Katru rezultāta rindu sāc ar zvaigznīti un atstarpi.
nauda = 20
griezieni = 0
while nauda > 3:
    nauda = nauda - 3
    griezieni = griezieni + 1

print(nauda,"naudas palika pāri")
print(griezieni,"Reizes uzgrieza")
