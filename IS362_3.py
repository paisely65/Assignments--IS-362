## Returns a value for the given key. If key is not available then returns default value None.

dict = {'Name': 'Cheray', 'Age': 27}
print("Value : %s" %  dict.get('Age')) 
print ("Value : %s" %  dict.get('Education', "None"))



## Returns true if the key exists and false if it does not.
dict = {'Name': 'Mike', 'Age': 11}
print ("Value : %s" %  dict.has_key('Age'))
print ("Value : %s" %  dict.has_key('Sex'))




## Returns key value pairs as a list of tuples.
dict = {'rank': 'manager', 'Age': 47}
print ("Value : %s" %  dict.items())




## Returns a list of Dictionary keys
dict = {'Room': 2, 'Tutor': 'Jennifer', 'Subject': 'Math'}
print ("Value : %s" %  dict.keys())




## Returns a list of dictionary vlaues
dict = {'Room': 2, 'Tutor': 'Jennifer', 'Subject': 'Math'}
print ("Value : %s" %  dict.values())

