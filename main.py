import sys
import time
from LRUcache import LRU
from utils import API_GET
from LFUcache import LFU


if __name__ == "__main__":
    result = dict()
    cache = None
    if sys.argv[2] == "LRU":
        cache = LRU(int(sys.argv[3]))
    elif sys.argv[2] == "LFU":
        cache = LFU(int(sys.argv[3]))


    with open(sys.argv[1], 'r') as inputfile:
        start_time = time.time()
        count = 0
        for i, line in enumerate(inputfile):
            line = line.replace("\n", "")

            print("----------------------------")
            print(line)
            print(cache.cache)

            if not cache.get(line):
                API_GET(line)
                cache.put(line)
                count += 1

            if count == 5:
                print(f'{count}, check')
                duration = time.time() - start_time
                if duration < 1:
                    time.sleep(1 - duration)
                start_time = time.time()
                count = 0

            
