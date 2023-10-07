from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # SQLite database
db = SQLAlchemy(app)

# Define your Todo model here
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

@app.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'GET':
        with app.app_context():
            todos = Todo.query.all()
            return jsonify([todo.__dict__ for todo in todos])

    if request.method == 'POST':
        data = request.get_json()
        new_todo = Todo(title=data['title'])
        with app.app_context():
            db.session.add(new_todo)
            db.session.commit()
        return jsonify(new_todo.__dict__), 201

@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def todo(id):
    todo = Todo.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(todo.__dict__)

    if request.method == 'PUT':
        data = request.get_json()
        todo.title = data['title']
        todo.completed = data['completed']
        with app.app_context():
            db.session.commit()
        return jsonify(todo.__dict__)

    if request.method == 'DELETE':
        with app.app_context():
            db.session.delete(todo)
            db.session.commit()
        return '', 204

if __name__ == '__main__':
    app.run()
