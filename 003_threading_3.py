import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# Make a list of threads that are started.
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    # Cannot do a join() here. It will run
    # synchronously.
    threads.append(t)

# Individually end each thread execution.
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')