from datetime import datetime

from flask import Blueprint, request, jsonify

# from application.backend.services.message import Message

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
def view():
    return 'test'


@home_bp.route('/', methods=['POST'])
def message_answer():
    print('entro al post')
    data = request.get_json()
    message_user = data['message']['content']
    # message = Message(sender="Bot", content=message_user, hour=datetime.now().strftime('%I:%M %p'))
    # answer = message.answer_bot()
    # message.content = answer
    return jsonify({'a': 'test'}), 200
    # return jsonify(message.to_json()), 200


def init_app(app):
    app.register_blueprint(home_bp)
