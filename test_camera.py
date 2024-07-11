import cv2

def test_camera():
    cap = cv2.VideoCapture(0)  # Try to open the default camera (device 0)

    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('Frame', frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Properly release the capture object
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_camera()
