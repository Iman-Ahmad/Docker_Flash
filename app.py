from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/counter_db'
db = SQLAlchemy(app)

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    client_info = db.Column(db.String(200))

@app.route('/increment', methods=['POST'])
def increment_counter():
    client_info = request.headers.get('User-Agent')
    new_counter_entry = Counter(client_info=client_info)
    db.session.add(new_counter_entry)
    db.session.commit()
    return jsonify({"message": "Counter incremented!", "id": new_counter_entry.id}), 201

@app.route('/counter', methods=['GET'])
def get_counter():
    count = Counter.query.count()
    return jsonify({"counter": count}), 200

if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(host='0.0.0.0', port=5000)
