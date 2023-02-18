from ultralytics import YOLO

model = YOLO(f'tracking/weights/best.pt')
results = model.train()