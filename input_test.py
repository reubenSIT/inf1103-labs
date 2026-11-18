
from input_helper import get_positive_float


def main() -> None:
    price = get_positive_float("Enter product price: $")
    print(f"Accepted price: ${price:.2f}")


if __name__ == "__main__":
    main()
