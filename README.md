# MP-1
# 🌐 Implementation of Browser Back Button Using Stack
> A simple Python-based Web Browser Simulator that demonstrates the use of a Stack data structure to implement browser navigation and browsing history management.

---

## 🎯 Objective

The main objective of this project is to understand and implement the **Stack data structure** in a real-world application. This project simulates the working of a web browser's Back Button using stack operations such as Push, Pop, and Peek.

It allows users to visit new webpages, navigate back to previously visited webpages, display the current webpage, and view browsing history.

---

## 📖 Introduction

A web browser allows users to visit different websites and navigate between previously visited pages. One of the most important features of a browser is the Back Button, which helps users return to the previous webpage.

The **Stack data structure** follows the **LIFO (Last In, First Out)** principle, meaning that the last element inserted is the first element removed. This makes a stack suitable for demonstrating browser back navigation.

In this project, a Python list is used to implement a stack. Whenever a user visits a new webpage, its URL is pushed onto the stack. When the user clicks the Back Button, the current webpage is popped from the stack, and the previous webpage becomes the current page.

The project provides a menu-driven interface that allows users to perform different browser operations interactively.

---

## ✨ Features

| Feature | Description |
|---|---|
| Visit New Webpage | Adds a webpage URL to the stack using the Push operation. |
| Back Button | Removes the current webpage using the Pop operation when a previous page exists. |
| Display Current Webpage | Displays the current webpage using the Peek operation. |
| Display Browsing History | Displays the webpages stored in the stack, starting with the most recently visited page. |
| Empty History Handling | Displays appropriate messages when the browser history is empty or no previous webpage is available. |
| Input Validation | Handles invalid menu input and prevents empty webpage URLs. |
| Menu-Driven Interface | Provides a simple interface for performing browser operations. |

---

## 🧩 Data Structure Used

### Stack

A Stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

In this project, a Python list is used to implement the stack.

**Stack operations used:**

- **Push:** Adds a newly visited webpage to the stack using `append()`.
- **Pop:** Removes the current webpage from the stack using `pop()`.
- **Peek:** Displays the current webpage using `stack[-1]`.
- **Display:** Shows all stored webpages in reverse order of insertion.

**Example:**

Suppose the user visits these webpages in order:

1. `www.google.com`
2. `www.youtube.com`
3. `www.github.com`

The stack will contain:

```text
Bottom → www.google.com
         www.youtube.com
Top    → www.github.com
```

When the user presses the Back Button, `www.github.com` is removed, and `www.youtube.com` becomes the current webpage.

---

## 💻 Technology Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code (VS Code)
- **Data Structure:** Stack
- **Python Concept:** Classes, Objects, Lists, Functions, Loops, Conditional Statements, Exception Handling, and User Input

---

## ⚙️ Operations

### 1. Visit New Webpage

The user enters a webpage URL. The URL is added to the top of the stack using the `append()` method.

### 2. Back Button

The program checks whether the stack contains more than one webpage. If so, the current webpage is removed using `pop()`, and the previous webpage is displayed.

If only one webpage remains, the program informs the user that no previous webpage is available.

### 3. Display Current Webpage

The program displays the webpage at the top of the stack without removing it.

### 4. Display Browsing History

The program displays all webpages stored in the stack, beginning with the most recently visited webpage.

### 5. Exit

The program terminates when the user selects the Exit option.

---

## ▶️ How to Run

1. Install Python on your computer.
2. Open Visual Studio Code.
3. Create a folder named `Browser-Back-Button-Using-Stack`.
4. Create a Python file named `main.py`.
5. Copy and paste the project code into `main.py`.
6. Open the VS Code terminal.
7. Execute the following command:

```bash
python main.py
```

8. Select an option from the menu and perform the desired browser operation.

---

## 📌 Learning Outcomes

- Understanding the Stack data structure and its LIFO principle.
- Learning how to implement Push, Pop, and Peek operations in Python.
- Understanding the practical application of stacks in browser navigation.
- Using Python classes and objects to organize program functionality.
- Implementing menu-driven programs using loops and conditional statements.
- Handling invalid input and empty-stack conditions.
- Understanding how browsing history can be represented using a stack.

---

## 🎓 Conclusion

The **Implementation of Browser Back Button Using Stack** project demonstrates how a fundamental data structure can be applied to a real-world computing problem.

By using a stack, the program efficiently simulates visiting webpages and navigating back to previously visited pages. It provides a clear understanding of the LIFO principle and the Push, Pop, and Peek operations.

This mini project strengthens practical knowledge of data structures and Python programming. It also provides a foundation for understanding more advanced browser navigation systems, including separate Back and Forward stacks.

---

### 👩‍💻 Developed as a Data Structures Mini Project

**Python | Stack | Web Browser Navigation | LIFO Principle**
