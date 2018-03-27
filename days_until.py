from flask import Flask, jsonify
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
visitor_table = dynamodb.Table('visitors')

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', "http://daysuntilevent.com.s3-website-eu-west-1.amazonaws.com")
    response.headers.add('Access-Control-Allow-Headers', "Content-Type,Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET,POST,OPTIONS")
    return response

@app.route('/')
def main_page():
    visitor = str(uuid.uuid4())
    visitor_table.put_item(Item={'visitor': visitor})
    return jsonify({'visitor': visitor})

if __name__ == '__main__':
    app.run(debug=True)