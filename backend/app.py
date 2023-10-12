from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
dbuser = os.environ.get('POSTGRES_USER')
dbpassword = os.environ.get('POSTGRES_PASSWORD')
dbname = os.environ.get('POSTGRES_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{dbuser}:{dbpassword}@db:5432/{dbname}"
db = SQLAlchemy(app)

# Define your Todo model here
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

@app.route('/todos', methods=['GET'])
def todos():
    if request.method == 'GET':
        with app.app_context():
            todos = Todo.query.all()
            todo_list = [{"id": todo.id, "title": todo.title, "completed": todo.completed} for todo in todos]
            return jsonify(todo_list)

@app.route('/todos', methods=['POST'])
def create_todo():
    try:
        data = request.get_json()

        if 'title' not in data:
            return jsonify({"error": "Title is required"}), 400

        new_todo = Todo(title=data['title'])

        try:
            with app.app_context():
                with db.session.begin():
                    db.session.add(new_todo)
                db.session.commit()
            
            # Serialize the relevant properties of the new_todo object
            todo_dict = {
                "id": new_todo.id,
                "title": new_todo.title,
                "completed": new_todo.completed
            }

            return jsonify(todo_dict), 200

        except Exception as e:
            with app.app_context():
                db.session.rollback()
                app.logger.error(f"Failed to create todo: {str(e)}")
            return jsonify({"error": "Failed to create todo"}), 500
    except Exception as e:
        return jsonify({"error": "Invalid JSON data"}), 400

    


@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def todo(id):
    #todo = Todo.query.get_or_404(id)

    if request.method == 'GET':
        todo = Todo.query.get_or_404(id)
        return jsonify(todo.__dict__)

    if request.method == 'PUT':
        todo = Todo.query.get_or_404(id)
        data = request.get_json()
        todo.title = data['title']
        todo.completed = data['completed']
        with app.app_context():
            db.session.commit()
        return jsonify(todo.__dict__)

    if request.method == 'DELETE':
        with app.app_context():
            todo = Todo.query.get_or_404(id)
            db.session.expunge(todo)
            db.session.delete(todo)
            db.session.commit()
        return '', 204

if __name__ == '__main__':
    app.run()
