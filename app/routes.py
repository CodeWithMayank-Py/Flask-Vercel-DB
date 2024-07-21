from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Subscription

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    db.session.commit()
    flash('Subscription successful!!', 'success')
    return redirect(url_for('index'))