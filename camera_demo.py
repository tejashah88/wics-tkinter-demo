import tkinter as tk
from PIL import Image
from PIL import ImageTk
import threading
import cv2
import time

window = tk.Tk()
window.title('Camera Demo')
window.geometry('640x480')


def cvloop(run_event):
    global main_panel
    video_capture = cv2.VideoCapture(0)

    while run_event.is_set():  # while the thread is active we loop
        ret, image = video_capture.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        main_panel.configure(image=image)
        main_panel.image = image

    video_capture.release()


main_panel = tk.Label(window)
main_panel.pack(padx=10, pady=10)

# Creates a thread for openCV processing
run_event = threading.Event()
run_event.set()
action = threading.Thread(target=cvloop, args=(run_event,))
action.setDaemon(True)
action.start()


# Function to clean everything up
def terminate():
    global window, run_event, action
    print("Cleaning up OpenCV resources...")
    run_event.clear()
    time.sleep(1)
    # action.join() #strangely in Linux this thread does not terminate properly, so .join never finishes
    window.destroy()
    print("All closed!")


# When the GUI is closed it actives the terminate function
window.protocol("WM_DELETE_WINDOW", terminate)
window.mainloop()  # creates loop of GUI