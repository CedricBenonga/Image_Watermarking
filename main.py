import os
import tkinter
from tkinter import *
from tkinter import filedialog, colorchooser
from PIL import Image, ImageGrab

# Screen
window = Tk()
window.title("© Cedric Benonga")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)
window.configure(bg="#408080")


def reset():
    canvas.itemconfig(image, image="")
    canvas.itemconfig(text, fill=f"#fff")
    canvas.itemconfig(text, text="Please upload your image!", font="calibri 15 bold", fill="#408080")
    canvas.moveto(text, 100, 230)


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())
    canvas.itemconfig(text, font=f"calibri {spinbox.get()} bold")


# upload image
def upload_image(event=None):
    global nw_img, im, nw_img_loaded
    nw_img_loaded = filedialog.askopenfilename(filetypes=[("png", ".png"),
                                                          ("gif", ".gif"),
                                                          ("bitmap", "bmp"),
                                                          ("jpeg", ".jpg")])

    im = Image.open(nw_img_loaded)
    width, height = im.size

    old_width = width
    old_height = height

    nw_width = canvas.winfo_width()
    nw_height = canvas.winfo_height()

    # resize canvas
    canvas.configure(width=nw_width, height=nw_height)
    # format and resize image
    nw_img = tkinter.PhotoImage(file=nw_img_loaded, width=old_width, height=old_height, master=window)

    # Upload new image
    # "nw_img" needs to be held as a global variable to avoid the crack, and it can't be empty.
    canvas.itemconfig(image, image=nw_img)


def choose_color():
    color = colorchooser.askcolor(color=None)
    print(color)
    canvas.itemconfig(text, fill=f"{color[1]}")
    return f"{color[1]}"


def up():
    global txt_x, txt_y
    txt_y -= 5
    canvas.moveto(text, txt_x, txt_y)


def down():
    global txt_x, txt_y
    txt_y += 5
    canvas.moveto(text, txt_x, txt_y)


def left():
    global txt_x, txt_y
    txt_x -= 5
    canvas.moveto(text, txt_x, txt_y)


def right():
    global txt_x, txt_y
    txt_x += 5
    canvas.moveto(text, txt_x, txt_y)


# save image
def download_image():

    filename = filedialog.asksaveasfilename(title="Create Image",
                                            defaultextension="png",
                                            filetypes=[("png", ".png"),
                                                       ("gif", ".gif"),
                                                       ("bitmap", "bmp"),
                                                       ("jpeg", ".jpg")])
    if filename:
        if os.path.exists(filename):
            print("Name already exists!")
        else:
            path, file = os.path.split(filename)
            name, ext = os.path.splitext(file)
            if ext.lower() in ['.gif', '.png']:
                # Standard way of calculating widget dimensions
                x1 = window.winfo_rootx() + canvas.winfo_x()
                y1 = window.winfo_rooty() + canvas.winfo_y()
                x2 = x1 + canvas.winfo_width()
                y2 = y1 + canvas.winfo_height()
                # Extract image
                saved_img = ImageGrab.grab().crop((x1, y1, x2, y2))
                # And save it
                saved_img.save(filename)
                print(f"Saved image {file}")
            else:
                print("Unknown file type")
    else:
        print("Cancel")


def change_text():
    watermark_text = text_input.get()
    canvas.itemconfig(text, text=watermark_text)
    return watermark_text


nw_img = "123"
im = "000"
nw_img_loaded = "111"
txt_x = 220
txt_y = 230

# Set up canvas
canvas = Canvas(width=440, height=460)
img = PhotoImage(file="")
image = canvas.create_image(220, 230, image=img)
text = canvas.create_text(txt_x, txt_y, text="Please upload your image!", font="calibri 15 bold", fill="#408080")
canvas.grid(column=0, columnspan=7, row=1, rowspan=8)

# Reset button
reset_button = Button(text="Reset App", command=reset)
reset_button.grid(column=9, row=3)

# App Title
label = Label(text="Image Watermarking App", font=("Ariel", 20, "bold"))
label.config(bg="#408080")
label.grid(column=0, row=0)

# Text label
label1 = Label(text=" ", font=("Ariel", 13, "bold"))
label1.config(bg="#408080")
label1.grid(column=0, row=9)

# Upload button
upload_button = Button(text='Upload Image', command=upload_image)
upload_button.config()
upload_button.grid(column=8, row=2, padx=10)  # padding inside grid creates margin

# Text color button
color_button = Button(text="Text Color", command=choose_color)
color_button.grid(column=10, row=10)

# Text Direction buttons
# Text direction label
direction_label = Label(text="Text Directions", font=("Ariel", 13, "bold"))
direction_label.config(bg="#408080")
direction_label.grid(column=9, row=5)

# Up
button_up = Button(text="🔼", command=up)
button_up.grid(column=9, row=6)

# Down
button_down = Button(text="🔽", command=down)
button_down.grid(column=9, row=7)

# Left
button_left = Button(text="◀", command=left)
button_left.grid(column=8, row=6)

# Right
button_right = Button(text="▶", command=right)
button_right.grid(column=10, row=6)

# change_text button
text_button = Button(text="Upload Text", command=change_text)
text_button.grid(column=8, row=10)

# Download button
download_button = Button(text="Download", command=download_image)
download_button.grid(column=10, row=2)

# Spinbox
spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.grid(column=9, row=10)

# Spinbox Text label
spin_label = Label(text="Text Size", font=("Ariel", 13, "bold"))
spin_label.config(bg="#408080")
spin_label.grid(column=9, row=9)

# Input
text_input = Entry(width=55)
text_input.insert(END, string="Please type your text here...")
text_input.grid(column=0, columnspan=7, row=10)


mainloop()
