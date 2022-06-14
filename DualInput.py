from tkinter import *
from tkinter import simpledialog

class DualInput(simpledialog.Dialog):
    assignment_field = ""
    date_field = "" 

    def __init__(self, parent, title, assignment="Assignment", date="2022-01-01 00:00:00"):
        self.assignment = None
        self.date = None
        self.assignment_field = assignment
        self.date_field = date
        super().__init__(parent, title)

    def body(self, frame):

        Label(frame, text="Assignment:").grid(row=0)
        Label(frame, text="Date:").grid(row=1)

        self.assignmentEntry = Entry(frame)
        self.dateEntry = Entry(frame)

        self.assignmentEntry.insert(0, self.assignment_field)
        self.dateEntry.insert(0, self.date_field)

        self.assignmentEntry.grid(row=0, column=1)
        self.dateEntry.grid(row=1, column=1)

        return frame 

    def apply(self):
        self.assignment = self.assignmentEntry.get()
        self.date = self.dateEntry.get()