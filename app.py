# from flask import Flask, jsonify */
import os
from flask import Flask, json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():
    #respond= {"user":"admin", "result":"OK -  healthy"}
    #return jsonify(respond)
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request sucessfull')
    return response


@app.route("/metrics")
def metrics():
    #data = {"UserCount":140, "UserCountActive":23}
    #respond=  {"user":"admin", "data":data}
    #return jsonify(respond)
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request sucessfull')
    return response

# streaming logs to a file called app.log
#filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'app.log')
#print(filename)
#app.logger.setLevel(logging.DEBUG)
#app.debug = True

logging.basicConfig(filename='app.log', level=logging.DEBUG)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    
    
