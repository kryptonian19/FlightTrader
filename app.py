from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tickets_owned = db.relationship('Ticket', backref='owner', lazy=True)

# Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.String(50), nullable=False)
    to_airport = db.Column(db.String(50), nullable=False)
    from_airport = db.Column(db.String(50), nullable=False)
    date_of_travel = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

# Routes
@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")

    if User.query.filter_by(email=email).first():
        flash("Email already registered!")
        return redirect("/")

    user = User(name=name, email=email, phone=phone, password=password)
    db.session.add(user)
    db.session.commit()
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email, password=password).first()
    
    if user:
        session["user_id"] = user.id
        session["user_name"] = user.name
        return redirect("/index")
    else:
        flash("Invalid email or password!")
        return redirect("/login")

@app.route("/index")
def index():
    if "user_id" not in session:
        return redirect("/login")
    
    tickets = Ticket.query.filter_by(owner_id=None).all()
    return render_template("index.html", tickets=tickets)

@app.route("/search", methods=["POST"])
def search():
    from_airport = request.form.get("from_airport")
    to_airport = request.form.get("to_airport")
    date = request.form.get("date")
    tickets = Ticket.query.filter_by(from_airport=from_airport, to_airport=to_airport, date_of_travel=date, owner_id=None).all()
    return render_template("index.html", tickets=tickets, search_results=True)

@app.route("/buy/<int:ticket_id>")
def buy_ticket(ticket_id):
    if "user_id" not in session:
        return redirect("/login")
    
    ticket = Ticket.query.get(ticket_id)
    if ticket and ticket.owner_id is None:
        ticket.owner_id = session["user_id"]
        db.session.commit()
    return redirect("/index")

@app.route("/sell", methods=["POST"])
def sell_ticket():
    if "user_id" not in session:
        return redirect("/login")
    
    ticket_id = request.form.get("ticket_id")
    price = float(request.form.get("price"))

    ticket = Ticket.query.filter_by(ticket_id=ticket_id, owner_id=session["user_id"]).first()
    if ticket:
        ticket.price = price
        ticket.owner_id = None
        db.session.commit()
    return redirect("/index")

@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect("/login")
    
    user = User.query.get(session["user_id"])
    return render_template("profile.html", user=user)

@app.route("/add-ticket", methods=["POST"])
def add_ticket():
    if "user_id" not in session:
        return redirect("/login")
    
    ticket_id = request.form.get("ticket_id")
    to_airport = request.form.get("to_airport")
    from_airport = request.form.get("from_airport")
    date = request.form.get("date_of_travel")
    price = request.form.get("price")
    
    ticket = Ticket(ticket_id=ticket_id, to_airport=to_airport, from_airport=from_airport, date_of_travel=date, price=price, owner_id=session["user_id"])
    db.session.add(ticket)
    db.session.commit()
    return redirect("/profile")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

from app import app, db
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
