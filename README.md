# 🎯 Poll Editor – Django Poll Voting Application

A simple and user-friendly **poll voting web application** built with **Python, Django, SQLite3, HTML, and Bootstrap 5**.

Poll Editor allows users to view available polls, vote for their preferred choices, and view the voting results. The application also includes the **Django Admin Panel** for managing polls and choices.

---

## ✨ Features

- 📋 View available polls
- 🗳️ Vote for poll choices
- 📊 View voting results
- ⚙️ Manage polls through Django Admin
- 🗄️ Database operations using Django ORM
- 🧩 Django template inheritance
- 📱 Responsive Bootstrap 5 interface
- 🔄 Simple and easy-to-use polling workflow

---

## 🛠️ Technologies Used

### Backend
- **Python**
- **Django**
- **Django ORM**

### Database
- **SQLite3**

### Frontend
- **HTML5**
- **Bootstrap 5**

### Administration
- **Django Admin**

---

## 📌 Application Workflow

The application follows a simple polling workflow:

User
  ↓
View Available Polls
  ↓
Select a Poll
  ↓
Choose an Option
  ↓
Submit Vote
  ↓
View Results

Administrators can manage polls and their choices through the Django Admin Panel.

📁 Project Structure
Poll_Editor/
│
├── manage.py
│
├── polls/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── db.sqlite3
└── README.md

The project structure may vary depending on the current implementation.

🚀 Installation & Setup
1. Clone the Repository
git clone https://github.com/aysha-nasrin26/Poll_Editor.git
2. Navigate to the Project
cd Poll_Editor
3. Install Django
pip install django
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Create an Admin User
python manage.py createsuperuser

Follow the prompts to create your Django admin account.

6. Start the Development Server
python manage.py runserver

The application will be available at:

http://127.0.0.1:8000/
🌐 Application URLs
Page	URL
🗳️ Polls	http://127.0.0.1:8000/polls/
⚙️ Admin Panel	http://127.0.0.1:8000/admin/
🎯 Main Functionalities
📋 Poll Listing

Users can view the available polls from the polls page.

🗳️ Voting System

Users can select an available choice and submit their vote.

📊 Result Display

After voting, users can view the current results of the poll.

⚙️ Django Admin

The Django Admin Panel allows administrators to manage polls and their choices.

🗄️ Django ORM

The project uses Django ORM to interact with the SQLite3 database through Django models.

🧩 Template Inheritance

Django template inheritance is used to maintain reusable and consistent page layouts.

💡 Project Highlights
Built a complete poll and voting workflow using Django
Implemented database operations using Django ORM
Used Django Admin for managing application data
Created reusable templates using template inheritance
Designed the interface using Bootstrap 5
Used SQLite3 for lightweight database management
📚 Learning Outcomes

Through this project, I gained practical experience in:

Python Django development
Django project and app structure
Django models and ORM
URL routing
Views and templates
Template inheritance
Database migrations
Django Admin
Handling user voting functionality
Bootstrap-based UI development
🔮 Future Improvements

Some possible improvements for future versions include:

🔐 User authentication and login
📈 Advanced poll analytics
⏰ Poll start and end dates
👤 User-specific voting history
🔍 Poll search and filtering
🎨 Enhanced UI and animations
👩‍💻 Author
Aysha Nasrin

Python & Django Developer

GitHub:
https://github.com/aysha-nasrin26
