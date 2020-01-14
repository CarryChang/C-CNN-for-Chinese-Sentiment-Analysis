from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from SA import CnnModel
app = Flask(__name__)
api = Api(app)
# 返回的json支持中文
app.config['JSON_AS_ASCII'] = False
class Sentiment_analysis(Resource):
    def get(self, comment):
        import time
        s = time.clock()
        sa = CnnModel().emotion_score(comment)
        output = {'comment': comment, 'sa': ("%.5f" % sa)}
        print(time.clock()-s)
        return jsonify({'result': output})
api.add_resource(Sentiment_analysis, '/cnn_sa_api/<string:comment>')
if __name__ == '__main__':
    app.run()