from tkinter import*
from tkinter import messagebox
import pyqrcode


ws = Tk()
ws.title("AIDS-2 B oops")
ws.config(bg="purple")

def generate_QR():
    if len(user_input.get())!=0:
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning','All fields are required!')
    try:
        display_code()
    except:
        pass
def display_code():
    img_lbl.config(image=img)
    output.config(text="QR code of"+user_input.get())
    
lbl=Label(ws,text="Enter message-aids or URL",bg='blue')
lbl.pack()
user_input = StringVar()
entry = Entry(ws,textvariable = user_input)
entry.pack(padx=10)

button=Button(ws,text = "Generate qrcode",width=20,command=generate_QR)
button.pack(pady=20)

img_lbl=Label(ws,bg='green')
img_lbl.pack()
output = Label(ws,text = "",bg='pink')
output.pack()

ws.mainloop()
