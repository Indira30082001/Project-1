# Feedback Form Application

A simple web application built with **HTML**, **CSS**, and **Python (Flask)** that allows users to submit feedback. The feedback is processed by the backend and stored in a file for future use.

---

## Features

- A responsive feedback form built with HTML and CSS.
- Backend functionality using Python Flask to process form submissions.
- Feedback is saved in a text file (`feedback_data.txt`).
- Easy-to-extend structure for additional features like databases or advanced validation.

---

## Project Structure

feedback_app/ │ ├── app.py # Main Python script (Flask server) ├── templates/ # Folder for HTML files │ └── feedback.html # Feedback form ├── static/ # Folder for static files (CSS) │ └── styles.css # Styling file └── feedback_data.txt # File to save feedback (created automatically)

---

## Requirements

Make sure you have the following installed:

- Python 3.x
- Flask library

Install Flask using:
pip install flask
How to Run the Application
Clone the repository:

git clone <repository-URL>
cd feedback_app
Run the Flask server:

python app.py
Open a web browser and go to:

http://127.0.0.1:5000
Fill out the feedback form and submit it. The feedback will be saved in the feedback_data.txt file.
