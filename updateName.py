import os
import re

fileExtensions = ('.html','.py', '.js')
path = '/Users/arpitsingh/Documents/Python/py27-dj17/myProj'
projNameOriginal = 'tango_with_django_project'
projNameNew = 'myProj'
projOriginalText = 'How to Tango with Django!'
projNewText = 'Project Name!'
appNameOriginal = 'rango'
appNameNew = 'myApp'
skipedFile = ('updateName.py',)


for root, dir, files in os.walk(path):
    for f in files:
        if f in (skipedFile):
            pass
        elif f.endswith(fileExtensions):
            with open(os.path.join(root, f)) as eachfile:
                data = eachfile.read()
            if re.search(''+(appNameOriginal)+'',data,re.I):
                print 'App name changed: ', os.path.join(root, f)
                data = re.sub(''+(appNameOriginal)+'',appNameNew,data,flags=re.I)
            elif re.search(''+(projNameOriginal)+'',data,re.I):
                print 'Project name changed: ', os.path.join(root, f)
                data = re.sub(''+(projNameOriginal)+'',projNameNew,data,flags=re.I)
            elif re.search(''+(projOriginalText)+'',data,re.I):
                print 'Project name changed: ', os.path.join(root, f)
                data = re.sub(''+(projOriginalText)+'',projNewText,data,flags=re.I)
            updatedFile = open(os.path.join(root, f), 'w')
            updatedFile.write(data)
            updatedFile.close()
        else:
            pass

# modify the file name as well
