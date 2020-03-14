import sys


def oneMapping(s, t):
        if(len(set(s)) < len(set(t))):
                return False
        elif (len(set(s)) != len(set(s))):
                return False
        else:
                return True


print(oneMapping(sys.argv[1],sys.argv[2]))
