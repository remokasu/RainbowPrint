from contextlib import contextmanager
from typing import Optional


class Terminal:
    """A class for colorizing text output to the terminal.

    Attributes:
        colors (dict): A dictionary of available colors.
    """

    def __init__(self):
        self.colors = {
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

    def set_terminal_color(self, color: str) -> None:
        """Set the terminal text color.
        Args:
            color (str): The desired text color.
        Returns:
            None
        Note:
            The text color will remain changed until reset() is called.
        """
        print("{}".format(self.colors[color]), end="")

    def reset(self) -> None:
        """Reset the terminal text color to its default value.
        Args:
            None
        Returns:
            None
        """
        print("{}".format(self.colors["reset"]), end="")

    @contextmanager
    def colored(self, color: Optional[str] = "default"):
        """A context manager for setting and resetting the terminal color.
        Args:
            color (str, optional): The desired text color. Defaults to "default".
        Returns:
            None
        """
        try:
            self.set_terminal_color(color)
            yield
        finally:
            self.reset()

    def print_colored(self, message: str, color: Optional[str] = "default", end: str = "\n") -> None:
        """Print a message in the specified color.
        Args:
            message (str): The message to print.
            color (str, optional): The desired text color. Defaults to "default".
            end (str, optional): The string appended after the last value, defaults to newline.
        Returns:
            None
        Raises:
            ValueError: If an invalid color is specified.
        """
        if color in self.colors.keys():
            with self.colored(color):
                print(message, end=end)
        else:
            with self.colored():
                print(message, end=end)


if __name__ == "__main__":
    # Terminal クラスのインスタンスを作成
    terminal = Terminal()

    # 通知メッセージ（緑色）を出力
    terminal.print_colored("[NOTE] This is a notification message.", "green")

    # 警告メッセージ（黄色）を出力
    terminal.print_colored("[WARNING] This is a warning message.", "yellow")

    # エラーメッセージ（赤色）を出力
    terminal.print_colored("[ERROR] This is an error message.", "red")

    # カスタムカラーでメッセージを出力（例: 青色）
    terminal.print_colored("This is a custom-colored message.", "blue")

    # 無効な色を指定した場合のエラーメッセージを出力
    terminal.print_colored("[ERROR] Invalid color specified.", "not_a_color")

    words = [
        ("Hello", "lightblue"),
        ("beautiful", "lightmagenta"),
        ("world!", "lightgreen"),
    ]

    for index, (word, color) in enumerate(words):
        if index == len(words) - 1:
            terminal.print_colored(word, color)
        else:
            terminal.print_colored(word, color, end=" ")
