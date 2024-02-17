import cv2
import numpy

def detect_eyes(img, img_gray, classifier):
    coords = cascade.detectMultiScale(img_gray, 1.3, 5)# detect eyes
    height = np.size(image, 0) # get face frame height
    for (x, y, w, h) in coords:
        if y+h > height/2: # pass if the eye is at the bottom
            pass

def detect_eyes(img, classifier):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5) # detect eyes
    width = np.size(image, 1) # get face frame width
    height = np.size(image, 0) # get face frame height
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye

    
def detect_faces(img, classifier):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
    return frame



def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
    return img

def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    print(keypoints)
    return keypoints

def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('image')
    cv2.createTrackbar('threshold', 'image', 0, 255, nothing)
    while True:
        _, frame = cap.read()
        face_frame = detect_faces(frame, face_cascade)
        if face_frame is not None:
            eyes = detect_eyes(face_frame, eye_cascade)
            for eye in eyes:
                if eye is not None:
                    threshold = cv2.getTrackbarPos('threshold', 'image')
                    eye = cut_eyebrows(eye)
                    keypoints = blob_process(eye, threshold, detector)
                    eye = cv2.drawKeypoints(eye, keypoints, eye, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def nothing(x):
    pass



detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread("your_image_name.jpg")

gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#make picture gray
faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

#cv2.imshow('my image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

gray_face = gray_picture[y:y+h, x:x+w] # cut the gray face frame out
face = img[y:y+h, x:x+w] # cut the face frame out
eyes = eye_cascade.detectMultiScale(gray_face)

color_threshold = 68
_, img_tracked = cv2.threshold(gray_face, color_threshold, 255, cv2.THRESH_BINARY)

for (ex,ey,ew,eh) in eyes: 
    cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2)


#, eyes2 = eye_cascade.detectMultiScale(img_tracked)


#cv2.imshow('my image', img_tracked)
##cv2.waitKey(0)
#cv2.destroyAllWindows()



cut_eyebrowsOff = cut_eyebrows(img_tracked)


cv2.imshow('my image', img_tracked) #error here
cv2.waitKey(0)
cv2.destroyAllWindows()
