#create a list using []
a = [3,4,6,7,1]
print (a[0])
print(a)
# we can overwrite a[0],a[1],etc.value
a[0] = 6
print(a)
#Accending order
a.sort()
#Reverse Order
a.reverse()
#we can add another element at last by 
a.append(2)
#we can insert another element between list by 
a.insert(2,5)
#we can remove index from the list
a.pop(3)
#we remove element of the list by
a.remove(1)
print(a)
