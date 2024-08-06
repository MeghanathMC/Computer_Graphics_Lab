import face_recognition

import cv2

def detect_faces(image_path):
    img=face_recognition.load_image_file(image_path)
    
    for(top,right,bottom,left) in face_recognition.face_locations(img):
        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),2)
        
        
        
    
    cv2.imshow("face Detected",cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
detect_faces("rv.jpg")