__author__ = 'VUTUNG'
import math
def checkInput(a,b,c):
    if(a is None or b is None or c is None):
        return "False"
    else:
        return "True"
def Triangle(a='',b='',c=''):

        if ((a != '') and (b != '') and (c != '')):
            if(isinstance(a,float) and isinstance(b,float) and isinstance(c,float)):
                if (a+b>c) and (a+c>b) and (b+c>a):
                    if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c ==  a*a):
                        if(a==b) or (b==c) or (c==a):
                            return "isosceles right-angled"
                        else:
                            return "isosceles"
                    elif (a==b) and (b==c) and (c==a):
                        return "equilateral"
                    elif (a==b) or (b==c) or (c==a):
                        return "right-angled"
                    else:
                        return "normal"
                else:
                    return "Not Triangle"
            else:
                return "Wrong value(not interger)"
        else:
            return "Null Value"
