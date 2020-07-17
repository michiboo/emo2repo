from flask import Flask, render_template, request, redirect, url_for, Response, stream_with_context, send_from_directory
import face_recognition
import os, time, re
import cv2.cv2 as cv2, numpy as np
import keras
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model
import tensorflow as tf
import random
import requests

global model
global graph
global sess
sess = tf.compat.v1.Session()
graph = tf.compat.v1.get_default_graph()
# model = load_model(".hdf5") # put your model path
UPLOAD_FOLDER = './imgs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'WebP'])
app = Flask(__name__)


@app.route('/video/emo/', methods=['GET'])
def get_emo_video():
    time.sleep(0.5)
    cap = cv2.VideoCapture('rtsp://192.168.1.146:1234/test') # here input your streaming server IP address 
    while not cap.isOpened():
        pass
    res = []
    count = 0
 
    while True:
        ret, img = cap.read()
        if ret:  
            e = None 
            cv2.imwrite('out.png', np.rot90(img))
            e = emo_recognition(np.rot90(img))
            if e:
                res.append(e)
                count += 1
        if count > 10 or res:
            break
    cap.release()
    print(res)
    return max(res).lower()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def emo_recognition(img):
    emots = {'Angry': 0, 'Disgust': 1, 'Fear': 2, 'Happy': 3, 'Neutral': 4, 'Sad': 5, 'Surprise': 6}
   
    face_locations = face_recognition.face_locations(img)
    if not face_locations:
        print('no face')
        return None
    img = cv2.resize(img, (48,48))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.reshape(img, [1, img.shape[0], img.shape[1], 1])
    with graph.as_default():
        set_session(sess)
        cur_loc = os.path.dirname(os.path.realpath(__file__))
        model = load_model(f"{cur_loc}/model_v6_23.hdf5")
        em_class = np.argmax(model.predict(img))
    label_display = dict((a,b) for b,a in emots.items())
    pred_label = label_display[em_class]
    
    return pred_label.lower() # predicted label


# get music by emotion category
@app.route('/music/<path:foldername>')
def download_file(foldername):
    cur_loc = os.path.dirname(os.path.realpath(__file__))
    filename = random.choice([x for x in os.listdir(f"{cur_loc}/music/{foldername}") if os.path.isfile(os.path.join(f"{cur_loc}/music/{foldername}", x))])
    return send_from_directory(f'{cur_loc}/music/{foldername}', filename)

@app.route('/repo/<path:foldername>')
def get_repo(foldername):
    cur_loc = os.path.dirname(os.path.realpath(__file__))
    with open(f"{cur_loc}/repos/{foldername}.txt", 'r') as repofile:
        repos = repofile.readlines()
    repo = random.choice(repos)
    return repo

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.1.146', port=1235, threaded=True)
    # img = cv2.imread('out.png')
    