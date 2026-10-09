from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['cityName']
        state_code = request.form['stateName']
        country_code = request.form['countryName']
        data = get_weather(city_name, state_code, country_code)
        return render_template('index.html', data=data)
    return render_template('index.html', data=None)

if __name__ == "__main__":
    app.run(debug=True)