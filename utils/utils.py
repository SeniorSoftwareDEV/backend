import cv2
import numpy as np
import os
from math import dist

dataset_dir_name = 'dataset'

class Grahph_similarity:
    def __init__(self, img):
        self.src = img
        self.height, self.width = self.src.shape[:2]
        self.pts = self.get_points(self.src)
        
    def get_points(self, img):
        pts = []
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0,255,cv2.THRESH_OTSU)[1]
        for i in range(4, self.width):
            idxs = np.where(gray[:, i] == 0)
            if len(idxs[0]) == 0:
                pts.append([i, 0]) 
            else:
                pts.append([i, idxs[0][0]])
        return pts
    
    def calc_error(self, pts1, pts2):
        error = 0
        for i in range(len(pts1)):
            error += dist(pts1[i], pts2[i])
        return error
    
    def main(self):
        pts_error_data = []
        for fname in os.listdir(dataset_dir_name):
            img = cv2.imread(os.path.join(dataset_dir_name, fname))
            pts_error_data.append({'name':fname, 'error': self.calc_error(self.pts, self.get_points(img))})
        errors = []
        for error in pts_error_data:
            errors.append(error['error'])
        self.min_error = min(errors)
        
        pts_error_data = sorted(pts_error_data, key=lambda data:data['error'])
        src_name = pts_error_data[0]['name']
        res = cv2.imread(os.path.join(dataset_dir_name, src_name))
        accuracy = np.round(100 - self.min_error / (self.width*self.height) * 200, 2)
        return {'img': res, 'accuracy': str(accuracy), 'fname': src_name}

