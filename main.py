# TODO: implement from src.fuzzy import rank_window
from src.focus import focus_window
from src.windows import get_windows


def main():
    windows = get_windows()

    window_titles = enumerate([window.title for window in windows])

    for index, title in window_titles:
        print(index, title)

    while True:
        try:
            index = int(input("Choose a window by index: "))
            if 0 <= index < len(windows):
                break
            print(f"Enter a number between 0 and {len(windows) - 1}")
        except ValueError:
            print("Invalid input, enter a number")

    focus_window(windows[index])

    # query = input("Search: ")
    # results = rank_windows(windows, query)
    # if results:
    #     focus_window(results[0])


if __name__ == "__main__":
    main()