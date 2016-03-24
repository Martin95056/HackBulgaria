from db_communicator import session
from models import Airline
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/airlines/country/<country_name>')
def get_country_amount(country_name):
    country = session.query(Airline).\
             filter(Airline.country == country_name).first()

    return str(country.amount)


@app.route('/airlines/country_code/<country_code>')
def get_code_name(country_code):
    country = session.query(Airline).\
             filter(Airline.code == country_code).first()

    return str(country.amount)

if __name__ == '__main__':
    app.run(debug=True)
