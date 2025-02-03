from flask import Flask, request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def handle_404(error):
    return error

#get params as URL parameters
@app.route('/my_getP', methods=['GET'])
def handle_getP():
    param1 = request.args['param1']
    param2 = request.args['param2']


    #let's just return parameters back to a client as JSON
    return jsonify(param1=param1, param2=param2)

#get params as part of URL
@app.route('/my_getU/<param1>/<param2>', methods=['GET'])
def handle_getU(param1, param2):

    #let's just return parameters back to a client as JSON
    return jsonify(param1=param1, param2=param2)

#get params as part as body
@app.route('/my_getB', methods=['GET'])
def handle_getB():
    if request.data == None :
        raise Exception("data in request is null","WebHost")
    
    data = request.data
    
    # do something with data you got from client

    #when done return success
    return jsonify(success=True, data=str(data))      

#POST

#get params as URL parameters
@app.route('/my_postP', methods=['POST'])
def handle_postP():
    param1 = request.args['param1']
    param2 = request.args['param2']


    #let's just return parameters back to a client as JSON
    return jsonify(param1=param1, param2=param2)

#get params as part of URL
@app.route('/my_postU/<param1>/<param2>', methods=['POST'])
def handle_postU(param1, param2):

    #let's just return parameters back to a client as JSON
    return jsonify(param1=param1, param2=param2)

#get params as part as body
@app.route('/my_postB', methods=['POST'])
def handle_postB():
    if request.data == None :
        raise Exception("data in request is null","WebHost")
    
    data = request.data
    
    # do something with data you got from client

    #when done return success
    return jsonify(success=True, data=str(data))


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=777)