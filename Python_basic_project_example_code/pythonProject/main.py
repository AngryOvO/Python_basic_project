# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *
window = Tk()

if __name__ == '__main__':





    photo = PhotoImage(file= "cat.gif")
    photo2 = PhotoImage(file= "cat2.gif")

    label1 = Label(window, image=photo)

    label2 = Label(window, image=photo2)


    label2.pack(side=LEFT)
    label1.pack()


    window.mainloop()

