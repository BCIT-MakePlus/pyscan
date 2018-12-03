# Features:
# Email Parser - downloads scans from an email
# Model Classifier - loads .ply or .obj files and returns the shape of the object

from tkinter import Tk, mainloop
from controller.GUI_main_controller import main_controller

def main():
    root = Tk()
    main_controller(root)
    mainloop()

if __name__ == "__main__":
    main()
