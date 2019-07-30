import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, colorchooser, font
import os

main_application = tk.Tk()
main_application.geometry('1000x800')
main_application.title('Gpad text editor')


# # ----------------- main menu -----------------
main_menu = tk.Menu()

#file
# file icons

new_icon = tk.PhotoImage(file="./icons2/new.png")
open_icon = tk.PhotoImage(file="./icons2/open.png")
save_icon = tk.PhotoImage(file="./icons2/save.png")
save_as_icon = tk.PhotoImage(file="./icons2/save_as.png")
exit_icon = tk.PhotoImage(file="./icons2/exit.png")



file=tk.Menu(main_menu, tearoff=False)




#edit
#edit icons

copy_icon  = tk.PhotoImage(file = "./icons2/copy.png")
cut_icon = tk.PhotoImage(file = "./icons2/cut.png")
paste_icon = tk.PhotoImage(file = "./icons2/paste.png")
find_icon = tk.PhotoImage(file = "./icons2/find.png")
clear_all_icon = tk.PhotoImage(file = "./icons2/clear_all.png")



edit =tk.Menu(main_menu,tearoff = False)









#view
#view icons
toolbar_icon = tk.PhotoImage(file = "./icons2/tool_bar.png")
statusbar_icon = tk.PhotoImage(file = "./icons2/status_bar.png")

view =tk.Menu(main_menu,tearoff = False)


#colorTheme
#themeicons
light_default_icon = tk.PhotoImage(file = "./icons2/light_default.png")
dark_icon = tk.PhotoImage(file = "./icons2/dark.png")
red_icon = tk.PhotoImage(file = "./icons2/red.png")
light_plus_icon = tk.PhotoImage(file = "./icons2/light_plus.png")
monokai_icon = tk.PhotoImage(file = "./icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file = "./icons2/night_blue.png")

colortheme =tk.Menu(main_menu,tearoff = False)


color_choice = tk.StringVar()

color_dict = {
    'light Default':('#000000','#ffffff',light_default_icon),
    'dark':('#c4c4c4','#2d2d2d',dark_icon),
    'red':('#2d2d2d','#ffe8e8',red_icon),
    'light Plus':('#474747','#e0e0e0',light_plus_icon),
    'monokai':('#d3b774','#474747',monokai_icon),
    'night blue':('#ededed','#6b9dc2',night_blue_icon)
}




#cascade
main_menu.add_cascade(label = "File",menu=file)
main_menu.add_cascade(label = "Edit",menu=edit)
main_menu.add_cascade(label = "View",menu=view)
main_menu.add_cascade(label = "ColorTheme",menu=colortheme)




# # ----------------- end menu  -----------------

# # ----------------- main toolbar -----------------
tool_bar = ttk.Label(main_application)
tool_bar.pack(fill = tk.X,side = tk.TOP)

font_tuples = font.families()
font_family = tk.StringVar()

##font box
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0, column=0, padx=10)


##font size

size_var = tk.IntVar()
size_tuple = tuple(range(8, 90, 2))
font_size = ttk.Combobox(tool_bar, width=15, textvariable=size_var, state='readonly')
font_size['values'] = size_tuple
font_size.current(size_tuple.index(16))
font_size.grid(row=0,column = 1,padx=10)

##bold button
bold_icon = tk.PhotoImage(file = "./icons2/bold.png")
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
##italic button
italic_icon = tk.PhotoImage(file = "./icons2/italic.png")
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
##underline button
underline_icon = tk.PhotoImage(file = "./icons2/underline.png")
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
##font color button
font_icon = tk.PhotoImage(file = "./icons2/font_color.png")
font_btn = ttk.Button(tool_bar,image=font_icon)
font_btn.grid(row=0,column=5,padx=5)
##alignLeft button
align_left_icon = tk.PhotoImage(file = "./icons2/align_left.png")
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
##align center button
align_center_icon = tk.PhotoImage(file = "./icons2/align_center.png")
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
##align_right button
align_right_icon = tk.PhotoImage(file = "./icons2/align_right.png")
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

# # ----------------- end toolbar  -----------------

# # ----------------- main text editor -----------------


text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.focus_set()
text_editor.pack(fill=tk.BOTH,expand = True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font_family and font_size functionality

current_font_family = 'Arial'
current_font_size = 16
text_property = font.Font(font = text_editor['font'])
def change_font_size(main_application):
    global current_font_size
    global text_property
    global current_font_family
    current_font_size = size_var.get()
    print(text_property.actual()['weight'])
    text_editor.configure(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)

def change_font_family(main_application):
    global current_font_family
    global text_property
    global current_font_size
    current_font_family = font_family.get()
    # print(current_font_size)
    text_editor.configure(font=(current_font_family,current_font_size))
    
font_box.bind('<<ComboboxSelected>>',change_font_family)
    


## button functionalities
# print(font.Font(font = text_editor['font']).actual())
#bold button functionality
def change_boldness():
    global text_property
    text_property = font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        # text_property.actual()['weight'] = 'bold'
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    elif text_property.actual()['weight'] == 'bold':
        # text_property.actual()['weight'] = 'normal'
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command = change_boldness)



