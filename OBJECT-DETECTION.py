import tkinter as tk
import pyttsx3
from ultralytics import YOLO

# Function to close the window
def close_window():
    root.destroy()

# Function to speak the given text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Create the main application window
root = tk.Tk()

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Run inference on the source
results = model(source=0, show=True, conf=0.4, save=True) # generator of Results objects

# Create a button to close the window
close_button = tk.Button(root, text="Close Window", command=close_window)
close_button.pack()

# Text to be spoken
text_to_speak = "YOLO inference completed!"

# Speak the text when the Tkinter window appears
speak_text(text_to_speak)

# Start the Tkinter event loop
root.mainloop()
