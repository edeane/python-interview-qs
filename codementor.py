#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:32:58 2017

@author: applesauce

interview questions

https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6
"""


import os
import time

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
            
#print_directory_contents('/home/applesauce/galvanize/immersive/pyimagesearchtutorials')

#A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#A1 = list(range(10))
#A2 = sorted([i for i in A1 if i in A0])
#A3 = sorted([A0[s] for s in A0])
#A4 = [i for i in A1 if i in A3]
#A5 = {i:i*i for i in A1}
#A6 = [[i,i*i] for i in A1]

#print('A0', A0)
#print('A1', A1)
#print('A2', A2)
#print('A3', A3)
#print('A4', A4)
#print('A5', A5)
#print('A6', A6)

#A0 {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#A1 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#A2 []
#A3 [1, 2, 3, 4, 5]
#A4 [1, 2, 3, 4, 5]
#A5 {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#A6 [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    return(l)

#print('f(2)', f(2))
#print('f(3,[3,2,1])', f(3,[3,2,1]))
#print('f(3)', f(3))

#f(2) [0, 1]
#f(3,[3,2,1]) [3, 2, 1, 0, 1, 4]
#f(3) [0, 1, 4]


def f(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}
    
#f()
#f(1,2,3)
#f(1,2,3,'groovy')
#f(a=1, b=2, c=3)
#f(a=1,b=2,c=3,zzz='hi')
#f(1,2,3,a=1,b=2,c=3)  
#f(*l, **d)
#f(*t, **d)
#f(1,2,*t)
#f(q='winning', **d)
#f(1,2,*t,q='winning',**d)

#args ()
#kwargs {}
#args (1, 2, 3)
#kwargs {}
#args (1, 2, 3, 'groovy')
#kwargs {}
#args ()
#kwargs {'a': 1, 'b': 2, 'c': 3}
#args ()
#kwargs {'a': 1, 'b': 2, 'c': 3, 'zzz': 'hi'}
#args (1, 2, 3)
#kwargs {'a': 1, 'b': 2, 'c': 3}
#args (1, 2, 3)
#kwargs {'a': 7, 'b': 8, 'c': 9}
#args (4, 5, 6)
#kwargs {'a': 7, 'b': 8, 'c': 9}
#args (1, 2, 4, 5, 6)
#kwargs {}
#args ()
#kwargs {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}
#args (1, 2, 4, 5, 6)
#kwargs {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}


def f2(arg1, arg2, *args, **kwargs):
    print('arg1', arg1)
    print('arg2', arg2)
    print('args', args)
    print('kwargs', kwargs)
    
#f2(1,2,3)                       # 1 2 (3,) {}
#f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
#f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
#f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
#f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}
#
#f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
#f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
#f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
#f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
#f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

#arg1 1
#arg2 2
#args (3,)
#kwargs {}
#arg1 1
#arg2 2
#args (3, 'groovy')
#kwargs {}
#arg1 1
#arg2 2
#args ()
#kwargs {'c': 3}
#arg1 1
#arg2 2
#args ()
#kwargs {'c': 3, 'zzz': 'hi'}
#arg1 1
#arg2 2
#args (3,)
#kwargs {'a': 1, 'b': 2, 'c': 3}
#arg1 1
#arg2 2
#args (3,)
#kwargs {'a': 7, 'b': 8, 'c': 9}
#arg1 4
#arg2 5
#args (6,)
#kwargs {'a': 7, 'b': 8, 'c': 9}
#arg1 1
#arg2 2
#args (4, 5, 6)
#kwargs {}
#arg1 1
#arg2 1
#args ()
#kwargs {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}
#arg1 1
#arg2 2
#args (4, 5, 6)
#kwargs {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}
    
def time_this(original_function):
    def new_function(*args,**kwargs):
        import datetime
        before = datetime.datetime.now()     
        x = original_function(*args,**kwargs)     
        after = datetime.datetime.now()     
        print('new_function args: {} kwargs: {}'.format(args, kwargs))
        print("Elapsed Time = {0}".format(after-before))
        return x
    return new_function

@time_this
def func_a(sleep_time):
    time.sleep(sleep_time)
    print('func_a sleep_time: {}'.format(sleep_time))


#func_a(2)
#func_b = time_this(func_a)
#func_b(3)


class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print("calling normal_method({0},{1})".format(args,kwargs))
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})".format(args,kwargs))
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})".format(args,kwargs))
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})".format(self,args,kwargs))
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_other_property
    
#o = MyClass()
#o.normal_method #<bound method MyClass.normal_method of <__main__.MyClass object at 0x7fb27d8f1048>>
#o.normal_method() #calling normal_method((<__main__.MyClass object at 0x7fb27d8f1048>,),{})
#o.normal_method(1,2,x=3,y=4) #calling normal_method((<__main__.MyClass object at 0x7fb27d8f1048>, 1, 2),{'x': 3, 'y': 4})
#o.class_method #<bound method MyClass.class_method of <class '__main__.MyClass'>>
#o.class_method() #calling class_method((<class '__main__.MyClass'>,),{})
#o.class_method(1,2,x=3,y=4) #calling class_method((<class '__main__.MyClass'>, 1, 2),{'x': 3, 'y': 4})
#o.static_method #<function __main__.MyClass.static_method>
#o.static_method() #calling static_method((),{})
#o.static_method(1,2,x=3,y=4) #calling static_method((1, 2),{'x': 3, 'y': 4})
#o.some_property #calling some_property getter(<__main__.MyClass object at 0x7fb27d8f1048>,(),{})
##                Out[30]: 'properties are nice'
##o.some_property() #error
#o.some_property = "groovy" #calling some_property setter(<__main__.MyClass object at 0x7fb27d8f1048>,('groovy',),{})
#o.some_property #calling some_property getter(<__main__.MyClass object at 0x7fb27d8f1048>,(),{})
##                Out[34]: 'groovy'


class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

#a = A()
#b = B()
#c = C()
#d = D()
#e = E()

#a.go() #go A go!
#b.go() #go A go and go B go
#c.go() # A and C
#d.go() # A, C, B, and D
#e.go() # A, C, and B
#
#a.stop() # A
#b.stop() # A
#c.stop() # A and C
#d.stop() # A, C, D
#e.stop() # A, C
#
#a.pause() # Not implemented
#b.pause() # Not implemented
#c.pause() # Not implemented
#d.pause() # D
#e.pause() # Not implemented


class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

# specify output from here onwards

oRoot.print_all_1()
oRoot.print_all_2()







