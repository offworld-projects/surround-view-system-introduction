import numpy as np
import cv2
import time

class StreamSingleImage(object):
    def __init__(self, image_file=None, rate=None):
        self.image = cv2.imread(image_file)
        self.period = 1./rate
        self.last_time_read = None
        
    def isOpened(self):
        return self.image is not None
    
    def read(self, image=None):
        if self.image is None:
            return False, None
        if not image:
            return True, self.image.copy()
        np.copyto(image, self.image)
        return True, image

    def grab(self):
        current_time = time.time()
        if self.last_time_read is None or current_time - self.last_time_read >= self.period:
            self.last_time_read = current_time
            return True
        return False
    
    def retrieve(self):
        return True, self.image
    
    def release(self):
        self.image = None

    def set(self, prop, val):
        # this method just needs to be implemented; it doesn't need to do anything
        pass

    def get(self):
        return self.image.shape[0], self.image.shape[1] 
