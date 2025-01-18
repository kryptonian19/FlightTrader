# FlightTrader
The Flight Trader project is a web-based platform designed for users to trade flight tickets. It provides a seamless user experience with visually appealing pages, an intuitive interface, and functionality for both buying and selling flight tickets. Here's a detailed breakdown of the project:

I. Key Features
    1. User Authentication

      i. Sign-Up Page:
        Users can register by providing their name, email, phone number, and password.
        A visually engaging form is presented with user-friendly input fields.
Login Page:
Registered users can log in using their email and password.
Validation ensures secure authentication.
Index Page

The primary dashboard for users post-login.
Divided into two main sections:
Searching Tickets:
Users can search for tickets by entering the "From Airport," "To Airport," and the travel date.
If no tickets match the search criteria, a message displays: "No tickets found."
If tickets are available, details such as Ticket ID, departure, and destination airports, date, and price are displayed with a "Buy" button.
Selling Tickets:
Users can sell their tickets by entering the ticket ID and price.
This makes the ticket available for others searching for matching criteria.
User Profile Page

Accessible by clicking on the circular profile picture at the top-right corner of the index page.
Displays the user’s:
Name
Email
Phone number
Owned tickets (if any).
Provides options to:
Add Tickets: Allows users to add ticket details (Ticket ID, From/To Airports, and Date of Travel).
Log Out: Ends the user session and redirects to the login page.
A back button navigates back to the index page.
Dynamic Ticket Transactions

Tickets sold by one user become available for purchase by others.
The search functionality ensures that only matching tickets are displayed to buyers.
Technical Details
Frameworks and Technologies
Backend:

Flask (Python): Handles routing, session management, and server-side logic.
SQLite: Lightweight database for storing user data, ticket details, and transactions.
Frontend:

HTML: Structures the web pages.
CSS: Enhances visual appeal with gradients, animations, hover effects, and responsive design.
JavaScript (Optional): Adds interactivity, such as loading spinners.
Static Files:

Custom stylesheets (styles.css) and images are stored in a static/ directory.
Templates:

Dynamic pages rendered using Jinja2 templates (.html files) with placeholders for dynamic content.
Workflow
Sign-Up:

Users visit the sign-up page by default when the app starts.
Form data is validated and stored in the database.
Login:

Users are redirected to the login page upon successful registration.
Credentials are validated against the database, and a session is created.
Index Page:

The user is greeted with a welcome message (e.g., Welcome, John).
Users can:
Search for tickets.
Sell tickets they own.
Profile Management:

Clicking the profile picture opens the profile page.
Users can:
View their details and tickets.
Add new tickets.
Log out.
Database Structure
Users Table:
Stores user details (ID, name, email, phone, password).
Tickets Table:
Stores ticket information (ID, seller ID, from airport, to airport, date, price, and buyer ID).
Transactions Table (Optional):
Logs purchase history and ticket ownership changes.
Visual Enhancements
The project employs modern design principles to ensure a polished look:

Gradient Backgrounds: Add depth and vibrancy.
Hover Effects: Enhance interactivity on buttons and list items.
Animations:
Loading spinner for fetching results.
Smooth transitions on button hover.
Typography: Clean, readable fonts (e.g., Poppins).
Use Case Example
Scenario 1: Selling Tickets
User 1 logs in and adds a ticket with ID T123, departing from JFK to LAX on 2025-01-20.
They sell the ticket on the index page for $200.
Scenario 2: Buying Tickets
User 2 logs in and searches for a ticket from JFK to LAX on 2025-01-20.
The system retrieves ticket T123 and displays it with the option to buy.
Future Enhancements
Payment Gateway Integration:
Enable secure transactions using platforms like Stripe or PayPal.
Email Notifications:
Notify users when their ticket is purchased or a matching ticket is available.
Mobile Responsiveness:
Ensure the platform adapts seamlessly to smartphones and tablets.
User Reviews:
Allow buyers and sellers to rate each other for improved trust.
This project offers a complete, visually appealing, and functional platform for trading flight tickets. It’s designed with scalability and extensibility in mind for future features! Let me know if you'd like further customization or additional features.
