from flask import Flask, render_template, request

app = Flask(__name__)

# Route for displaying the feedback form
@app.route('/')
def feedback_form():
    return render_template('feedback.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Save feedback to a file
    with open('feedback_data.txt', 'a') as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n{'-'*40}\n")
    
    return f"<h1>Thank you, {name}! Your feedback has been received. Test commit</h1>"

if __name__ == '__main__':
    app.run(debug=True)
