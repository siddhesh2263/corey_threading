import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# No parenthesis after function name, since it is not
# to be run. It is to be passed.
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# The join() makes sure the above threads are completed
# execution, and only then will move to the next line.
t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')