from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
import cv2
import os
import warnings
warnings.filterwarnings('ignore')

recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
recognizer.read("TrainingImageLabel\Trainner.yml")

path = "C:/Users/Preethi Ayyappan/PycharmProjects/Student Attendance Ssytem Using Face Recognition/Dataset_2"
test_labels = [7,9,9,1,10,2,7,2,2,10,2,2,1,8,8,1,1,6]
# in lexicographical order of file
test_pred = []
dir_list = os.listdir(path)

for elt in dir_list:
    impath = path + '/' + elt
    print(impath)
    image = cv2.imread(impath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    label_text, score = recognizer.predict(image)
    print(score)
    test_pred.append(label_text)
print(test_labels)
print(test_pred)
print("Accuracy Score: ", accuracy_score(test_labels, test_pred))
print("Confusion Matrix:\n", confusion_matrix(test_labels, test_pred))
print("Precision:\n", precision_score(test_labels, test_pred, average='macro'))
print("Recall:\n", recall_score(test_labels, test_pred, average='macro'))