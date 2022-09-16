import datetime
import tracemalloc
import petl as etl 
import pandas as pd 


def etll():

    begin_time = datetime.datetime.now()
    td = etl.fromjson('big.jsonl', lines=True)
    a=td[1050]
    b=td[12045]
    
    print(datetime.datetime.now()-begin_time)
def checketl():
    tracemalloc.start()
    etll()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    print(45358456/320148)

def pdd():
    begin_time = datetime.datetime.now()
    with open('big.jsonl') as f:
        lines = f.read().splitlines()
    td = pd.DataFrame(lines)
    a=td.iloc[1049]
    b=td.iloc[12044]
    
    print(datetime.datetime.now()-begin_time)

def checkpd():
    tracemalloc.start()
    pdd()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
if __name__ == '__main__':
    checketl()
    checkpd()

