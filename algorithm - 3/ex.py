import random
import string

def generarId():
    def random_string():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    
    id_pattern = '{}-{}-{}-{}'.format(random_string(), random_string(), random_string(), random_string())
    return id_pattern

id = generarId()
print("Generated ID:", id)