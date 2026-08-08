import random

# Real version later: load YOLO model here once, at module level
# from ultralytics import YOLO
# model = YOLO(settings.YOLO_MODEL_PATH)

def detect_ppe(image_bytes: bytes) -> list[dict]:
    """
    MOCK: returns fake detections so the frontend can be built against
    a realistic response shape before the real YOLO model is wired in.
    """
    possible_labels = ["helmet", "no_helmet", "vest", "no_vest", "gloves"]
    label = random.choice(possible_labels)
    return [
        {
            "label": label,
            "confidence": round(random.uniform(0.6, 0.98), 2),
            "bbox": [50.0, 60.0, 200.0, 220.0],
        }
    ]