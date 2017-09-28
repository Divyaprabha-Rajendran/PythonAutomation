from os import listdir
from shutil import move
for f in listdir('C:\\Users\\dia5cob\\Downloads'):
 if f.endswith("pdf"):
  print(f)
  move('C:\\Users\\dia5cob\\Downloads\\'+f, 'C:\\Users\\dia5cob\\Downloads\\PDF')
 elif f.endswith("exe"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\exe')
 elif f.endswith("bin"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\bin')
 elif f.endswith("zip"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\ZIP')
 elif f.endswith("jar"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\jar')
 elif f.endswith("csv"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\csv')
 elif f.endswith("doc"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\doc')
 elif f.endswith("xlsx"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\xlsx')
 elif f.endswith("war"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\war')
 elif f.endswith("tar.gz"):
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\zip')
 else:
     print(f)
     move('C:\\Users\\dia5cob\\Downloads\\' + f, 'C:\\Users\\dia5cob\\Downloads\\OTHERS')