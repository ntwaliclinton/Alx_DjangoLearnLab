Django Blog Project
This project is a simple blog platform built using Django, where users can register, log in, and manage blog posts. It also supports CRUD operations for blog posts and basic profile management.

Features
User Authentication:

User registration, login, and logout.
Profile management for logged-in users.
Blog Post Management:

Create, read, update, and delete (CRUD) operations for blog posts.
Authenticated users can manage their own blog posts.
Permissions:

Only registered users can create posts.
Users can only edit or delete their own posts.
Anonymous users can view blog posts but cannot modify them.
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/django_blog
2. Create and Activate Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Apply Database Migrations
bash
Copy code
python manage.py migrate
5. Create a Superuser (optional)
bash
Copy code
python manage.py createsuperuser
6. Run the Development Server
bash
Copy code
python manage.py runserver
7. Access the Application
Go to http://127.0.0.1:8000 in your browser.

How to Use the Features
1. User Authentication
Register: Go to /register/ to create an account.
Login: Use /login/ to log in.
Logout: Log out at /logout/.
Profile: Users can view and edit their profile at /profile/.
2. Blog Post Management
View Posts: All users can see blog posts on the homepage / or individual posts at /post/<id>/.
Create Post: Logged-in users can create a new post at /post/new/.
Edit Post: Post authors can edit their posts at /post/<id>/edit/.
Delete Post: Post authors can delete their posts at /post/<id>/delete/.
Permissions
Anonymous Users: Can view posts but cannot create, edit, or delete them.
Authenticated Users: Can create posts, edit or delete their own posts.
Profile Management: Only authenticated users can manage their profile.
Security
CSRF Protection: All forms are secured with CSRF tokens.
Password Security: Django's hashing algorithms ensure secure password handling.
Contributing
Feel free to open issues or contribute to this project via pull requests.