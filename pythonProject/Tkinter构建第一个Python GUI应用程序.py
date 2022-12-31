import tkinter as tk
import time as t
window = tk.Tk()
label = tk.Label(text="NAME",
                    foreground ="white",
                    background = "black",
                    width = 10,
                    height=10
                    )
button = tk.Button(text="Click me!",
                     width=25,
                     height=15,
                     bg="blue",
                     fg="yellow"
                     )
entry = tk.Entry()
label.pack()
button.pack()
entry.pack()
name = entry.get()
window.mainloop()
# t.sleep(3)
#
# entry.delete(0)
print(name,1)

