"""Extra functions of user app"""

import random
import string


def code_generator(size=6, chars=string.ascii_uppercase + string.digits ):
    """function to create a random code string upper case and plane text """
    return ''.join(random.choice(chars) for _ in range(size))