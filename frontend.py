from tkinter import * 
from backend import Databse

databse = Databse()
selected_tuple = None

def get_selected_row(event):
    try:
        global selected_tuple
        index=list_view.curselection()[0]
        selected_tuple=list_view.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END,selected_tuple[1])
        author_entry.delete(0,END)
        author_entry.insert(END,selected_tuple[2])
        year_entry.delete(0,END)
        year_entry.insert(END,selected_tuple[3])
        isbn_entry.delete(0,END)
        isbn_entry.insert(END,selected_tuple[4])
    except IndexError:
        pass
    
# view function
def view_command():
    list_view.delete(0, END)
    for row in databse.view():
        list_view.insert(END, row)

# search function
def search_command():
    list_view.delete(0,END)
    for row in databse.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_view.insert(END, row)

# insert function
def add_command():
    databse.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_view.delete(0, END)
    list_view.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# Delete function
def delete_command():
    databse.delete(selected_tuple[0])

# Update function
def update_command():
    databse.update(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])

# Set up a main application window
window = Tk()
window.wm_title('BookStore')

# Create labels
title_label = Label(window, text='Title')
title_label.grid(row=0, column=0)
author_label = Label(window, text='Author')
author_label.grid(row=0, column=2)
year_label = Label(window, text='Year')
year_label.grid(row=1, column=0)
isbn_label = Label(window, text='ISBN')
isbn_label.grid(row=1, column=2)

# Create entry fields
title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)
author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)
year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)
isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

# Create listbox
list_view = Listbox(window, height=6, width=35)
list_view.grid(row=2, column=0, rowspan=7, columnspan=2)
list_view.bind('<<ListboxSelect>>', get_selected_row)

# Create scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=7)
list_view.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_view.yview)

# Create buttons
view_button = Button(window, text='View', width=12, command=view_command)
view_button.grid(row=2, column=3)
search_button = Button(window, text='Search', width=12, command=search_command)
search_button.grid(row=3, column=3)
add_button = Button(window, text='Add', width=12, command=add_command)
add_button.grid(row=4, column=3)
update_button = Button(window, text='Update', width=12, command=update_command)
update_button.grid(row=5, column=3)
delete_button = Button(window, text='Delete', width=12, command=delete_command)
delete_button.grid(row=6, column=3)
close_button = Button(window, text='Close', width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
