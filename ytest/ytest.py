import cv2
import torch
import time
import os

model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)
model.conf = 0.01

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("WebCam 열기 실패")
    exit()
    
save_dir = 'person_frames'
os.makedirs(save_dir, exist_ok=True)

win = 'WebCam YOLO Monitor'
cv2.namedWindow(win)
def nothing(x):
    pass
cv2.createTrackbar('Conf %', win, 50, 100, nothing)

names = model.names

while True:
    ret, frame = cam.read()
    if not ret:
        break

    t = cv2.getTrackbarPos('Conf %', win) / 100.0

    results = model(frame)
    df = results.pandas().xyxy[0]

    df = df[(df['confidence'] >= t) & (df['name'] == 'person')]

    if not df.empty:
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        fname = os.path.join(save_dir, f'person_{timestamp}.jpg')
        cv2.imwrite(fname, frame)
        print(f"[{timestamp}] Person detected → saved {fname}")

    disp = frame.copy()
    for _, row in df.iterrows():
        x1, y1, x2, y2 = map(int, row[['xmin','ymin','xmax','ymax']])
        conf = row['confidence']
        label = f"person {conf:.2f}"
        cv2.rectangle(disp, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(disp, label, (x1, y1-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    cv2.imshow(win, disp)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
