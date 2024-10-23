import html_funciones as htf

fil = open('../Python_Pubmed/parkinsonO.txt', 'r')

datos = fil.readlines()

print(len(datos))

filo = open('parkinson.html', 'w')

ss = htf.doctype()
filo.write(ss)

ss = htf.fontt()
filo.write(ss)
for i in range(10):
  ss = datos[i]
  print(ss)
  ssh =  htf.p(ss)
  filo.write(ssh)


ss = htf.end_fontt()
filo.write(ss)
ss =  htf.end_doctype()
filo.write(ss)

