from singleton_object_class import SingletonObject

obj1 = SingletonObject()
obj1.val = 'Object Value 1'
obj1.val = 'anasuni meky'
print("print obj1: ", obj1)
print('----------')
obj2 = SingletonObject()
obj2.val = "anasuni mek for 2"
print("print obj1: ", obj1)
print("print obj2: ", obj2)