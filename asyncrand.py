# python3 asyncrand.py
import asyncio, random

# ANSI colors for colorized output
c = (
    "\033[0m",  # End of color <- reset to default
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def make_random(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(
            c[idx + 1]
            + f"makerandom({idx})=={i} too low; retrying after {idx + 1} seconds."
        )
        await asyncio.sleep(idx + 1)
        # asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"-------> Finished: makerandom({idx})=={i}" + c[0])
    return i


async def main():
    # res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    res = await asyncio.gather(
        (make_random(0, 9)), (make_random(1, 8)), (make_random(2, 7))
    )
    # res -> variable to hold result
    # await -> required to get the result from coroutines
    # asyncio.gather -> async controller/event loop/coordinator
    # (*(make_random())) -> * for unpacking; ?
    # make_random(i, 10 - i - 1) for i in range(3) -> ternary for loop for 3
    # function calls
    return res


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f"\nr1: {r1}, r2: {r2}, r3: {r3}")
