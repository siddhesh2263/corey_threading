import requests
import time
import random
import string
import concurrent.futures

image_urls = [
    'https://images.pexels.com/photos/3573351/pexels-photo-3573351.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/66869/green-leaf-natural-wallpaper-royalty-free-66869.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/192136/pexels-photo-192136.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/1407305/pexels-photo-1407305.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/886521/pexels-photo-886521.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/158780/leaf-nature-green-spring-158780.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/1072179/pexels-photo-1072179.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/212324/pexels-photo-212324.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/957024/forest-trees-perspective-bright-957024.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/1353938/pexels-photo-1353938.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/35196/water-plant-green-fine-layers.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/64296/pexels-photo-64296.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/409696/pexels-photo-409696.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/38012/pexels-photo-38012.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/40896/larch-conifer-cone-branch-tree-40896.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
]

def name_generator():
    digits = "".join( [random.choice(string.digits) for i in range(8)] )
    chars = "".join( [random.choice(string.ascii_letters) for i in range(15)] )
    name = digits + chars
    return name

t1 = time.perf_counter()

def download_image(image_url):
    image_bytes = requests.get(image_url).content
    image_name = name_generator()
    image_name = f'{image_name}.jpg'
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print(f'{image_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    # The map() function will run each url in the list
    # with the download_image function. Because we are
    # using the ThreadPoolExecutor, it will download each
    # image using different thread. This will make the requests
    # asynchronously.
    executor.map(download_image, image_urls)

t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds.')

# Threads wouldn't be ideal where a lot of computation
# is involved. If there are operations that involve
# image resizing, etc., threading would not speed up
# the process by that much. That would be an example of
# something that is CPU bound, and not IO bound. In those
# scenarios, threads can slow down the script, because threads
# involve some overhead when they are created and destroyed. So,
# given the case, we need to decide whether we need to go with
# threading, or multiprocessing.