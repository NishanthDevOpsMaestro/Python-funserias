import cv2
import numpy as np

# Set video parameters
frame_width = 640
frame_height = 480
frame_rate = 30

# Create a VideoWriter object
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))

# Create a loop to generate frames for the video
for i in range(300):  # You can change the number of frames
    # Create a blank frame
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    # Add text to the frame
    text = f'Frame {i+1}'
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write the frame to the video
    out.write(frame)

# Release the video writer
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
