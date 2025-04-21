def bresenham_circle(h: int, k: int, r: int) -> None:
    """Implements Bresenham's circle drawing algorithm."""
    
    x, y = 0, r
    p = 1 - r

    plot_octants(h, k, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1

        plot_octants(h, k, x, y)


def plot_octants(h: int, k: int, x: int, y: int) -> None:
    """Plots the symmetric points of the circle in all eight octants."""

    points = [
        (x, y), (-x, y),
        (x, -y), (-x, -y),
        (y, x), (-y, x),
        (y, -x), (-y, -x)
    ]

    for px, py in points:
        print(f"{px:^10} | {py:^10}")
    
def get_coordinates(prompt: str) -> tuple[int, int]:
    """Prompts the user to input circle coordinates."""
    while True:
        try:
            return tuple(map(int, input(prompt).strip().split()))
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")



def main() -> None:
    """Main execution function."""
    h, k = get_coordinates("Enter center of cirlce (h, k): ")
    r = int(input("Enter radius of circle(r): ").strip())

    print("\nStarting Bresenham's Circle Algorithm...")
    print(" X-Coords  |  Y-Coords ")
    print('-' * 21)

    bresenham_circle(h, k, r)


if __name__ == "__main__":
    main()