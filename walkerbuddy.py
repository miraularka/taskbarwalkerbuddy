# .--------------------------------------------.
# | Taskbar Walker Buddy                       |
# | Inspired by a script on Acmlmboard/board2  |
# |                             ~Mirau 2024    |
# '--------------------------------------------'
from tkinter import *
from tkinter import ttk
from ctypes import windll, wintypes, byref
from PIL import Image, ImageTk
from random import *
import os, time, base64

#Initialization and Common Variable Declaration
version = 0.3
root = Tk()
root.title('Taskbar Walker Buddy')
root.tk_setPalette("lightgrey")
root.wm_overrideredirect(1)
root.wm_attributes("-transparentcolor","lightgrey")
SPI_GETWORKAREA = 0x0030
desktop_area = wintypes.RECT()
_ = windll.user32.SystemParametersInfoW(SPI_GETWORKAREA,0,byref(desktop_area),0)
screen_width = root.winfo_screenwidth()
screen_height = desktop_area.bottom
actor_size = 32 #32 pixels gives plenty of space for most sprites
root.geometry('%dx%d+%d+%d' % (screen_width, actor_size, 0, screen_height-actor_size))
current_sprite = 2
clicked = False
option_spawn_loc = IntVar()
option_spawn_loc.set(2)
option_count = 0
option_repeat = IntVar()
option_repeat.set(0)
option_delay = IntVar()
option_delay.set(50)
style = ttk.Style()
style.configure('Horizontal.TScale', background='grey')
lbl_cli = Label()


class Misc:
    MIRAU_HEAD = r"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"
    LICENSE = """
    Taskbar Walker Buddy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

    Taskbar Walker Buddy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

    To receive a copy of the GNU General Public License please visit: https://www.gnu.org/licenses/
    """

#Load Spritesheets
spritelist = []
for filename in os.listdir("img/"):
    sheet = Image.open("img/"+filename)
    sheet = ImageTk.PhotoImage(sheet)
    spritelist.append(sheet)
mirau=PhotoImage(data=Misc.MIRAU_HEAD)

def about_window(event):
    about= Toplevel(root)
    about.geometry("350x300+%d+%d" % (screen_width/2-175, screen_height/2-200))
    about.title("About Taskbar Walker Buddy")
    about.resizable(False, False)
    about.attributes('-toolwindow',True)
    lbl_mir = Label(about, image=mirau).pack(pady=(actor_size/2,0))
    lbl_twb = Label(about, text='Taskbar Walker Buddy', font=('Helvetica',20,'bold')).pack()
    lbl_cop = Label(about, text='v'+str(version)+' - Copyright © 2024 - Mirau', font=('Helvetica',8)).pack()
    fra_opt = Frame(about,bg='grey',highlightbackground='black',highlightthickness=1, width=340, height=200)
    fra_opt.pack(side=BOTTOM, pady=(0,8))
    fra_opt.pack_propagate(0)
    global lbl_cli
    lbl_cli = Label(fra_opt, text='Total of '+str(option_count)+' active walkers clicked.', bg='grey', font=('Helvetica',10))
    lbl_cli.pack()
    fra_but = Frame(fra_opt, bg='grey')
    fra_but.pack(side=BOTTOM, pady=(2,4))
    but_lisc = Button(fra_but, text='License', width=10, command=license_window).grid(row=1, column=0, padx=2)
    but_quit = Button(fra_but, text='Quit', width=10, command=quit).grid(row=1, column=1, padx=2)
    fra_side = Frame(fra_opt,bg='grey')
    fra_side.pack(side=BOTTOM)
    rad_side1 = Radiobutton(fra_side,text='Spawn Left',bg='grey',activebackground='grey',variable=option_spawn_loc, value=0).grid(row=2, column=0)
    rad_side2 = Radiobutton(fra_side,text='Spawn Both',bg='grey',activebackground='grey',variable=option_spawn_loc, value=2).grid(row=2, column=1)
    rad_side0 = Radiobutton(fra_side,text='Spawn Right',bg='grey',activebackground='grey',variable=option_spawn_loc, value=1).grid(row=2, column=2)
    
    chk_rep = Checkbutton(fra_side, text='Force Specific Walker',bg='grey',activebackground='grey',variable=option_repeat).grid(row=1, column=1)
    sca_del = ttk.Scale(fra_opt, from_=0, to=500, variable=option_delay, value=option_delay.get(), command=update_delay_scale, length=250)
    sca_del.pack(side=BOTTOM)
    global lbl_del
    lbl_del = Label(fra_opt, text='Delay Timer: '+str(option_delay.get())+'ms (default 50)', bg='grey', font=('Helvetica',10))
    lbl_del.pack(side=BOTTOM)
    
