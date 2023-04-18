from typing import Optional

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "lightgray": "\033[37m",
    "default": "\033[39m",
    "darkgray": "\033[90m",
    "lightred": "\033[91m",
    "lightgreen": "\033[92m",
    "lightyellow": "\033[93m",
    "lightblue": "\033[94m",
    "lightmagenta": "\033[95m",
    "lightcyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m",
}


def set_terminal_color(color: str) -> None:
    """Set the terminal text color.
    Args:
        color (str): The desired text color.
    Returns:
        None
    Note:
        The text color will remain changed until reset() is called.
    """
    print("{}".format(COLORS[color]), end="")


def reset() -> None:
    """Reset the terminal text color to its default value.
    Args:
        None
    Returns:
        None
    """
    print("{}".format(COLORS["reset"]), end="")


def colored(message: str, color: Optional[str] = "default", end: str = "\n") -> None:
    """A context manager for setting and resetting the terminal color.
    Args:
        color (str, optional): The desired text color. Defaults to "default".
    Returns:
        None
    """

    if color in COLORS.keys():
        set_terminal_color(color)
        print(message, end=end)
        reset()
    else:
        print(message, end=end)


if __name__ == "__main__":
    colored("[NOTE] This is a notification message.", "green")
    colored("[WARNING] This is a warning message.", "yellow")
    colored("[ERROR] This is an error message.", "red")
    colored("This is a custom-colored message.", "blue")
    colored("[ERROR] Invalid color specified.", "not_a_color")

    words = [
        ("Hello", "lightblue"),
        ("beautiful", "lightmagenta"),
        ("world!", "lightgreen"),
    ]

    for index, (word, color) in enumerate(words):
        if index == len(words) - 1:
            colored(word, color)
        else:
            colored(word, color, end=" ")
