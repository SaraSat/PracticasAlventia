from flask import Flask, escape, request, jsonify, render_template

import json

app=Flask(__name__)

@app.route('/')
def home():
    with open('lista.html') as f:
        return f.read()
@app.route('/api/lista')
@app.route('/api/lista/<id>')
def lista_GET(id=None):
    with open('database.json') as f:
        database = json.loads(f.read())
    res=database
    if id:
        item =[x for x in database if x['id']==id]
        res =item[0] if item else None
    return jsonify(res)

@app.route('/api/lista', methods=['POST'])
def lista_POST():
    data=request.json
    with open('database.json') as f:
        database= json.loads(f.read())
    res=dict(
        id=len(database),
        texto=data['texto'],
        comprado=False,
    )
    database.append(res)
    with open('database.json','w') as f:
        f.write(json.dumps(database))
    return jsonify(res)

@app.route('/api/lista/<id>',methods=['PUT'])
def lista_PUT(id):
    data=request.json
    with open('database.json') as f:
        database = json.loads(f.read())

    res =[x for x in database if x['id']==id]
    for x in res:
        database.update(x['comprado'],data)
    
    return jsonify(res)

@app.route('/api/lista/<id>', methods=['DELETE'])
def lista_DELETE(id):
    pass

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__=='__main__':
    main()