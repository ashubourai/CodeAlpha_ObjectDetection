
import cv2
from ultralytics import YOLO

# Load YOLOv8n model
model = YOLO('yolov8n.pt')

# Load video file
cap = cv2.VideoCapture('sample_video.mp4')

# Define video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))  # Resize for better performance

    # Run YOLO detection
    results = model(frame, stream=True, verbose=False)

    # Draw detections
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        confidences = result.boxes.conf.cpu().numpy()
        class_ids = result.boxes.cls.cpu().numpy()

        for bbox, conf, cls_id in zip(boxes, confidences, class_ids):
            x1, y1, x2, y2 = map(int, bbox)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {int(cls_id)} Conf: {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show frame
    cv2.imshow('YOLOv8 Object Detection (Video Input)', frame)

    # Save frame to output video
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
