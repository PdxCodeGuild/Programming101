# Terminal Cheatsheet

The following commands will work in Mac and Linux terminals as well as Windows PowerShell.

## Terminal Navigation

| Action                    | Command                       |
| ------------------------- | ----------------------------- |
| Display current directory | `pwd`                         |
| Show directory contents   | `ls`                          |
| Change directory          | `cd <directory_name>`         |
| Go up a directory         | `cd ..`                       |
| Create a directory        | `mkdir <directory_name>`      |
| Delete a directory        | `rm -r <directory_name>`      |
| Move a file or folder     | `mv <filename> <destination>` |
| Cancel current operation  | `ctrl + C` / `Command + C`    |

## Python in the Terminal

Each operating system has a different shortcut for running Python's `.py` files in the terminal.

| Command                 | Mac      | Linux    | Windows  |
| ----------------------- | -------- | -------- | -------- |
| `py <filename>.py`      | &#10007; | &#10007; | &#10003; |
| `python3 <filename>.py` | &#10003; | &#10003; | &#10007; |
| `python <filename>.py`  | &#10007; | &#10003; | &#10007; |

When these commands are run without a `filename`, the **Python** **_interpreter_** will run in the terminal.
