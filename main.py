from loading.bouncing_ball import bouncing_ball
from loading.dots_loading import dots_loading
from loading.growing_bar import growing_bar
from loading.progress_bar import loading_bar
from loading.sliding_arrow_loading import sliding_arrow_loading
from loading.spinner_loading import spinner_loading
from loading.star_dot_loading import star_dot_loading


def main():
    loading_types = {
        "Progress Bar": loading_bar,
        "Bouncing Ball": bouncing_ball,
        "Growing Bar": growing_bar,
        "Dots Loading": dots_loading,
        "Spinner Loading": spinner_loading,
        "Star Dot Loading": star_dot_loading,
        "Sliding Arrow Loading": sliding_arrow_loading
    }

    loading_list = list(loading_types.items())

    try:
        while True:
            print("\nSelect a loading type:")
            for idx, (name, _) in enumerate(loading_list, 1):
                print(f"  {idx}. {name}")

            choice = input("Enter number (or name, or 'exit' to quit): ").strip().lower()

            if choice == "exit":
                print("Exiting...")
                break

            # Try by number
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(loading_list):
                    _, func = loading_list[index]
                    func()
                    continue

            # Try by name
            for name, func in loading_list:
                if choice == name.lower():
                    func()
                    break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
