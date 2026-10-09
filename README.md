# Flask Weather App 🌦️

A weather web application built with **Python and Flask** that allows users to retrieve and view weather information for a specified location.

The project demonstrates the fundamentals of Python web development, server-side routing, dynamic HTML rendering, and integration with external weather data sources.

## ✨ Features

* **Weather Information:** Retrieve and display weather information for a specified location.
* **Flask Backend:** Handle HTTP requests and application routing using Flask.
* **Dynamic Web Pages:** Render weather information using HTML templates and Jinja2.
* **External Data Integration:** Fetch weather data from an external weather API.
* **Simple User Interface:** Provide a straightforward interface for searching weather information.

## 🛠️ Tech Stack

* **Language:** Python
* **Backend Framework:** Flask
* **Frontend:** HTML, CSS
* **Templating Engine:** Jinja2
* **Data Source:** Weather API

## 📁 Project Structure

```text
flask-weather-app/
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Adjust the structure above to match the actual files in your repository.*

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3
* pip
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/Subhajit-13/flask-weather-app.git
cd flask-weather-app
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment.

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

If the application requires a weather API key, configure it using the environment variable expected by the application.

Keep API keys and other sensitive credentials out of version control.

### 5. Run the Application

If the entry-point file is `app.py`, start the application using:

```bash
python3 app.py
```

Alternatively, if the application supports Flask's CLI:

```bash
flask --app app run --debug
```

Open the local URL displayed in the terminal, typically:

http://127.0.0.1:5000/

## 🎯 Learning Objectives

* Understand the fundamentals of Python web development.
* Build web applications using Flask.
* Implement routes and handle HTTP requests.
* Render dynamic HTML pages using Jinja2 templates.
* Integrate external APIs into a web application.
* Organize application code and manage Python dependencies.

## 🔮 Future Improvements

* Add input validation and handling for invalid locations.
* Display additional weather details, such as humidity, wind speed, and feels-like temperature.
* Improve responsive design for mobile and desktop devices.
* Implement meaningful error messages for API failures.
* Manage configuration and API credentials through environment variables.
* Add automated tests for application routes and core functionality.

## 👨‍💻 Author

**Subhajit Biswas**

* GitHub: [Subhajit-13](https://github.com/Subhajit-13)

---

*Developed as a hands-on Python and Flask web application project.*