#italic button functionality
def change_italic():
    global text_property
    text_property = font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        # text_property.actual()['slant'] = 'italic'
        # print(text_property)
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    elif text_property.actual()['slant'] == 'italic':
        # text_property.actual()['slant'] = 'roman'
        # print(text_property)
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command = change_italic)


#underline button functionality
def change_underline():
    global text_property
    text_property = font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 1:
        # text_property.actual()['slant'] = 'underline'
        # print(text_property)
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
    elif text_property.actual()['underline'] == 0:
        # text_property.actual()['slant'] = 'roman'
        # print(text_property)
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
underline_btn.configure(command = change_underline)

#change font_color
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    print(color_var)
    text_editor.configure(fg=color_var[1])

font_btn.configure(command=change_font_color)



#KEEPING DEFAULT FONT_FAMILY AND FONT_SIZE
text_editor.configure(font = ('Arial',16))


##alignment functionalities

def align_left():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,"end")
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=align_left)

def align_right():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,"end")
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command=align_right)

def align_center():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,"end")
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command=align_center)




# # ----------------- end text editor  -----------------

# # ----------------- main status bar -----------------
status_bar = ttk.Label(main_application,text = "Welcome to this software!!!")
status_bar.pack(side = tk.BOTTOM)

##status bar functionalities
text_change = False
def getWords(main_application):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        totalText = text_editor.get(1.0,"end-1c")
        words = len(totalText.split(" "))
        characters = len(totalText)-totalText.count(' ')
        status_bar.config(text=f'Total words: {words} and total characters: {characters}')
    text_editor.edit_modified(0)
text_editor.bind('<<Modified>>',getWords)


# # ----------------- end status bar  -----------------

# # ----------------- main main menu functionality -----------------

#file commands
url = ""
def getNewFile(x = None):
    global url
    url = ""
    text_editor.delete(1.0,tk.END)
file.add_command(image=new_icon,label = "  new",compound=tk.LEFT,accelerator = "Ctrl+N",command = getNewFile)

def openFile(x = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Choose file to open it...",filetypes = (('All files','*.*'),('Text File','*.txt')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    except:
        return 
    main_application.title(os.path.basename(url))
        
        
        
file.add_command(image=open_icon,label = "  open",compound=tk.LEFT,accelerator = "Ctrl+O",command = openFile)

def saveFile(x = None):
    global url
    try:
        content = str(text_editor.get(1.0,tk.END))
        if url:
            with open(url,'w') as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('All files','*.*'),('Text File','*.txt')))
            url = url.name
            with open(url,'w') as af:
                af.write(content)
    except:
        return

def saveAsFile(x = None):
    global url
    try:
        content = str(text_editor.get(1.0,tk.END))
        url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('All files','*.*'),('Text File','*.txt')))
        url = url.name
        with open(url,'w') as saf:
            saf.write(content)
    except:
        return 
        
        
file.add_command(image=save_icon,label = "  save",compound=tk.LEFT,accelerator = "Ctrl+S",command = saveFile)
file.add_command(image=save_as_icon,label = "  saveAs",compound=tk.LEFT,accelerator = "Ctrl+Alt+S",command = saveAsFile)


def exitFile(x = None):
    global url, text_change
    
    try:
        content = str(text_editor.get(1.0,tk.END))
        if text_change:
            mbox = messagebox.askyesnocancel(title = "Warning!!!",message = "Do u want to save the file?")
            if mbox == True:
                if url:
                    with open(url,'w') as wf:
                        wf.write(content)
                    text_change = False
                    main_application.destroy()
                else:
                    # print('bye')
                    url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('All files','*.*'),('Text File','*.txt')))
                    # print(url.name)
                    url = url.name
                    with open(url,'w') as saf:
                        saf.write(content)
                    text_change = False
                    main_application.destroy()
            elif mbox == False:
                text_change = False
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 

file.add_command(image=exit_icon,label = "  exit",compound=tk.LEFT,accelerator = "Ctrl+Q",command = exitFile)

##find functionality

