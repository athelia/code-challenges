import asyncio, time


# count() is a standard API (Python 3.7+) coroutine, since introduced with `async`
async def count():
    print("One")
    # Ceding control back to the caller - the coordinator
    # Here asyncio.sleep() is standing in for a long-running function
    await asyncio.sleep(1)
    print("Two")


# main() is a coroutine also
async def main():
    # This is the control loop/coordinator.
    # To use a coroutine, we have to `await` the calls to get the results.
    # Any f() we await must be awaitable: either a coroutine or with an
    # .__await__() method returning an iterator.
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
