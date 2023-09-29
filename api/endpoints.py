from flask import Flask, request, jsonify

app = Flask(__name__)

# (simulación de base de datos)
chats = []
messages = []

# Endpoint para crear un nuevo chat
@app.route('/api/chats', methods=['POST'])
def create_chat():
    data = request.json
    chat = {
        'id': len(chats) + 1,
        'nombre': data['nombre'],
        'miembros': data['miembros']
    }
    chats.append(chat)
    return jsonify(chat), 201

# Endpoint para obtener la lista de chats de un usuario
@app.route('/api/chats', methods=['GET'])
def get_chats():
    usuario = request.args.get('usuario')
    user_chats = [chat for chat in chats if usuario in chat['miembros']]
    return jsonify(user_chats)

# Endpoint para enviar un mensaje en un chat
@app.route('/api/messages', methods=['POST'])
def send_message():
    data = request.json
    message = {
        'id': len(messages) + 1,
        'chatId': data['chatId'],
        'contenido': data['contenido'],
        'autor': 'usuario1',  # Aquí debe obtenerse el autor autenticado
        'fecha': '2023-09-27T10:00:00Z'  # Timestamp actual
    }
    messages.append(message)
    return jsonify(message), 201

# Endpoint para obtener mensajes de un chat específico
@app.route('/api/messages', methods=['GET'])
def get_messages():
    chat_id = int(request.args.get('chatId'))
    chat_messages = [msg for msg in messages if msg['chatId'] == chat_id]
    return jsonify(chat_messages)

# Endpoint para cargar una imagen en un chat (simplificado)
@app.route('/api/upload', methods=['POST'])
def upload_image():
    chat_id = int(request.form['chatId'])
    image_file = request.files['imagen']
    
    # Aquí debes implementar la lógica para almacenar la imagen y devolver la URL
    # Esto puede implicar guardar la imagen en una ubicación específica y generar una URL para acceder a ella
    
    response = {
        'id': len(messages) + 1,
        'chatId': chat_id,
        'nombreArchivo': image_file.filename,
        'url': 'https://www.ejemplo.com/imagenes/' + image_file.filename
    }
    
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)