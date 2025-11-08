Proyecto: Descargar videos o música de YouTube con Python

Estructura de carpetas:
proyecto_descargas/
├── descargas/              → Carpeta donde se guardan los archivos descargados
├── descargar_youtube.py    → Script principal con el código
├── lista.txt               → (Opcional) lista de URLs para descargas múltiples
└── README.txt              → Este archivo con las instrucciones

Cómo usar:
1. Abrir PowerShell o CMD dentro de la carpeta proyecto_descargas.
2. Ejecutar:
   python descargar_youtube.py "URL_DEL_VIDEO"
   → descarga el video (MP4)

   python descargar_youtube.py "URL_DEL_VIDEO" -a
   → descarga solo el audio (MP3)

3. Si quieres descargar varias URLs desde lista.txt:
   python descargar_youtube.py lista.txt -b -a
