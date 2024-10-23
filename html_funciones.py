def doctype():
  ss = '''
<html>
<body>
  '''
  return ss

def end_doctype():
  ss = '''
</body>
</html>
  '''
  return ss

def h1(hh=''):
  ss = '<h1>' + hh + '</h1>'
  return ss

def p(pp=''):
  ss = '<p>' + pp + '</p>'
  return ss

def fontt():
  f = '<font size="5">'
  return f

def end_fontt():
  f = '</font>'
  return f  


