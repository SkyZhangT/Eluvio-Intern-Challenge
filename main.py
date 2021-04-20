import sys
import time
from LRUcache import LRU
from utils import API_GET
from LFUcache import LFU
from concurrent.futures import ThreadPoolExecutor


if __name__ == "__main__":
    '''
    argv[1]: input file name
    argv[2]: cache type
    argv[3]: cache capacity
    '''
    s = time.time()

    cache = None
    if sys.argv[2] == "LRU":
        cache = LRU(int(sys.argv[3]))
    elif sys.argv[2] == "LFU":
        cache = LFU(int(sys.argv[3]))
    
    
    processes = []
    with open(sys.argv[1], 'r') as inputfile:
        with ThreadPoolExecutor(max_workers=5) as executor:
            for line in inputfile:
                line = line.replace("\n", "")

                # check if in the cache, create new thread if not in
                if not cache.get(line):
                    cache.put(line)
                    processes.append(executor.submit(API_GET, line))
                
    result = []
    for p in processes:
        result.append(p.result())

    print(f"Total time used is {time.time() - s}")


            
