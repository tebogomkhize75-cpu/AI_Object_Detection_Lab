import cv2


camera = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_path = r"C:\Users\Tebog\Downloads\AI_Object_Detection_Lab\webcam_capture.py\videos\output.avi"
out = cv2.VideoWriter(video_path, fourcc, 20.0, (640,480))

img_counter = 0

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    
    cv2.imshow("Webcam", frame)

    
    out.write(frame)

    key = cv2.waitKey(1)

    
    if key % 256 == 32:
        img_name = r"C:\Users\Tebog\Downloads\AI_Object_Detection_Lab\webcam_capture.py\videos_" + str(img_counter) + ".png"
        cv2.imwrite(img_name, frame)
        print("Image saved:", img_name)
        img_counter += 1

    
    elif key % 256 == 27:
        print("Video saved:", video_path)
        break

camera.release()
out.release()
cv2.destroyAllWindows()