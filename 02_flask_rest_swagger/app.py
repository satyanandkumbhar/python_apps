from apispec import APISpec
from flask import Flask, jsonify
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World !'

spec = APISpec(
    title = 'flask-api-swagger-doc',
    version = '1.0.0',
    openapi_version = '3.0.2',
    plugins = [FlaskPlugin(), MarshmallowPlugin()]
)

@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())


class TodoResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    status = fields.Boolean()

class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoResponseSchema))


@app.route('/todo')
def todo():
    """Get list of todo
        ---
        get:
            description: Get list of todos
            response:
                200:
                    description: Return a todo list
                    content:
                        application/json:
                            schema: TodoListResponseSchema


    """
    dummy_data = [{
        'id': 1,
        'title': 'Finish this task',
        'status': False
    }, {
        'id': 2,
        'task': 'Finish that task',
        'status': True
    }]
    return TodoListResponseSchema().dump({'todo_list':dummy_data})

with app.test_request_context():
    spec.path(view=todo)

if __name__ == '__main__':
    app.run(debug=True)