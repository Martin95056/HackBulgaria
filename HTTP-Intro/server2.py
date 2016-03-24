from db_communicator import session
from models import Airline
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def show_airlines():
    airlines = session.query(Airline).all()
    dic = {}
    for a in airlines:
        dic[a.country] = a.amount

    return jsonify(dic)


@app.route('/airlines', methods=['GET', 'POST'])
def get_airline():
    if request.method == 'GET':
        return request.args[0]


if __name__ == '__main__':
    app.run(debug=True)
