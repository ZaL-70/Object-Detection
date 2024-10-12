import cv2
import cvlib
from cvlib.object_detection import draw_bbox
from PIL import Image, ImageTk

def detectObjV1(filepath):
    # read the image file in
    image = cv2.imread(filepath)

    # perform object detection
    bbox, labels, counts = cvlib.detect_common_objects(image)

    # draw boxes around objects
    output = draw_bbox(image, bbox, labels, counts)

    # convert opencv img format to tkinter rgb
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    # convert tkinter to PIL img
    img_pil = Image.fromarray(output_rgb)

    return img_pil