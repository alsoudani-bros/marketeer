from flask import Flask
from utilities import reports


app = Flask(__name__)


@app.route("/financial")
def getting_financials():
    return reports.finance


@app.route("/performance")
def getting_performace():
    return reports.performance
