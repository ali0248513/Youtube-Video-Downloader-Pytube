from pytube import YouTube
from tkinter import *
import ctypes as ct

win = Tk()
win.geometry("600x600")
win.title('YT Video Downloader')
win.resizable(width=False, height=False)
#win.configure(bg= 'honeydew2')

c = Canvas(win, bg="gray16")
filename=PhotoImage(file="D:\\Sublime Text 3\\PROJECTS\\YTDownloader\\12.png")
background_label= Label(win, image= filename)
background_label.place(x=0,y=0,relwidth=1, relheight=1)

def get_link():
	yt = link.get()
	yt = YouTube(yt)
	txt =yt.title
	yd = yt.streams.get_highest_resolution()

	title_l = Label(win, text= "Video Title", font= 20,fg = 'red', bg = '#10222F')
	title_l.grid(column=0, row = 1, sticky= 'w')

	title_l = Label(win,text = txt, fg = 'light blue', bg = '#10222F')#'DodgerBlue4' )
	title_l.grid(column=1, row=1)
	
	dp_l = Label(win, text ="Enter Download Path" , font= 20,fg = 'red', bg = '#10222F')
	dp_l.grid(column=0 , row=2, sticky = 'w')
	
	d_path = Entry(win, width= 48,fg = '#E6B3CD', bg = '#10222F')
	d_path.grid(column=1 , row=2)
	
	def d_p():
		yd.download(d_path.get())

	d_button = Button(text= 'Go!' ,font= (20), command= d_p, fg= 'green', bg = '#10222F')
	d_button.grid(column=2 , row=2, sticky= 'E')


link_l = Label(text='Enter Link' ,font= 20,fg = 'red', bg = '#10222F')
link_l.grid(column=0 , row=0, sticky = 'w')

link = Entry(win, width= 48,fg = '#E6B3CD', bg = '#10222F')
link.grid(column=1 , row=0)


l_button= Button(text="Enter" , font=(20),fg= 'green', bg = '#10222F', command= get_link)
l_button.grid(column= 2, row= 0, sticky= 'E')


win.mainloop()