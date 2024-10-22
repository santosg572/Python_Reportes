
import html_funciones as htf

file = 'qhost2.dat'

filin = open(file, 'r')

datos = filin.readlines()

ss = datos[0]

print(ss)

global fil
fil = open('sal.html', 'w')

tt = htf.doctype()
fil.write(tt)

nl = len(datos)
fil.write('<table>\n')
for i in range(nl): 
  ss = datos[i]
  ss = ss.replace('\n','')
  ssp = ss.split(' ')
  print(len(ssp))
  if len(ssp) == 11:
    fil.write('<tr>\n')
    for ss in ssp:
      w = '<td>' + ss + '</td>\n'
      fil.write(w)
    fil.write('</tr>\n')
fil.write('<table>\n')
tt = htf.end_doctype()
fil.write(tt)

fil.close()




