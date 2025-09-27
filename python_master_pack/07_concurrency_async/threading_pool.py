"""Threading and ThreadPoolExecutor example"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def work(x):
    time.sleep(0.1)
    return x*x

def run():
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(work,i) for i in range(8)]
        for f in as_completed(futures):
            print('got', f.result())

if __name__ == '__main__':
    run()
