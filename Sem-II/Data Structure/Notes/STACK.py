class StackADT:
    def __init__(self):
        self.data = []  # list end will be the "top" of the stack

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            return None  # safe underflow
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def display(self):
        return self.data


def reverse_string_using_stack(s):
    st = StackADT()
    for ch in s:
        st.push(ch)
    rev = ""
    while not st.is_empty():
        rev += st.pop()
    return rev


def main():
    st = StackADT()
    while True:
        print("\n--- STACK ADT MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Size")
        print("6. Display Stack")
        print("7. Reverse a String (Meaningful Use)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            val = input("Enter value to push: ")
            st.push(val)
            print("Pushed:", val)

        elif choice == "2":
            removed = st.pop()
            if removed is None:
                print("Underflow! Stack is empty, cannot pop.")
            else:
                print("Popped:", removed)

        elif choice == "3":
            top = st.peek()
            if top is None:
                print("Stack is empty, nothing to peek.")
            else:
                print("Top element:", top)

        elif choice == "4":
            print("isEmpty:", st.is_empty())

        elif choice == "5":
            print("Size:", st.size())

        elif choice == "6":
            print("Stack (bottom -> top):", st.display())

        elif choice == "7":
            s = input("Enter a string to reverse: ")
            print("Reversed string:", reverse_string_using_stack(s))

        elif choice == "0":
            print("Exiting Programme.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
