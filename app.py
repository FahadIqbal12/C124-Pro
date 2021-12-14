from flask import Flask,request,jsonify
app = Flask(__name__)

data = [
    {
        'contact':7454567234,
        'name':'Raj',
        'done':False,
        'id':1
    },
    {
        'contact':93464573245,
        'name':'Rahul',
        'done':False,
        'id':2
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the data"
        },400)

    contact = {
        'id':data[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    data.append(contact)
    return jsonify({
        "status" : "success",
        "message":"Task added sucessfully"
    }) 

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })


if(__name__ == "__main__"):
    app.run(debug = True)