def license_window():
    license= Toplevel(root)
    license.geometry("300x260+%d+%d" % (screen_width/2-150, screen_height/2-130))
    license.title("License")
    license.resizable(False, False)
    license.attributes('-toolwindow',True)
    fra_lic = Frame(license,bg='grey',highlightbackground='black',highlightthickness=1, width=290, height=240)
    fra_lic.pack(side=TOP, pady=4)
    fra_lic.pack_propagate()
    lbl_lic = Label(fra_lic, text=Misc.LICENSE, wraplength=284, justify=LEFT, bg='grey', font=('Helvetica',8))
    lbl_lic.pack(side=TOP)
    but_close = Button(license, text='Close', width=10, command=lambda:license.destroy())
    but_close.pack(side=BOTTOM, pady=(0,4))

def quit():
    root.destroy()

def update_delay_scale(event):
    global lbl_del
    lbl_del["text"]='Delay Timer: '+str(option_delay.get())+'ms (default 50)'

def shuffle_actor():
    global actor, current_sprite
    if option_repeat.get()==0:
        current_sprite = randrange(0,len(spritelist))
    actor.config(image=spritelist[current_sprite])

def animate(dir, Ax=0,Ay=0):
    global actor
    if clicked==False:
        Ax = actor.winfo_x()-actor_size if actor.winfo_x() > -abs(spritelist[current_sprite].width()-actor_size) else 0
    if dir=='left': Ay=0
    if dir=='right': Ay=-abs(actor_size)
    if dir=='click': Ay=-abs(actor_size*2)        
    actor.place(x=Ax,y=Ay-2) #-2 accounts for frame padding

def interact(event):
    global clicked, actor, option_count, lbl_cli
    actor.place(x=0)
    clicked=True
    option_count=option_count+1
    lbl_cli["text"]='Total of '+str(option_count)+' active walkers clicked.' #live update in About

def reset():
    global frame
    if option_spawn_loc.get()==2:
        frame.place(x=-abs(actor_size*2+option_delay.get())) if randrange(2)%2==0 else frame.place(x=screen_width+option_delay.get()+actor_size)
    else:
        if option_spawn_loc.get()==1: frame.place(x=screen_width+option_delay.get()+actor_size)
        if option_spawn_loc.get()==0: frame.place(x=-abs(actor_size*2+option_delay.get()))
    shuffle_actor()

def actor_walk(dir='right',speed=2,timer=0):
    global frame, clicked
    if frame.winfo_x() > screen_width+option_delay.get(): dir='left'
    if frame.winfo_x() < -abs(actor_size+option_delay.get()): dir='right'
    move = (-abs(speed) if dir=='left' else abs(speed))
    if clicked==True: dir='click'
    animate(dir)
    if actor.winfo_y()==-abs(actor_size*2+2): move = 0
    if clicked==True: root.after(int((spritelist[current_sprite].width()/actor_size)*100),reset); clicked=False
    frame.place(x=frame.winfo_x()+move)
    root.after(100,actor_walk,dir,speed)

frame = Frame(root)
frame.place(x=-abs(option_delay.get()),y=0, width=actor_size, height=actor_size)

actor = Label(frame, image = spritelist[current_sprite])
actor.place(x=0,y=0)
actor.bind("<Button-1>", interact)
actor.bind("<Button-3>", about_window)

actor_walk()
root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop()