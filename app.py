from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    email = request.form.get('email')
    activity = request.form.get('activity')
    date = request.form.get('date')
    people = request.form.get('people')

    # Save booking to a file
    with open('bookings.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}, Activity: {activity}, Date: {date}, People: {people}\n")

    # Redirect back to home with a success message (optional)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)