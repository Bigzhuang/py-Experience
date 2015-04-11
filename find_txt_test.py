import re,os
def findstr(path,str):
    with open(path,'r+')as f:
        for num,line in enumerate(f.readlines()):
            if re.findall(str,line):
                print '''in No.%d line,you can find guda. 
                detail is:
                %s'''%(num+1,line)
#findstr('c://Python27/get_html.py','guda')

def find_file(path,str):
    for walk in os.walk(path):
        for file in walk[2]:
            if re.findall(str,file):
                return file
#                
l=[]
l.append(find_file('C://Python27','.*.py$'))
print l