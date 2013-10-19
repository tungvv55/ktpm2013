__author__='VUTUNG'
from input import *
import collections
import unittest
import itertools
#get number in docstring
def get_value(string):
    lines=string.expandtabs().splitlines()
    k = []
    a = len(lines)
    for c in range(1,a-1):
        s = "".join(x if x.isdigit() else " " for x in lines[c])
        digitStrings = s.split()
        numbers = map(int, digitStrings)
        k.append(numbers)
    return k
#check number value in row
def check_value(arr):
    a = []
    for i in range(len(arr)):
        a.append(len(arr[i]))
        if (a[i]%2!=0) or (a[i] == 0) or (a[i]>6) or (len(arr)>10):
            raise Exception, "Wrong input"
            break
    return True
#check classes equivalence
def check_equivalence(arr):
    if check_value(arr):
        d = []
        for a in range(0,len(arr)):
            o = []
            for b in range(0,len(arr[a]),2):
                o.extend(range(arr[a][b],arr[a][b+1]+1))
            d.append(o)
            y=collections.Counter(d[a])
            if len(([i for i in y if y[i]>1])) > 0:
                raise Exception, "Wrong input"
                break
        return True
#get input of list
def get_input(arr):
    if check_equivalence(arr):
        d = []
        for i in range(0,len(arr)):
            o = []
            for j in range(0,len(arr[i]),2):
                z = (arr[i][j]+ arr[i][j+1])/2
                o.append(z)
            d.append(o)
        return d
#class test case
class MainTest(unittest.TestCase):
    pass

# function to generate test cases
def test_generator(params):
    def wrapper(func, args):
        func(*args)
    paramsLen = len(params)
    def test(self):
        try:
            if (paramsLen == 0):
                result = main()
                self.assertEquals(result,result)

            elif (paramsLen > 0):
                a = []
                for i in range(0,paramsLen):
                    a.append(params[i])
                result = wrapper(main, a)
                self.assertEquals(result,result)
        except:
            self.fail("Raised an exception.")
    return test

# run test
if __name__ == '__main__':
    input = get_input(get_value(main.__doc__))
    output = list(itertools.product(*input))
    print "Generating test cases..."
    i = 0
    for arr in output:
        i = i + 1
        test_name = 'test_%d' % i
        test = test_generator(arr)
        setattr(MainTest, test_name, test)
    print "Running test..."
    unittest.main()