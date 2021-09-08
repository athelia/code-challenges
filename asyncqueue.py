# asyncqueue.py
import asyncio, os, random, time
import itertools as it

async def make_item(size: int = 5) -> str:
    # create a random hex string from a bytes object
    return os.urandom(size).hex()

async def rand_sleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f'{caller} sleeping for {i} seconds.')
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    # creates an iterator that returns obj (None) n times
    for _ in it.repeat(None, n): # synchronous loop for each single producer
        # why not use for _ in range?
        await rand_sleep(caller=f'Producer {name}')
        i = await make_item()
        t = time.perf_counter() # performance counter for benchmarking
        await q.put((i, t)) # put tuple in queue -> (item, start_time)
        print(f'Producer {name} added <{i}> to queue.')

async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await rand_sleep(caller=f'Consumer {name}')
        i, t = await q.get() # .get() -> remove and return an item from queue
        # and unpack the tuple
        now = time.perf_counter()
        print(f'Consumer {name} got element <{i}> in {now-t:0.5f} seconds.')
        q.task_done() #.task_done() -> indicate to queue that task complete

async def main(nprod: int, ncon: int) -> None:
    q = asyncio.Queue()
    # .create_task() -> schedule the execution of a coroutine object in a spawn task
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers) # unpack producers as arguments for .gather()
    await q.join() # implicitly awaits consumers #how???
    # .join() -> blocks until queue is empty (maintains a counter for added/done)
    for c in consumers:
        c.cancel() # .cancel() -> request that a task cancel itself

if __name__ == '__main__':
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--nprod', type=int, default=5)
    parser.add_argument('-c', '--ncon', type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f'Program completed in {elapsed:0.5f} seconds.')