from tkinter import *
import pyshorteners

root = Tk()
root.title('Naveen Link Shortner')
root.geometry("500x600")
# root.iconbitmap('C:/Users/ASUS/Downloads/iconforproject.ico')
def shorten():
	if shorty.get():
		shorty.delete(0, END)
		
	if my_entry.get():
		# Convert to tinyurl
		url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
		# Output to screen
		shorty.insert(END, url)
		# Reverse URL
		# print(pyshorteners.Shortener().tinyurl.expand(url))
		# type_bitly = pyshorteners.Shortener(api_key='439bbac124e081dcf7ff9d5de9dcd4e2752f2bba')
		# print(type_bitly.bitly.short(url))
#second shortner function
def shorten2():
	if shorty2.get():
		shorty2.delete(0, END)
		
	if my_entry2.get():
		# Convert to tinyurl
		url = pyshorteners.Shortener().tinyurl.short(my_entry2.get())
		# Output to screen
		# Reverse URL
		# print(pyshorteners.Shortener().tinyurl.expand(url))
		type_bitly = pyshorteners.Shortener(api_key='439bbac124e081dcf7ff9d5de9dcd4e2752f2bba')
		url=type_bitly.bitly.short(url)
		shorty2.insert(END, url)

 #shorten 1

my_label = Button(root, text="Please Enter The Url You Want To Shorten", font=("Times New Roman", 14),borderwidth=5, bg="#000000",fg="blue",state=DISABLED)
my_label.pack(pady=16)
Label(root, text="------------------------------------------------------------", bg="#ffffe0", fg="#4a4140", font="verdana 12 ").place(x=25, y=60)
my_entry = Entry(root,font=("Helvetica", 14))
my_entry.pack(pady=20)
Label(root, text="------------------------------------------------------------", bg="#ffffe0", fg="#4a4140", font="verdana 12 ").place(x=30, y=130)
my_button = Button(root, text="Shorten Link", command=shorten, font=("Helvetica", 15))
my_button.pack(pady=16)

shorty_label = Label(root, text="Shortened Link will appear below", font=("Helvetica", 14))
shorty_label.pack(pady=20)

shorty = Entry(root, font=("Helvetica", 16), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=10)
#shorten 2

my_label2 = Button(root, text="Please Write Url Below For Bitly", font=("Times New Roman", 14),borderwidth=5, bg="#000000",fg="blue",state=DISABLED)
my_label2.pack(pady=12)
Label(root, text="------------------------------------------------------------", bg="#ffffe0", fg="#4a4140", font="verdana 12 ").place(x=25, y=380)
my_entry2 = Entry(root,font=("Helvetica", 14))
my_entry2.pack(pady=16)
my_button = Button(root, text="Shorten Link Bitly", command=shorten2, font=("Helvetica", 15))
my_button.pack(pady=16)
shorty2 = Entry(root, font=("Helvetica", 16), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty2.pack(pady=10)
Label(root,text="Copyright Naveen", font= ("Times New Roman",12)).place(x=350, y=550)

root.mainloop()

# Naveen Project