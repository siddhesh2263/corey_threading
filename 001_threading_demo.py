import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# CPU bound and IO bound tasks. Check examples. No use of
# using threads in this kind of scenarios. The above code
# example runs synchronously.