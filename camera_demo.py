import time
import threading
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2

# Prepare the window
window = tk.Tk()
window.title('Camera Demo')
window.geometry('640x480')

# Creates a thread for openCV processing
def start_as_background_task(loop_function):
    run_event = threading.Event()
    run_event.set()
    action = threading.Thread(target=loop_function, args=(run_event,))
    action.setDaemon(True)
    action.start()

    return run_event

# This is the infinite loop where we display the camera feed
def cvloop(run_event):
    global main_panel
    camera = cv2.VideoCapture(0)

    # Run while the app hasn't been terminated
    while run_event.is_set():
        # Read an image from the camera feed
        _, image = camera.read()

        # Convert it from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Prepare it for displaying on tkinter
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        display.configure(image=image)
        display.image = image

    camera.release()

# Main widget for holding the camera feed
display = tk.Label(window)
display.pack(padx=10, pady=10)

# This is needed for the GUI to display the camera feed properly
run_event = start_as_background_task(cvloop)

# Clean everything up when the user wants to quit
def terminate():
    global window, run_event
    run_event.clear()
    time.sleep(.5)
    window.destroy()
    print("Bye!")

# When the GUI is closed it calls the terminate() function
window.protocol("WM_DELETE_WINDOW", terminate)

# Show the GUI
window.mainloop()
