
import os
import re

fileExtensions = ('.html','.py')
path = '/Users/arpitsingh/Documents/Python/py27-dj17/myProj'
projNameOriginal = 'tango_with_django_project'
projNameNew = 'myProj'
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
                print os.path.join(root, f)
                data = re.sub(''+(appNameOriginal)+'',appNameNew,data,flags=re.I)
            updatedFile = open(os.path.join(root, f), 'w')
            updatedFile.write(data)
            updatedFile.close()
        else:
            pass

# modify the file name as well
