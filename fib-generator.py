def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


if __name__ == "__main__":
    f = fibonacci()
    print("Initial: 0, 1")
    for _ in range(10):
        print(next(f))
