## README.md -- personal Flask Webpage Project

## description
This project was a challenging yet rewarding experience where I worked to integrate both Python (Flask) and Java elements into a unified web application. Learning two programming languages in a short time was difficult, especially while managing cookies, sessions, and databases across different components. One of the biggest challenges was keeping such a large codebase organized while implementing interactive front-end features and dynamic back-end functionality.

Despite the initial difficulty, I’ve become significantly more comfortable with both languages, particularly Python for web development. I’ve also improved in visualizing and planning web designs, which helped me bring this personal site to life more effectively than I thought I could at the start of this class.

## overview
This is a **personal website project** built using:
- Python Flask (back-end)
- HTML templates (front-end structure)
- CSS (styling)
- SQLite (database)
- Cookies and sessions (user login and authentication)

## features
- Multi-page Flask website
- User registration & login with cookies and sessions
- Contact form with AJAX and validation
- SQLite database for users and messages
- Interactive hobby cards with animations
- Protected messages page
- Auto logout after inactivity

---

## file Structure
```text
project/
│
├── web.py               # Main Flask server (routes and logic)
├── database.py          # Handles database setup and queries
├── /templates           # HTML files for each webpage
│    ├── base.html
│    ├── index.html
│    ├── about.html
│    ├── resume.html
│    ├── contact.html
│    ├── messages.html
│    ├── login.html
│    └── register.html
│
└── /static
     └── style.css       # Website styling
```

---

## getting started
1. Make sure you have Flask installed:
```bash
pip install Flask
```

2. Run the web server:
```bash
python3 web.py
```

3. Open your browser and go to:
```
http://localhost:5055
```

---

## file explanations

### web.py
- Controls:
  - Page routing
  - Form submissions (AJAX in contact form)
  - User registration and login
  - Cookie handling
  - Session handling (auto logout after inactivity)
- Connects to `database.py` to save and retrieve data.

### database.py
- SQLite database with two tables:
  - `users` (for login, cookies, and registration)
  - `user_messages` (stores contact form messages)
- Key functions:
  - `init_db()` → Creates tables
  - `add_message()` → Saves a message
  - `get_all_messages()` → Fetches all messages
  - `add_user()` → Registers a new user
  - `find_user()` → Looks up user by username and password

### static/style.css
- All styling and animations:
  - Layout, buttons, headers, forms, hover effects
  - Progress bars, hobby cards, GitHub cards
  - Success and error message styling
  - Responsive design

---

## templates (HTML Files)

### base.html
- Main layout (navbar, header, footer)
- Uses `{% block content %}` for page-specific content

### index.html
- Homepage with a welcome message

### about.html
- Personal interests:
  - Reading, Hiking, Violin, Coding, GitHub Projects
- Hobby cards with animations and interactions

### resume.html
- Education, skills, experience
- Expandable sections with toggle icons and animations

### contact.html
- AJAX contact form with client-side validation
- Submits to Flask server and stores messages in database

### messages.html
- Displays all stored messages (requires login)
- Uses an unordered list inside a styled container

### login.html
- User login form with cookie and session handling
- Protects the messages page

### register.html
- User registration form with username and password

---

## authentication features

- Cookies: Stores username on browser
- Sessions: Tracks login server-side
- Auto Logout: Logs out after 5 minutes of inactivity
- Protected Pages: Messages page is hidden unless logged in

---

## database schema

### users table
| Column            | Type         | Notes                 |
|-------------------|--------------|-----------------------|
| id                | INTEGER      | Primary Key           |
| username          | TEXT         | Unique, Not Null      |
| password_hash     | TEXT         | Not Null              |
| registration_date | TIMESTAMP    | Auto-set on creation  |

### messages table
| Column    | Type      | Notes                 |
|-----------|-----------|-----------------------|
| id        | INTEGER   | Primary Key           |
| name      | TEXT      | Not Null              |
| email     | TEXT      | Not Null              |
| message   | TEXT      | Not Null              |
| timestamp | DATETIME  | Auto-set on creation  |

---


