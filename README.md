# ✈️ Flight Trader

Flight Trader is a web-based application that allows users to seamlessly buy and sell flight tickets. It features user authentication, dynamic ticket transactions, and a visually appealing interface to enhance the user experience.

---

## How to Run the project

### **Go to the master branch in this repository**
- Go to the master branch in this repository.
- Go to the codespace which is already created.
- run the command **pip install -r requirements.txt** in the terminal.
- run the command **python app.py** in the terminal to launch the project
- open the url in the browser to explore the project

---

## 🚀 Features

### **User Authentication**
- **Sign-Up**: Register by entering name, email, phone number, and password.
- **Login**: Access the platform using registered credentials.

### **Index Page (Dashboard)**
- **Search Tickets**:
  - Enter "From Airport," "To Airport," and the date to search for flight tickets.
  - Displays ticket details if available or a "No tickets found" message.
  - Option to buy available tickets.
- **Sell Tickets**:
  - Enter Ticket ID and price to sell tickets.
  - Tickets become available for other users to purchase.
- Displays a personalized welcome message at the top left (e.g., *Welcome, John*).

### **User Profile**
- View:
  - Name
  - Email
  - Phone number
  - Tickets owned
- **Add Tickets**:
  - Enter ticket details (Ticket ID, From/To Airports, Date of Travel) to add tickets.
- **Log Out**: End session and redirect to the login page.
- Navigate back to the index page.

### **Dynamic Ticket Transactions**
- Tickets listed by one user are available for others to buy.
- Ensures only matching tickets are displayed to buyers.

---

## 🛠️ Technologies Used

### **Backend**
- [Flask](https://flask.palletsprojects.com/): A lightweight Python web framework.
- [SQLite](https://www.sqlite.org/): A lightweight database for storing user and ticket information.

### **Frontend**
- **HTML**: For structuring web pages.
- **CSS**: For styling, including animations, gradients, and hover effects.
- **JavaScript (Optional)**: Adds interactivity (e.g., loading spinners).

---

## 📂 Project Structure

```plaintext
Flight-Trader/
├── app.py                # Main application file
├── templates/            # HTML templates
│   ├── signup.html       # User sign-up page
│   ├── login.html        # User login page
│   ├── index.html        # Dashboard (search/sell tickets)
│   ├── profile.html      # User profile page
├── static/               # Static assets
│   ├── styles.css        # Stylesheet for the project
│   ├── profile-placeholder.jpg # Placeholder for user profile picture
├── database.db           # SQLite database
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
