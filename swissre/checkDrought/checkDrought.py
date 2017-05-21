from flask import Flask
import openpyxl as px
import pandas as pd
import itertools as it
from flask import request


app = Flask(__name__)

@app.route("/")
def hello():
    args = request.args
    county = request.args.getlist('county')
    print(county)
    data = getData(county[0])
    return data.to_json()

def getData(county):
    print(county)
    wb = px.load_workbook('EARS_sample_index_dataset.xlsx')
    ws = wb['payout_monitoring_2016']
    data = ws.values
    cols = next(data)[1:]
    data = list(data)
    idx = [r[0] for r in data]
    data = (it.islice(r, 1, None) for r in data)
    df = pd.DataFrame(data, index=idx, columns=cols)
    df = df[df.index == county]
    output = df.PAYOUT
    return output

if __name__ == "__main__":
    app.run()
