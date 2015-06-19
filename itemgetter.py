

import random
import string
import pprint
from operator import itemgetter

# data = [
    # {'age': 31, 'city': 'taipei', 'name': 'amy'},
    # {'age': 71, 'city': 'tokyo', 'name': 'john'},
    # {'age': 16, 'city': 'london', 'name': 'zoe'},
    # {'age': 16, 'city': 'rio', 'name': 'cathy'},
    # {'age': 48, 'city': 'frankfurt', 'name': 'david'}]
# pprint.pprint(data)
# pprint.pprint(sorted(data, key=lambda x: x['age']))
# pprint.pprint(sorted(data, key=lambda x: (x['age'], x['name'])))

####
    
def random_str(size_lower=3, size_upper=10):
    size = random.randint(size_lower, size_upper)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

def random_data(size):
    result = []
    for _ in range(size):
        d = {}
        d['age'] = random.randint(1, 99)
        d['name'] = random_str() 
        d['city'] = random_str() 
        result.append(d)
    return result

DATA_SIZE = 10000
data = random_data(DATA_SIZE)

def test_lambda():
    data0 = sorted(data, key=lambda x: x['age'])
    data1 = sorted(data, key=lambda x: x['name'])
    data2 = sorted(data, key=lambda x: x['city'])
    data3 = sorted(data, key=lambda x: (x['age'], x['name']))
    data4 = sorted(data, key=lambda x: (x['age'], x['city']))
    
def test_itemgetter():
    data0 = sorted(data, key=itemgetter('age'))
    data1 = sorted(data, key=itemgetter('name'))
    data2 = sorted(data, key=itemgetter('city'))
    data3 = sorted(data, key=itemgetter('age', 'name'))
    data4 = sorted(data, key=itemgetter('age', 'city'))
    
if __name__ == '__main__':
    from timeit import Timer
    TEST_COUNT = 100
    t_lambda = Timer('test_lambda()', 'from __main__ import test_lambda')
    print('lambda: ', t_lambda.timeit(TEST_COUNT))
    t_itemgetter = Timer('test_itemgetter()', 'from __main__ import test_itemgetter')
    print('itemgetter: ', t_itemgetter.timeit(TEST_COUNT))
    

