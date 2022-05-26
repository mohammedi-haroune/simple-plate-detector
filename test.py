""" import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk

video_name = "video.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    for image in video.iter_data():
        open    
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

if __name__ == "__main__":

    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop() """

status1 = [['Hamid', "Rahimi", '1998', '13:40'], ['Karim', "Sabri", '405', '13:40'], ['Abdelrahman', "Mrabet", '525', '13:40'], ['Salim', "Ghamel", '309', '13:40']]


import re
import string
from PlateDetection import main
import tkinter
from tkinter import BOTH, CENTER, INSERT, NORMAL, ttk
import cv2
import PIL.Image, PIL.ImageTk
import time
class App:
    def __init__(self, window, window_title, video_source="video.mp4"):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = 2000, height = 600)
        self.canvas.pack()


        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor="s")

        self.text = tkinter.Text(width = 50, height = 50, borderwidth=1, bg="grey", state=NORMAL)
        self.text.tag_configure("tag_name", justify='center')
        self.text.pack(expand=0)



        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        
        if ret:
            frame_name = "snapshots/" + "frame-"  + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
            cv2.imwrite(frame_name, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            img = cv2.imread(frame_name)
            cropped_image = img[250:546, 373:907]
            cv2.imwrite("cropped.jpg", cropped_image)
            plate = main()
            plate.replace(" ", "")
            if plate != "":
                pattern = r'[' + string.punctuation + ']'
                plate = re.sub(pattern, '', plate)
            else:
                plate = None
            self.text.insert(tkinter.INSERT, plate)


    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source="video.mp4"):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                 return (ret, None)
        else:
            return (ret, None)
 
     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")