__author__ = 'VUTUNG'
import math
s = (10**-10)
def detect_triangle(a='',b='',c=''):
        if ((a != '') and (b != '') and (c != '')):
            if (isinstance(a,float) or isinstance(a,int)) and (isinstance(b,float) or isinstance(b,int)) and (isinstance(c,float) or isinstance(c,int)):
                a=float(a)
                b=float(b)
                c=float(c)
                if (a+b>c) and (a+c>b) and (b+c>a):
                    if abs((a**2+b**2)-(c**2)) < s or abs((c**2+a**2)-(b**2)) < s or abs((c**2+b**2)-(a**2)) < s:
                        if(a==b) or (b==c) or (c==a):
                            return "isosceles right-angled"
                        else:
                            return "right-angled"
                    elif (a==b) and (b==c) and (c==a):
                        return "equilateral"
                    elif (a==b) or (b==c) or (c==a):
                        return "isosceles"
                    else:
                        return "normal"
                else:
                    return "Not Triangle"
            else:
                return "Wrong value(not float)"
        else:
            return "Null Value"
