from datetime import datetime

from flask import Blueprint, request, jsonify

from application.backend.services.message import Message

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['POST'])
def message_answer():
    data = request.get_json()
    message_user = data['message']['content']
    message = Message(sender="Bot", content=message_user, hour=datetime.now().strftime('%I:%M %p'))
    message.content = 'enviado del servidor'
    return jsonify(message.to_json()), 200


def init_app(app):
    app.register_blueprint(home_bp)
