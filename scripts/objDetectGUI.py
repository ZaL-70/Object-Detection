from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import objDetection as objDetect

MAX_WIDTH = 800
MAX_HEIGHT = 450
selected_img = ""

def openImage():
    lbl_in_img.config(image=None, bg=frm_leftim.cget("bg"))  # Set the background to match the left frame's background
    lbl_in_img.image = None  # Clear the image reference
    # Clear the output image properly and reset the background color
    lbl_out_img.config(image=None, bg=frm_rightim.cget("bg"))  # Set the background to match the right frame's background
    lbl_out_img.image = None  # Clear the image reference

    global selected_img
    selected_img = filedialog.askopenfilename(title="Select jpg",
                                          filetypes=[("JPG files", "*.jpg"), ("All files", "*.*")])
    if not selected_img.lower().endswith(".jpg"):
        lbl_feedback.config(text="You must select a .jpg file")
        print("You must select a .jpg file")
        return  # Stop execution if the file is not a .jpg
    
    in_img = Image.open(selected_img) # load image
    # Resize the image to fit within the max size while maintaining aspect ratio
    in_img = resizeImage(in_img, MAX_WIDTH, MAX_HEIGHT)
    in_img = ImageTk.PhotoImage(in_img) # allow image to be displayed
    lbl_in_img.config(image=in_img) # display the image in the tkinter label
    lbl_in_img.image = in_img  # keep a reference (avoid garbage collection)
    lbl_in_img.pack()

def detectImage():
    lbl_out_img.config(image=None)
    if(selected_img):
        out_img = objDetect.detectObjV1(selected_img) # load displayable image
        out_img = resizeImage(out_img, MAX_WIDTH, MAX_HEIGHT)
        out_img = ImageTk.PhotoImage(out_img) # allow image to be displayed
        lbl_out_img.config(image=out_img) # display the image in the tkinter label
        lbl_out_img.image = out_img  # keep a reference (avoid garbage collection)
        lbl_out_img.pack()
    else:
        lbl_feedback.config(text="No image selected")
        print("No image selected")

def resizeImage(image, max_width, max_height):
    width, height = image.size # get image size
    scale = min(max_width/width, max_height/height) # make a scale depending on the original image size
    new_width = int(width*scale)
    new_height = int(height*scale)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# create main tkinter window
window = Tk()
window.title("Object Detect")
# allow main window to resize
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

frm1 = Frame(window, bg='black')
frm1.grid(row=0, sticky="nesw")
# allow frame 1 to expand when window resizes
frm1.grid_rowconfigure(1, weight=1)
frm1.grid_columnconfigure(0, weight=1)
frm1.grid_columnconfigure(1, weight=1)

# Feedback message label (frame 1)
lbl_feedback = Label(frm1, text="Object Detector", font=20)
lbl_feedback.grid(row=0, columnspan=2, padx=10, pady=5, sticky="ew")
# input image title label (frame 1)
lbl_leftim_title = Label(frm1, text="Original Image")
lbl_leftim_title.grid(row=1, column=0, padx=10, sticky="w")
# output image title label (frame 1)
lbl_rightim_title = Label(frm1, text="Output Image")
lbl_rightim_title.grid(row=1, column=1, padx=10, sticky="e")

# images group frame (frame 2)
frm2 = Frame(window, width=800, height=400, bg='black')
frm2.grid(row=1, sticky="nesw")
# allow the frame 2 to expand when window resized
frm2.grid_rowconfigure(0, weight=1)
frm2.grid_columnconfigure(0, weight=1)
frm2.grid_columnconfigure(1, weight=1)

# original image frame (frame 2)
frm_leftim = Frame(frm2, width=400, height=200, bg='light blue')
frm_leftim.grid(row=0, column=0, padx=10, sticky="nesw")
# output image frame (frame 2)
frm_rightim = Frame(frm2, width=400, height=200, bg='light green')
frm_rightim.grid(row=0, column=1, padx=10, sticky="nesw")
# input image label (frame 2)
lbl_in_img = Label(frm_leftim)
# output image label (frame 2)
lbl_out_img = Label(frm_rightim)

# buttons group frame (frame 3)
frm3 = Frame(window, bg='black')
frm3.grid(row=2, sticky="nesw")
# allow frame 3 to expand when window resizes
frm3.grid_columnconfigure(0, weight=1)
frm3.grid_columnconfigure(1, weight=1)

# image select button (frame 3)
btnSelect = Button(frm3, text="Open jpg file", command=openImage)
btnSelect.grid(row=0, column=0, padx=10, pady=5)
# object detect button (frame 3)
btnDetect = Button(frm3, text="Detect Objects", command=detectImage)
btnDetect.grid(row=0, column=1, padx=10, pady=5)

window.mainloop()
