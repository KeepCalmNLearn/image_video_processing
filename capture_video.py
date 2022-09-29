import cv2, time

video=cv2.VideoCapture(0) #parameter is camera index, for laptop front camera index is 0, multiple camera will be having more indexes

no_of_frames = 1
while True:
    no_of_frames +=1
    check, frame = video.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing", gray)
    #cv2.waitKey(0) #enter any key to close window
    key=cv2.waitKey(1)

    if key==ord("q"):
        break

print(no_of_frames)
video.release()
cv2.destroyAllWindows
