from flask import Flask, request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def handle_404(error):
    return error

@app.route('/my_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        param1 = request.args['param1']
        param2 = request.args['param2']


    #let's just return parameters back to a client as JSON
    return jsonify(param1=param1, param2=param2)
        

@app.route('/my_post', methods=['POST'])
def handle_post():
    if request.data == None :
        raise Exception("data in request is null","WebHost")
    
    data = request.data
    
    # do something with data you got from client

    #when done return success
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=777)