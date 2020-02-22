import tensorflow as tf
import os
from matplotlib import pyplot as plt
import numpy as np 
import cv2
import random
import pickle
ham_path = 'E:\HamImages\HamImages'
spam_path = 'E:\HamImages\SpamImages'
DATA_DIR = 'E:\HamImages'
categeories = ["HamImages","SpamImages"]
training_data =[]
X = []
y = []
img_size = 200
def create_training_data():
    for x in categeories:
        path = os.path.join(DATA_DIR,x)
        class_num = categeories.index(x)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img))
                new_array = cv2.resize(img_array,(img_size,img_size))
                training_data.append([new_array,class_num])
            except Exception as e:
                print(e)
                pass
create_training_data()
print(len(training_data))
random.shuffle(training_data)
for sample in training_data[:10]:
    print(sample[1])
for features,labels in training_data:
    X.append(features)
    y.append(labels)
X = np.array(X).reshape(-1,img_size,img_size,3)
pickle_out = open("x.pickle","wb")
pickle.dump(X,pickle_out)
pickle_out.close()
pickle_in = open("x.pickle","rb")
pickle_out1 = open("y.pickle","wb")
pickle.dump(y,pickle_out1)
pickle_out1.close()
