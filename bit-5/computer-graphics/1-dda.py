def dda(x0: int, y0: int, x1: int, y1: int) -> None:
    """Implements the Digital Differential Analyzer (DDA) line drawing algorithm."""
    delta_x = x1 - x0
    delta_y = y1 - y0

    steps = max(abs(delta_x), abs(delta_y))

    if steps == 0:
        plot(x0, y0)
        return

    x_increment = delta_x / steps
    y_increment = delta_y / steps

    x, y = x0, y0

    for _ in range(steps + 1):
        plot(round(x), round(y))
        x += x_increment
        y += y_increment


def plot(x: int, y: int) -> None:
    """Prints a single point on the line."""
    print(f"{str(x):^10} | {str(y):^10}")


def get_coordinates(prompt: str) -> tuple[int, int]:
    """Prompts the user to input 2D coordinates."""
    while True:
        try:
            return tuple(map(int, input(prompt).strip().split()))
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")


def main() -> None:
    """Main execution function."""
    x0, y0 = get_coordinates("Enter starting coordinates (x y): ")
    x1, y1 = get_coordinates("Enter ending coordinates (x y): ")

    print("\nStarting DDA Algorithm...")
    print(" X-Coords  |  Y-Coords ")
    print('-' * 21)
    
    dda(x0, y0, x1, y1)


if __name__ == "__main__":
    main()
