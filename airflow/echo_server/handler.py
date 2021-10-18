from flask import Flask, request, jsonify
from cloudevents.http import from_http
import logging,json

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def echo():
    if request.method == 'GET':
        sc = 200
        msg = 'POST to this endpoint to echo cloud events'
        message = {
            'status': sc,
            'message': msg,
        }
        resp = jsonify(message)
        resp.status_code = sc
        return resp

    if request.method == 'POST':
        try:
            event = from_http(request.headers, request.get_data(),None)

            data = event.data
            # hack to handle non JSON payload, e.g. xml
            if not isinstance(data,dict):
                data = str(event.data)

            e = {
                "attributes": event._attributes,
                "data": data
            }
            app.logger.info(f'"***cloud event*** {json.dumps(e)}')
            return {}, 204
        except Exception as e:
            sc = 404
            msg = f'could not decode cloud event: {e}'
            app.logger.error(msg)
            message = {
                'status': sc,
                'error': msg,
            }
            resp = jsonify(message)
            resp.status_code = sc
            return resp

# hint: run with FLASK_ENV=development FLASK_APP=handler.py flask run
if __name__ == "__main__":
    app.run()