from flask import Flask, jsonify, request, stream_with_context, Response
from flask_cors import CORS
app = Flask(__name__)
import openai_completions 
CORS(app, resources={r"/openai/*": {"origins": "http://localhost:4200"}})



#define a route
@app.route('/openai', methods=['GET'])
def get():
    # return Response(openai_completions.generate_streaming_response('how are you today?'), mimetype='text/event-stream')
    #stream = openai_completions.generate_streaming_response('how are you today?')
    #for chunk in stream:
    return Response(openai_completions.generate_streaming_response('how are you today?'), mimetype='text/event-stream')


#run the app
if __name__ == '__main__':
    app.run(debug=True)