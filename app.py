""" Module providing main functionality to run the application"""
import tkinter as tk


def run() -> int:
    """
    Runs the application.
    """
    root = tk.Tk()
    hello_label = tk.Label(root, text="Hello in DataManagementTool")
    hello_label.pack()
    root.mainloop()
    return 0
