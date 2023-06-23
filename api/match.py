import cv2
import numpy as np
import base64
from api.config import app
from flask import request, jsonify
from utils.utils import Grahph_similarity
@app.route("/match", methods=["POST"])
def match():
    ori_img = request.form['inputImg'].split(',')[1]
    ori_img = np.fromstring(base64.b64decode(ori_img), np.uint8)
    ori_img = cv2.imdecode(ori_img, cv2.IMREAD_COLOR)
    model = Grahph_similarity(ori_img)
    result = model.main()
    res = result['img']
    retval, buffer = cv2.imencode('.jpg', res)
    res_img = base64.b64encode(buffer)
    result['img'] = f'{res_img}'
    
    return result