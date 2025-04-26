
# Python Loading Animations

This project provides several different types of loading animations implemented in Python. The user can select a loading type, and the program will display the corresponding animation in the terminal.

## Features

- **Progress Bar**: Displays a progress bar that fills up to 100%.
- **Bouncing Ball**: A bouncing ball animation.
- **Growing Bar**: A bar that gradually fills up with dots to represent progress.
- **Dots Loading**: A simple dot loading animation.
- **Spinner Loading**: A spinning animation with different rotation states.
- **Star Dot Loading**: A star-based dot loading animation.
- **Sliding Arrow Loading**: An arrow sliding across the terminal to indicate progress.

## Installation

To use this program, make sure you have Python 3.x installed on your machine.

Clone or download the repository to your local system.

## Usage

1. Navigate to the project directory:

    ```bash
    cd path/to/project
    ```

2. Run the program:

    ```bash
    python main.py
    ```

3. You will be prompted to select a loading type by entering the corresponding number or name. To exit the program, type `exit`.

    ### Example Output:
    ```
    Select a loading type:
      1. Progress Bar
      2. Bouncing Ball
      3. Growing Bar
      4. Dots Loading
      5. Spinner Loading
      6. Star Dot Loading
      7. Sliding Arrow Loading
    Enter number (or name, or 'exit' to quit): 1
    ████████████████████████████████████████ 100%

    Select a loading type:
      1. Progress Bar
      2. Bouncing Ball
      3. Growing Bar
      4. Dots Loading
      5. Spinner Loading
      6. Star Dot Loading
      7. Sliding Arrow Loading
    Enter number (or name, or 'exit' to quit): 2
                    ●
    ```

4. You can continue selecting different loading types or exit the program by typing `exit`.

---

### Available Loading Types:

1. **Progress Bar**
   - A simple progress bar that fills up with `█` symbols to represent the progress.

2. **Bouncing Ball**
   - A ball that "bounces" around the terminal with the symbol `●`.

3. **Growing Bar**
   - A bar that grows from `[....................]` to a full completion.

4. **Dots Loading**
   - An animation where dots appear and disappear in sequence.

5. **Spinner Loading**
   - A spinning animation with a rotating cursor (`\`, `|`, `/`, `-`).

6. **Star Dot Loading**
   - A dot-based loading animation using stars (`*`).

7. **Sliding Arrow Loading**
   - An arrow (`=>`) that slides across the terminal to indicate progress.

## Example Usage:

```
Select a loading type:
  1. Progress Bar
  2. Bouncing Ball
  3. Growing Bar
  4. Dots Loading
  5. Spinner Loading
  6. Star Dot Loading
  7. Sliding Arrow Loading
Enter number (or name, or 'exit' to quit): 1
████████████████████████████████████████ 100%

Select a loading type:
  1. Progress Bar
  2. Bouncing Ball
  3. Growing Bar
  4. Dots Loading
  5. Spinner Loading
  6. Star Dot Loading
  7. Sliding Arrow Loading
Enter number (or name, or 'exit' to quit): exit
Exiting...
```

## Contributing

Feel free to open issues or pull requests if you encounter any problems or have suggestions for improvements. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
