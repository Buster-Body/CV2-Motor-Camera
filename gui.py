from tkinter import *
from PIL import Image, ImageTk
import cv2

# IMPORTANT: we cannot use pack(), place() or grid() in one window
# went with place() for the gui because we can pick specific (X,Y)
# Create an instance of TKinter Window or frame
win = Tk()


# Set the size of the window
win.geometry("900x450")

# Create a Label to capture the Video frames
label = Label(win)
#label.grid(row=0, column=0)
# this is where we move the camera view
label.place(x=300, y=0)
cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# Our up, down, left, and right button.
up = Button(win, text="Up", height=3, width=5).place(x=90, y=5)
down = Button(win, text="Down", height=3, width=5).place(x=90, y=100)
left = Button(win, text="Left", height=3, width=5).place(x=30, y=60)
right = Button(win, text="Right", height=3, width=5).place(x=150, y=60)

# Define function to show frame


def show_frames():
   # Get the latest frame and convert into Image
   ret, frame = cap.read()
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)y+h/2
   faces = face.detectMultiScale(frame, 1.3, 3)
   for (index, (x, y, w, h)) in enumerate(faces):
      center = (int(x + w / 2), int(y + h / 2))
      print(f'face {index+1} center x={center[0]}: y={center[1]}')
      frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
      frame = cv2.circle(frame, center, radius=5,
                         color=(0, 0, 255), thickness=-1)

   frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   img = Image.fromarray(frame)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image=img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(10, show_frames)


show_frames()
win.mainloop()
