

from config import SERVER_ADDR
import requests, json
from engine.retrieval import retrieval

import datetime

import warnings
warnings.filterwarnings("ignore")

testdata = [
"069.Rufous_Hummingbird/Rufous_Hummingbird_0011_59480.jpg",
"069.Rufous_Hummingbird/Rufous_Hummingbird_0011_59480.jpg",
"069.Rufous_Hummingbird/Rufous_Hummingbird_0011_59480.jpg",
"069.Rufous_Hummingbird/Rufous_Hummingbird_0011_59480.jpg"
]

def netSearch(d_l_i_s_t):
    d = json.dumps({
        'data': d_l_i_s_t,
    })
    res = requests.post(SERVER_ADDR, data=d)
    res = eval(res.text)
    return eval(res['res'])

def engine(retrieval_image_keys):
    dataset_root = '/Users/thatslc/Downloads/CUB_200_2011/CUB_200_2011'
    engine = retrieval(dataset_root, verbose=False)
    return engine.retrival_from_image_root(retrieval_image_keys)

print("TEST", len(testdata), " imgs:")
t = datetime.datetime.now()
#(engine(testdata) )
t2 = datetime.datetime.now()
print( "Loc(CPU)", (t2 - t).seconds, '.', round((t2 - t).microseconds/1000, 0), 'm' )

t = datetime.datetime.now()
print(netSearch(testdata) )
t2 = datetime.datetime.now()
print( "Net(GPU)", (t2 - t).seconds, '.', round((t2 - t).microseconds/1000, 0), 's' )

