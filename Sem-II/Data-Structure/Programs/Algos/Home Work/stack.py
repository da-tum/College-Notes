# class = keyword used to create a new "blueprint" (a type) for objects
# StackADT = name of the class (we chose it because this class implements Stack Abstract Data Type)
class StackADT:

    # def = keyword to define a function/method
    # __init__ = special function (constructor) that runs automatically when an object is created
    # (self) = the current object itself (like "this" in other languages)
    def __init__(self):

        # self.data = a variable (attribute) stored inside the object
        # data = name of the attribute that will hold stack elements
        # = means assignment (store the right side into the left side)
        # [] = empty list in Python (we use list as stack storage)
        # # ... = comment (Python ignores comments)
        self.data = []  # list end will be the "top" of the stack

    # push = method name for inserting an element in stack
    # (self, x) -> x is the value we want to push
    def push(self, x):

        # self.data.append(x)
        # append = list function to add an item at the end of list
        # (x) = add the value x
        self.data.append(x)

    # pop = method name for removing top element from stack
    def pop(self):

        # if = decision keyword (checks a condition)
        # self.is_empty() = calling our own method to check if stack is empty
        # () means "call this function now"
        # : starts the block of code for if
        if self.is_empty():

            # return = send a value back to where the function was called
            # None = special value meaning "no value" / "nothing" in Python
            return None  # safe underflow (no crash when stack is empty)

        # return self.data.pop()
        # pop() (list method) removes and returns last element of list
        # since we treat end as top, this removes the stack top
        return self.data.pop()

    # peek = method name for seeing the top element without removing it
    def peek(self):

        # if stack is empty, peek should not crash
        if self.is_empty():

            # return None means "no top element exists"
            return None

        # return self.data[-1]
        # [-1] means last element of list (Python supports negative indexing)
        # -1 = last index, -2 = second last, etc.
        return self.data[-1]

    # is_empty = method that checks whether stack has 0 elements
    def is_empty(self):

        # return len(self.data) == 0
        # len(...) = built-in function to get number of elements in list
        # == = comparison operator (checks equality)
        # 0 = zero elements means empty
        return len(self.data) == 0

    # size = method that returns how many elements are in stack
    def size(self):

        # return len(self.data) gives the total element count
        return len(self.data)

    # display = method to show stack contents
    def display(self):

        # show stack from bottom to top (bottom is index 0, top is last)
        return self.data


# def = define a function (this is not inside class, so it's a normal function)
# reverse_string_using_stack = function name
# (s) = parameter; s will store the input string given by user
def reverse_string_using_stack(s):

    # st = variable name (short for stack)
    # StackADT() = creating a new stack object by calling class constructor
    st = StackADT()

    # for = loop keyword (repeat for each element)
    # ch = loop variable (will take each character one by one)
    # in = keyword used to iterate through items of a collection
    # s = the input string (strings are iterable character by character)
    # : starts the for-loop block
    for ch in s:

        # st.push(ch) pushes each character into stack
        st.push(ch)

    # rev = variable to store reversed string
    # "" = empty string
    rev = ""

    # while = loop keyword (runs again and again while condition is True)
    # not = logical operator that reverses True/False
    # st.is_empty() returns True if stack empty
    # not st.is_empty() means "loop until stack becomes empty"
    # : starts the while-loop block
    while not st.is_empty():

        # rev += st.pop()
        # += means "append/add and store back"
        # st.pop() removes top character from stack
        # adding popped characters builds reversed string
        rev += st.pop()

    # return rev sends the final reversed string back
    return rev


# main = function that runs the menu program (good practice to separate logic)
def main():

    # create one stack for menu operations
    st = StackADT()

    # while True = infinite loop (keeps menu running until we break)
    # True is a boolean value meaning "yes/continue"
    while True:

        # print() = built-in function to display output on screen
        # "\n" = newline character (moves cursor to next line)
        # --- STACK ADT MENU --- = text shown to user
        print("\n--- STACK ADT MENU ---")

        # printing menu options
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Size")
        print("6. Display Stack")
        print("7. Reverse a String (Meaningful Use)")
        print("0. Exit")

        # choice = variable to store user's choice
        # input(...) = built-in function to take input from keyboard as a string
        # "Enter your choice: " = message shown before taking input
        # .strip() = string method that removes leading/trailing spaces/newlines
        choice = input("Enter your choice: ").strip()

        # if = checks first condition
        # choice == "1" compares choice with string "1"
        # IMPORTANT: input() gives string, so we compare with "1" not 1
        if choice == "1":

            # val = user input value to push
            val = input("Enter value to push: ")

            # st.push(val) pushes value onto stack
            st.push(val)

            # print("Pushed:", val)
            # comma inside print prints items with space between them
            print("Pushed:", val)

        # elif = "else if" (checks next condition if previous if was false)
        elif choice == "2":

            # removed stores the returned value from pop()
            removed = st.pop()

            # if removed is None checks if pop failed (underflow)
            # is = identity operator (checks if it is exactly None object)
            if removed is None:
                print("Underflow! Stack is empty, cannot pop.")
            else:
                print("Popped:", removed)

        # elif choice == "3" handles peek
        elif choice == "3":

            # top gets top element from stack without removing
            top = st.peek()

            # if top is None means stack empty
            if top is None:
                print("Stack is empty, nothing to peek.")
            else:
                print("Top element:", top)

        # elif choice == "4" checks emptiness
        elif choice == "4":

            # st.is_empty() returns True/False
            print("isEmpty:", st.is_empty())

        # elif choice == "5" prints size of stack
        elif choice == "5":
            print("Size:", st.size())

        # elif choice == "6" shows the stack list
        elif choice == "6":
            print("Stack (bottom -> top):", st.display())

        # elif choice == "7" reverse string demo using stack
        elif choice == "7":

            # take a string from user
            s = input("Enter a string to reverse: ")

            # call reverse_string_using_stack(s) and print result
            print("Reversed string:", reverse_string_using_stack(s))

        # elif choice == "0" exit program
        elif choice == "0":
            print("Exiting... Goodbye!")

            # break = exits the nearest loop (here it stops while True)
            break

        # else = runs when none of above conditions matched
        else:
            print("Invalid choice. Try again.")


# if = condition check
# __name__ = special built-in variable in Python
# "__main__" = special string meaning "this file is being run directly"
# This block ensures main() runs only when we run this file,
# not when this file is imported into another file
if __name__ == "__main__":

    # calling main() to start the program
    main()