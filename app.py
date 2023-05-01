from flask import Flask,request,jsonify
from chatbot import Intent,Entity,DEntity
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
device = Entity("device",[
    "phone",
    "laptop",
    "tablet",
    "camera",
    "smartphone",
    "laptop",
    "digital camera"
])
Entity.add_to_pipeline()


@app.route('/hello/<string:name>')
def hello_world(name):
    # return 'Hello World!'
    return jsonify({"message":f'Hello {name}'})




preBuildEntities = [
    "CARDINAL"
]
@app.route('/data',methods=['POST'])
def data():
    json = request.get_json()
    entities = [i for i in Entity.entities if i.name in json["required_entities"] and i.name not in preBuildEntities]
    l=[DEntity(i) for i in json["required_entities"] if i in preBuildEntities]
    if (len(l)>0):
        entities.extend(l)
    print(entities)
    response = ""
    user_msg = json["user_msg"]
    if not ("intents" in json):
        return jsonify({"msg":"","entities":[]})
    id=0
    for data in json["intents"]:
        intent = Intent(data["name"],data["messages"],data["responses"],required_entities=entities)
        r = intent.parse(user_msg)
        if (r!="") :
            response = r
            id = data['id']
            break
    return jsonify({"id":id,"msg":response,"entities":{i[1]:i[0] for i in intent.entities}})


if __name__ == '__main__':
    app.run(debug=True)