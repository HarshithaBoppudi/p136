from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)


@app.route("/")
def get_data():
    return jsonify({
        "data":data,
        "status":"success",


    }),200

@app.route("/planet")
def planet():
    name=request.args.get("name")
    planet_data=next(i for i in data if i["name"]==name)
    return jsonify({
        "data":planet_data,
        "status":"success"
    }),200    


if __name__=="__main__":
    app.run(debug=True)

    