"""JSON, CSV, and streaming large files"""
import json, csv
from pathlib import Path

def write_json(path):
    data = {'a':1,'b':[1,2,3]}
    Path(path).write_text(json.dumps(data))

def read_csv(path):
    with open(path,newline='') as f:
        r = csv.DictReader(f)
        for row in r:
            yield row

if __name__ == '__main__':
    write_json('06_file_io_data/sample.json')
    print('json ->', Path('06_file_io_data/sample.json').read_text())
    # create csv
    p = '06_file_io_data/sample.csv'
    with open(p,'w',newline='') as f:
        f.write('name,amt\nA,10\nB,20\n')
    for r in read_csv(p):
        print(r)
