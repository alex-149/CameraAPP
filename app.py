import cv2
import time

def capture_image():
    # Open the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            # Capture a frame from the camera
            ret, frame = cap.read()

            # Display the captured frame (optional)
            cv2.imshow('Camera', frame)

            # Save the captured frame as an image file (you can change the filename as needed)
            filename = f"image_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)

            # Wait for 1 minute (60 seconds)
            time.sleep(1)

            # Break the loop if the user presses 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the camera and close the OpenCV window
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