def find_func(x = None):
    findDialog = tk.Toplevel()
    findDialog.geometry('450x250+500+500')
    findDialog.title('Find')
    findDialog.resizable(width=0,height=0)
    
    def find():
        word = findEntryBox.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(pattern=word,index=start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                start_pos=end_pos
                matches+=1
                text_editor.tag_config('match',background="yellow",foreground="red")
        
            
    def replace():
        replace_text = replaceEntryBox.get()
        word = findEntryBox.get()
        if word and replace_text:
            old_content = text_editor.get(1.0,tk.END)
            new_content = old_content.replace(word,replace_text)
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,new_content)
    ##frame
    find_frame = ttk.LabelFrame(findDialog,text='Find/Replace')
    find_frame.pack(pady=25)
    
    ##creating labels on frame
    
    textFindLabel = ttk.Label(find_frame,text = "Find : ")
    textReplaceLabel = ttk.Label(find_frame,text = "Replace : ")
    
    
    #creating entry boxes
    findEntryBox = ttk.Entry(find_frame,width=30)
    replaceEntryBox = ttk.Entry(find_frame,width = 30)
    
    ##button(find and replace)
    find_btn = ttk.Button(find_frame,text = "Find",command = find)
    replace_btn = ttk.Button(find_frame,text = 'Replace',command=replace)
    
    ##designing
    textFindLabel.grid(row=0,column=0,padx=4,pady=4)
    findEntryBox.grid(row=0,column=1,padx=6,pady=4)
    textReplaceLabel.grid(row=1,column=0,padx=4,pady=4)
    replaceEntryBox.grid(row=1,column=1,padx=6,pady=4)
    find_btn.grid(row = 2,column = 1,padx=0,pady=8)
    replace_btn.grid(row = 3,column = 1,padx=0,pady=8)
    
    findDialog.mainloop()
    # print(f'x is {x}')
    
#edit commands
edit.add_command(image = copy_icon, label = '  copy', compound = tk.LEFT, accelerator = 'Ctrl+C   ',command = lambda :text_editor.event_generate('<Control c>'))
edit.add_command(image = cut_icon, label = '  cut', compound = tk.LEFT, accelerator = 'Ctrl+X     ',command = lambda :text_editor.event_generate('<Control x>'))
edit.add_command(image = paste_icon, label = '  paste', compound = tk.LEFT, accelerator = 'Ctrl+V     ',command = lambda :text_editor.event_generate('<Control v>'))
edit.add_command(image = find_icon, label = '  find', compound = tk.LEFT, accelerator = 'Ctrl+F     ',command = find_func)
edit.add_command(image = clear_all_icon, label = '  clear All', compound = tk.LEFT, accelerator = 'Ctrl+Alt+X   ',command = lambda :text_editor.delete(1.0,tk.END))


#toolbar commands

hide_tool = tk.BooleanVar()
hide_status = tk.BooleanVar()
hide_tool.set(True)
hide_status.set(True)


def hide_toolbar():
    global hide_tool
    global hide_status
    if hide_tool:
        tool_bar.pack_forget()
        hide_tool = False
    else:
        text_editor.pack_forget()
        if hide_status:
            status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH,expand = True)
        if hide_status:
            status_bar.pack(side = tk.BOTTOM)
        hide_tool = True
def hide_statusbar():
    global hide_status
    global hide_tool
    if hide_status:
        status_bar.pack_forget()
        hide_status = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        hide_status = True

view.add_checkbutton(onvalue= 1,offvalue = 0,image = toolbar_icon,label = "  Toolbar",compound = tk.LEFT,variable = hide_tool,accelerator = "Ctrl+T     ",command = hide_toolbar)
view.add_checkbutton(onvalue=1,offvalue=0,image = statusbar_icon,label = "  Statusbar",compound = tk.LEFT,variable = hide_status,accelerator = "Ctrl+Alt+B     ",command = hide_statusbar)


#colortheme commands

def changeTheme():
    global color_choice
    choosen_theme = color_choice.get()
    # print(colortheme)
    colorTuple = color_dict[choosen_theme]
    text_editor.config(foreground=colorTuple[1],background=colorTuple[0])

for i in color_dict:
    colortheme.add_radiobutton(image = color_dict[i][2],label = i,compound = tk.LEFT,command = changeTheme,variable=color_choice)



# # ----------------- end main menu functionality  -----------------

main_application.config(menu=main_menu)
main_application.title("Welcome to Gpad text-editor")

##binding shortcut keys
main_application.bind('<Control-n>',getNewFile)
main_application.bind('<Control-o>',openFile)
main_application.bind('<Control-s>',saveFile)
main_application.bind('<Control-Alt-s>',saveAsFile)
main_application.bind('<Control-q>',exitFile)
main_application.bind('<Control-f>',find_func)
main_application.mainloop()