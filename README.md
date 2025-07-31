# 📚 DesignPatternLibrary

This project demonstrates the usage of several classic **Design Patterns** through a library system that allows borrowing and returning books with different behaviors and rules.

---

## ✨ Overview

The system includes:

- Book categories (with subcategories)
- Regular and premium users
- Books with borrowing restrictions (e.g. rare or in-library only)
- Color-based display for book categories
- Centralized logic for adding, searching, and borrowing books

---

## 🧩 Design Patterns Used

### 1. Composite
Represents the hierarchical structure of book categories, allowing each category to contain subcategories and books.

📁 `BooksInCategory` (`composite/`)

### 2. Bridge
Separates the abstraction (how categories are displayed) from the implementation (display method such as text color or background color).

📁 `TextColorDisplay`, `BackgroundColorDisplay` (`bridge/`)

### 3. Adapter
Maps between the `BookCategory` enumeration and the actual color display on the console. Allows for flexible visual presentation.

📁 `Adapter` (`adapter/`)

### 4. Decorator
Dynamically extends book behavior:

- `RareBookDecorator`: allows borrowing only for premium users.
- `LibraryOnlyDecorator`: restricts books to in-library reading only.

📁 `RareBookDecorator`, `LibraryOnlyDecorator` (`decorator/`)

### 5. Flyweight
Minimizes memory usage by sharing identical book objects via a factory.

📁 `BookFactory` (`flyweight/`)

### 6. Facade
Provides a simple and unified interface for interacting with the library (borrowing, returning, and searching books).

📁 `LibraryFacade` (`facade/`)

---

## 🔧 Technologies

- Python 3.12+
- Object-Oriented Programming (OOP)
- Classic GOF (Gang of Four) Design Patterns

---

## 🏁 How to Run

```bash
# Clone the repository
git clone https://github.com/Dvora-Abrahams/DesignPatternLibrary.git

# Navigate to the project directory
cd DesignPatternLibrary

# Run the application
python main.py


## 👩‍💻 Author
Developed by Dvora Abrahams as a hands-on implementation of common software architecture patterns using Python.

