from tkinter import *
root = Tk()

# label1 = Label(root,text = "Hello world")
# label1.pack()
# root.mainloop()

# frameone = Frame(root)
# frameone.pack()
#
# frametwo = Frame(root)
# frametwo.pack(side = BOTTOM)
#
# button1 = Button(frameone,text="hi", fg="red")
# button2 = Button(frametwo,text="hello", fg="Blue")
#
# button1.pack()
# button2.pack()
#
# root.mainloop()

# # tkinter grid layout
# label1 = Label(root,text="firstname")
# label2 = Label(root,text="lastname")
#
#
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# label1.grid(row = 0,column = 0 )
# label2.grid(row = 1,column = 0 )
#
# entry1.grid(row = 0,column = 1 )
# entry2.grid(row = 1,column = 1 )
#
# root.mainloop()



# #tkinter self adjusting widgets
# label1 = Label(root,text = "Hello",bg = "black",fg = "red")
# label1.pack(fill = X)
#
# label2 = Label(root,text = "world",bg = "blue",fg = "white")
# label2.pack(fill = Y)
#
# root.mainloop()

import tkinter as tk

class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dropdown Menu Example")

        # Create a label
        self.label = tk.Label(root, text="Select an option:")
        self.label.pack()

        # Options for the dropdown menu
        self.options = ["Option 1", "Option 2", "Option 3"]

        # Variable to store the selected option
        self.selected_option = tk.StringVar(root)
        self.selected_option.set(self.options[0])  # Set default value

        # Create a dropdown menu
        self.dropdown = tk.OptionMenu(root, self.selected_option, *self.options)
        self.dropdown.pack()

        # Create a button to display the selected option
        self.button = tk.Button(root, text="Show Selection", command=self.show_selection)
        self.button.pack()

    def show_selection(self):
        selected = self.selected_option.get()
        print(f"Selected option: {selected}")

def main():
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
