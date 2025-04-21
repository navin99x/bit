def bresenham_line(x0: int, y0: int, x1: int, y1: int) -> None:
    """Implements Bresenham's line drawing algorithm."""
    
    # Calculate differences
    del_x = abs(x1 - x0)
    del_y = abs(y1 - y0)
    
    # Determine the step direction for x and y
    step_x = 1 if x1 > x0 else -1
    step_y = 1 if y1 > y0 else -1
    
    # Initialize decision parameter
    p = 2 * del_y - del_x
    x, y = x0, y0

    while x != x1:
        plot(x, y)
        if p < 0:
            p += 2 * del_y
        else:
            y += step_y
            p += 2 * del_y - 2 * del_x
        x += step_x
        
    plot(x1, y1)


def plot(x: int, y: int) -> None:
    """Prints a single point on the line."""
    print(f"{x:^10} | {y:^10}")


def get_coordinates(prompt: str) -> tuple[int, int]:
    """Prompts the user to input 2D coordinates."""
    while True:
        try:
            return tuple(map(int, input(prompt).strip().split()))
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")


def main() -> None:
    """Main execution function."""
    x0, y0 = get_coordinates("Enter starting coordinates (x y): ")
    x1, y1 = get_coordinates("Enter ending coordinates (x y): ")

    print("\nStarting Bresenham's Algorithm...")
    print(" X-Coords  |  Y-Coords ")
    print('-' * 21)

    bresenham_line(x0, y0, x1, y1)


if __name__ == "__main__":
    main()