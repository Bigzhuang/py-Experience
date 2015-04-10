import os,re
g=os.walk('/root')
for path in g:
    for name in path[2]:
        if re.findall('.*.py$',name):
            print name
