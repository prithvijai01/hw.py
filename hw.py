from flask import Flask,jsonify,request
app = Flask(__name__)

contacts = [
    {
        'id':1,
        'name':'Prithvi',
        'contact':'123456789',
        'done':False

        
    },

    {
        'id':2,
        'name':'Nischay',
        'contact':'123453789',
        'done':False

        
    }
]

@app.route("/add-data", methods =["POST"])

def add_task():

    if not request.json:

        return jsonify({

            "status":"error",
            "message": "Please provide the data !"
        },400)

    contact = {
        'id': tasks[-1]['id'] +1,
        'Name': request.json['Name'],
        'contact': request.json.get('contact',""),
        'done': False
    }

    contacts.append(contact)
    return jsonify({
            "status":"sucess",
            "message":"task added sucessfully"
    },200)
app.run()
