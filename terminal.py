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

    def print_note(self, message: str) -> None:
        """Print a notification message in green.

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        self.set_terminal_color("green")
        print("[NOTE] {}".format(message))
        self.reset()

    def print_warning(self, message: str) -> None:
        """Print a warning message in yellow.

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        self.set_terminal_color("yellow")
        print("[WARNING] {}".format(message))
        self.reset()

    def print_error(self, message: str) -> None:
        """Print an error message in red.

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        self.set_terminal_color("red")
        print("[ERROR] {}".format(message))
        self.reset()

    def cprint(self, message: str, color: Optional[str] = "default") -> None:
        """Print a message in the specified color.

        Args:
            message (str): The message to print.
            color (str, optional): The desired text color. Defaults to "default".

        Returns:
            None
        """
        if color in self.colors.keys():
            self.set_terminal_color(color)
            print(message)
            self.reset()
        else:
            self.set_terminal_color("red")
            print("[ERROR] Invalid color specified.")
            self.reset()

if __name__ == "__main__":
    # Terminal クラスのインスタンスを作成
    terminal = Terminal()

    # 通知メッセージ（緑色）を出力
    terminal.print_note("This is a notification message.")

    # 警告メッセージ（黄色）を出力
    terminal.print_warning("This is a warning message.")

    # エラーメッセージ（赤色）を出力
    terminal.print_error("This is an error message.")

    # カスタムカラーでメッセージを出力（例: 青色）
    terminal.cprint("This is a custom-colored message.", "blue")

    # 無効な色を指定した場合のエラーメッセージを出力
    terminal.cprint("This is an invalid color example.", "not_a_color")
