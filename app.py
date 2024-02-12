from flask import Flask, jsonify, request, stream_with_context, Response
from flask_cors import CORS

app = Flask(__name__)

import openai_completions
CORS(app, resources={r"/openai/*": {"origins": "http://localhost:4200"}})

#define a route
@app.route('/openai', methods=['GET'])
def get():
    print('in get')
    #sync call
    #return jsonify({'response': openai_completions.generate_response('Hello')})

    #streaming call
    return Response(openai_completions.generate_streaming_response('Hello'), content_type='text/event-stream')


#run the app
if __name__ == '__main__':
    app.run(debug=True, threaded=True)