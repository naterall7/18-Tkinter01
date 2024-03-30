import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")
label_name = tk.Label(window, text = "Name", background = "#000000", foreground = "#64e8c9")
label_name.pack()
entry_name = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_name.pack()
label_address1 = tk.Label(window, text = "Address Line 1", background = "#000000", foreground = "#64e8c9")
label_address1.pack()
entry_address1 = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_address1.pack()
label_address2 = tk.Label(window, text = "Address Line 2", background = "#000000", foreground = "#64e8c9")
label_address2.pack()
entry_address2 = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_address2.pack()
label_city = tk.Label(window, text = "City", background = "#000000", foreground = "#64e8c9")
label_city.pack()
entry_city = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_city.pack()
label_state = tk.Label(window, text = "State", background = "#000000", foreground = "#64e8c9")
label_state.pack()
entry_state = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_state.pack()
label_zip = tk.Label(window, text = "Zip Code", background = "#000000", foreground = "#64e8c9")
label_zip.pack()
entry_zip = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_zip.pack()
label_phone = tk.Label(window, text = "Phone Number", background = "#000000", foreground = "#64e8c9")
label_phone.pack()
entry_phone = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_phone.pack()
label_email = tk.Label(window, text = "Email Address", background = "#000000", foreground = "#64e8c9")
label_email.pack()
entry_email = tk.Entry(window, background = "#000000", foreground = "#64e8c9")
entry_email.pack()
button = tk.Button(window, text = "Submit", background = "#000000", foreground = "#64e8c9")
button.pack()
window.mainloop()