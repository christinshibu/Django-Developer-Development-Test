# Product Management System

A small Django project to manage products of an e-commerce store.
Made as a Junior Python/Django developer test for BThinkX.

## Technologies Used
- Python 3
- Django
- SQLite
- HTML, CSS, Bootstrap 5
- Pillow (for product images)

## How to Install
1. Clone the repository
   ```
   git clone <your-repo-link>
   cd product_project
   ```
2. Create and activate a virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate        (Windows)
   ```
3. Install the packages
   ```
   pip install -r requirements.txt
   ```
4. Create the database tables
   ```
   python manage.py makemigrations products
   python manage.py migrate
   ```
5. Create the admin user
   ```
   python manage.py createsuperuser
   ```

## How to Run
```
python manage.py runserver
```
Open http://127.0.0.1:8000/ in the browser.

**First time only:** categories are added from the Django admin panel.
Go to http://127.0.0.1:8000/admin/, log in, open **Categories** and add a few
(for example Clothing, Electronics, Books). After that you can add products.

## Login Credentials
Use the superuser you created in step 5. Example:
- Username: `admin`
- Password: `admin123` 

## About the Project
- **Login / Logout** - only logged-in users can use the pages.
- **Dashboard** - cards for total, active, inactive and low stock products.
- **Product List** - search by name, filter by category and status, pagination (5 per page), View / Edit / Delete.
- **Add / Edit Product** - one form used for both, with validation.
- **Product View** - shows all details of one product.

### Rules implemented
- SKU must be unique
- Price must be greater than 0
- Stock cannot be negative
- Name, SKU and Category are required
- Stock of 5 or less shows a "Low Stock" badge
- Inactive products show an "Inactive" badge
- Delete asks for confirmation first
