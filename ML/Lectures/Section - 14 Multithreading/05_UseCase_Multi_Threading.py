"""Real-World Example: Multithreading for I/O-bound Tasks

Scenario: Web Scraping

Web scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O-bound because they spend a lot of time waiting for
responses from servers. Multithreading can significantly improve the
performance by allowing multiple web pages to be fetched concurrently."""

# https://realpython.com/python-concurrency/#real-world-example-multithreading-for-io-bound-tasks
# https://realpython.com/python-concurrency/#real-world-example-multiprocessing-for-cpu-bound-tasks
# https://realpython.com/python-concurrency/#real-world-example-asyncio-for-io-bound-tasks
# https://realpython.com/python-concurrency/#real-world-example-multiprocessing-and-concurrency

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://realpython.com/python-concurrency/#real-world-example-multithreading-for-io-bound-tasks',
    'https://realpython.com/python-concurrency/#real-world-example-multiprocessing-for-cpu-bound-tasks',
    'https://realpython.com/python-concurrency/#real-world-example-asyncio-for-io-bound-tasks',
    'https://realpython.com/python-concurrency/#real-world-example-multiprocessing-and-concurrency',
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Main Thread Finished')