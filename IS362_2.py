## Finding values in a dictionary

dict = {'Name': 'Paisely', 'Age': 27, 'Level': 'Sophomore'}
print(dict['Name'])
print(dict['Age'])



## Finding key that do not exist
## Using a try except clause
dict = {'Name': 'Haley', 'Age': 21, 'Level': 'Junior'}
try:
    dict['Rainbow']
except KeyError:
    print('pass') 



## Updating a Dictionary 
dict = {'Name': 'Paisely', 'Age': 27, 'Level': 'Sophomore'}
dict['Age'] = 19; # update existing dictionay
dict['College'] = "CUNY SPS"; # Add new entry 
print("dict['Age']: ", dict['Age']) 
print ("dict['College']: ", dict['College'])


## Delete Dictionary Elements. 
dict = {'Name': 'Paisely', 'Age': 27, 'Level': 'Sophomore', 'College': 'CUNY SPS'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary
print("dict['Age']: ", dict['Age'])       # will return an error since contents of dict was cleared
print("dict['School']: ", dict['School']) # will return an error since contents of dict was cleared
