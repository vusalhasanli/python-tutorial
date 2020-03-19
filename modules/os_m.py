import os

# email = os.getenv('MY_EMAIL')
# print(email)

# print(os.path.abspath('.'))
# print(os.path.getatime('/Users/vusal'))
# print(os.path.getmtime('/Users/vusal'))
# print(os.path.getctime('/Users/vusal'))
# print(os.path.getsize('/Users/vusal'))


print(os.path.ismount('/Volumes/Backup')) #True
print(os.path.ismount('/Volumes/root')) #False, if no access
print(os.path.ismount('/Volumes/nothing')) #False, if no path


print(os.path.relpath('/Volumes/root', start=os.curdir)) #../../../../../../Volumes/root --> relational path
print(os.path.relpath('/Volumes/root', start='/~'))
