import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

# Make a list of threads that are started.
threads = []

for _ in range(10):
    # For passing arguments to a function, need to use
    # args = [], and pass the arguments as a list.
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    # Cannot do a join() here. It will run
    # synchronously.
    threads.append(t)

# Individually end each thread execution.
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')