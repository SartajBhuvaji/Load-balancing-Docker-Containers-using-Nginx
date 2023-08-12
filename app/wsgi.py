#docker-compose up -d --build --scale app=3
#docker compose down
#docker ps 


from flask import Flask, send_file, abort, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import configparser
import socket

app = Flask(__name__,template_folder='render_template')
config = configparser.ConfigParser()
config.read('config.ini')
limiter = Limiter(app, default_limits=["500kb/s"])



@app.route('/', methods=['GET'])
def home():
    container_id = socket.gethostname()
    return render_template('index.html', container_id=container_id)


@app.route('/download')
@limiter.limit("10Mb/s")
def download():
    #file_path =  'file.pdf'
    file_path =  'bigfile.mp4'
    #file_path =  'verybigfile.exe'

    try:
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
