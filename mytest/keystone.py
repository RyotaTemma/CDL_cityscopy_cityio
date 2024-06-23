import cv2
import numpy as np

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Define the four corners of the region you want to show
    corners = np.array([
  [frame.shape[1] // 2 - 100, frame.shape[0] // 2 - 100],
  [frame.shape[1] // 2 + 100, frame.shape[0] // 2 - 100],
  [frame.shape[1] // 2 + 100, frame.shape[0] // 2 + 100],
  [frame.shape[1] // 2 - 100, frame.shape[0] // 2 + 100]
], dtype='float32')

    # Define the size of the new image
    size = (800, 800)

    # Define the destination points to be a rectangle of the size specified
    dst = np.array([
      [0, 0],
      [size[0] - 1, 0],
      [size[0] - 1, size[1] - 1],
      [0, size[1] - 1]
    ], dtype='float32')

    # Use the cv2 getPerspectiveTransform function to get the transformation matrix
    M = cv2.getPerspectiveTransform( dst, corners)

    # Apply the perspective transformation
    warped = cv2.warpPerspective(frame, M, size)

    # Show the image
    cv2.imshow('Warped Image', warped)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()