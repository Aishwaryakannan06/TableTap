# TableTap – Smart Restaurant Ordering & Bill Splitting System

## About the Project

TableTap is a web-based restaurant ordering system designed to simplify the dining experience. Customers can browse the menu, add food items to their cart, place orders, and split their bills without switching to another application.

The system is designed around dedicated touchscreen devices assigned to individual restaurant tables.

## Key Features

- **Digital Menu:** Browse food items, categories, and prices.
- **Shopping Cart:** Add items, update quantities, and view the total.
- **Order Placement:** Submit food orders through the application.
- **Smart Bill Splitting:**
  - Equal Split – Divide the total bill equally.
  - Split by Items – Calculate individual shares based on selected items.
  - Custom Split – Enter custom amounts.
- **Kitchen Dashboard:** View incoming orders.
- **Admin Dashboard:** Manage restaurant operations.

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite

## Project Structure

```text
TableTap/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── admin.html
│   └── kitchen.html
└── static/
    ├── style.css
    └── script.js
```

## How to Run Locally

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder.

3. Install dependencies:

```bash
py -m pip install -r requirements.txt
```

4. Start the Flask application:

```bash
py app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Learning Outcomes

- Understanding Flask-based web application development.
- Integrating frontend and backend components.
- Working with SQLite databases.
- Implementing order management and bill-splitting functionality.
- Exploring cloud services and web application deployment concepts.

## Internship

Developed as part of the **Codomax Digital Solutions – Module 4: Cloud Services & Web App Deployment**.

