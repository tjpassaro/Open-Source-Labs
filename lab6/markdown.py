import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  line = re.sub(r'\#(.*)', r'<h1>\1</h1>', line)
  line = re.sub(r'_(.*)_', r'<h1>\1</h1>', line)
  return line

def convertH2(line):
  line = re.sub(r'\#\#(.*)', r'<h2>\1</h2>', line)
  line = re.sub(r'_(.*)_', r'<h2>\1</h2>', line)
  return line

def convertH3(line):
  line = re.sub(r'\#\#\#(.*)', r'<h3>\1</h3>', line)
  line = re.sub(r'_(.*)_', r'<h3>\1</h3>', line)
  return line

def convertBlockQuote(line, inblock):
  if(inblock is 2):
    if(re.match(r'> (.*)', line)):
      line = re.sub(r'> (.*)', r'\1', line)
      line = re.sub(r'_(.*)_', r'\1', line)
    else:
      inblock = 3
  else:
    if(re.match(r'> (.*)', line)):
      line = re.sub(r'> (.*)', r'\1', line)
      line = re.sub(r'_(.*)_', r'\1', line)
      inblock = 1
  return line, inblock

blockquotes = 0
for line in fileinput.input():
  line, blockquotes = convertBlockQuote(line, blockquotes)
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  line = convertH3(line)
  line = convertH2(line)
  line = convertH1(line)
  line =  '<p>' + line + '</p>'
  if blockquotes is 3:
    line = '</blockquote>' + line
    blockquotes = 0
  elif blockquotes is 1:
    line = '<blockquote>' + line
    blockquotes = 2

  print line
if blockquotes is 2:
  print '</blockquote>'