from flask import Flask, render_template, request, send_file, jsonify
from descargar_youtube import descargar_video, descargar_audio
import os
import tempfile

app = Flask(__name__, template_folder='paginas')

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
        # Crear carpeta temporal
        with tempfile.TemporaryDirectory() as temp_dir:
            if tipo == 'video':
                ruta_archivo = descargar_video(url, temp_dir)
            elif tipo == 'audio':
                ruta_archivo = descargar_audio(url, temp_dir)
            else:
                return jsonify({'mensaje': '❌ Tipo inválido'}), 400

            # Enviar el archivo al navegador
            nombre_archivo = os.path.basename(ruta_archivo)
            return send_file(ruta_archivo, as_attachment=True, download_name=nombre_archivo)

    except Exception as e:
        print("Error al descargar:", e)
        return jsonify({'mensaje': f'❌ Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
