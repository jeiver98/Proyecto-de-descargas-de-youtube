# app.py
from flask import Flask, render_template, request, jsonify, send_from_directory
from descargar_youtube import descargar_video, descargar_audio
import os

DESCARGAS = 'descargas'

app = Flask(__name__, template_folder='paginas')

# Crear carpeta descargas si no existe
os.makedirs(DESCARGAS, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    data = request.get_json()
    url = data.get('url')
    tipo = data.get('tipo')

    if not url:
        return jsonify({'mensaje': '❌ Debes ingresar una URL'}), 400

    try:
        if tipo == 'video':
            archivo = descargar_video(url, DESCARGAS)
            return jsonify({'mensaje': '✅ Video descargado correctamente', 'link': f'/descargas/{archivo}'})
        elif tipo == 'audio':
            archivo = descargar_audio(url, DESCARGAS)
            return jsonify({'mensaje': '✅ Audio descargado correctamente', 'link': f'/descargas/{archivo}'})
        else:
            return jsonify({'mensaje': '❌ Tipo de descarga inválido'}), 400
    except Exception as e:
        print("Error al descargar:", e)
        return jsonify({'mensaje': f'❌ Error: {str(e)}'}), 500

# Ruta para servir los archivos descargados
@app.route('/descargas/<filename>')
def descargar_archivo(filename):
    return send_from_directory(DESCARGAS, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
