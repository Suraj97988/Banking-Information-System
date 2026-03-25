# Name Validation
from BankExcept import *

def validate(name):
    if name.isspace():
        raise SpaceError
    else:
        words = name.split()
        if len(words) == 0:
            raise EmptyNameError
        else:
            for word in words:
                if not word.isalpha():
                    raise InvalidNameError

            return " ".join(words)
            # res = True
            # for word in words:
            #     if not word.isalpha():
            #         res = False
            #         break
            #     if res:
            #         return " ".join(words)
            #     else:
            #         raise InvalidNameError

