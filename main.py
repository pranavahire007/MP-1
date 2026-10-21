# Implementation of Browser Back Button Using Stack

class Browser:
    def __init__(self):
        self.stack = []

    # Visit a new webpage (Push operation)
    def visit_page(self, url):
        self.stack.append(url)
        print("Webpage visited successfully:", url)

    # Go back to the previous webpage (Pop operation)
    def back_button(self):
        if len(self.stack) > 1:
            self.stack.pop()
            print("Navigated back successfully.")
            print("Current webpage:", self.stack[-1])
        elif len(self.stack) == 1:
            print("No previous webpage available.")
        else:
            print("Browser history is empty.")

    # Display the current webpage (Peek operation)
    def current_page(self):
        if self.stack:
            print("Current webpage:", self.stack[-1])
        else:
            print("No webpage is currently open.")

    # Display browsing history
    def show_history(self):
        if self.stack:
            print("\nBrowsing History:")
            for page in reversed(self.stack):
                print(page)
        else:
            print("Browsing history is empty.")


def main():
    browser = Browser()

    while True:
        print("\n===== WEB BROWSER MENU =====")
        print("1. Visit New Webpage")
        print("2. Back Button")
        print("3. Display Current Webpage")
        print("4. Display Browsing History")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            url = input("Enter webpage URL: ").strip()

            if url:
                browser.visit_page(url)
            else:
                print("URL cannot be empty.")

        elif choice == 2:
            browser.back_button()

        elif choice == 3:
            browser.current_page()

        elif choice == 4:
            browser.show_history()

        elif choice == 5:
            print("Exiting Web Browser Simulator.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()