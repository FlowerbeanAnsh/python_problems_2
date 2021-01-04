dct={}
lst1=['name','rolln','section','nickname']
lst2=['Ansh',21,'E','Moni']
for i in lst1:
    k=i
dct.update(k)
print(dct)
for j in lst2:
    v=j
dct.update({k:v})

