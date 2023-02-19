import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, Response
from tracking import track
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
WEIGHTS = ROOT / 'tracking' / 'weights'

# Use a service account.
cred = credentials.Certificate('khkys22-firebase-adminsdk-gxlc0-aea51764b0.json')

firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()

flask_app = Flask(__name__)

cam_urls = ['https://www.youtube.com/watch?v=ttijFPbYtjg', 'https://www.youtube.com/watch?v=SMQzTYw-10o',
            'https://www.youtube.com/watch?v=q6sqbq--T5g']


@flask_app.route('/cam/<id>')
def video_feed(id):
    return Response(
        track.run(cam_id=int(id), source=cam_urls[int(id)], yield_frame=True, yolo_weights=WEIGHTS / 'last.pt',
                  show_vid=True, exist_ok=True, save_trajectories=True, update=True),
        mimetype='multipart/x-mixed-replace; boundary=frame')


flask_app.run(host='127.0.0.1', debug=True)
