def print_gugudan(dan):
    """Print the multiplication table for the given number (dan)."""
    print(f"\n {dan}단 ")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")


def main():
    dan = int(input("몇단을 입력할까요? "))
    print_gugudan(dan)


if __name__ == "__main__":
    main()