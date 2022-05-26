import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkVideoPlayer import TkinterVideo


USERNAME="admin"
PASSWORD="admin"
# You can also use a pandas dataframe for employees.
# you can convert the dataframe using df.to_numpy.tolist()
employees = [['Hamid', "Rahimi", '1998'], ['Karim', "Sabri", '405'], ['Abdelrahman', "Mrabet", '525'], ['Salim', "Ghamel", '309']]
status1 = [['Hamid', "Rahimi", '1998', '13:40'], ['Karim', "Sabri", '405', '13:40'], ['Abdelrahman', "Mrabet", '525', '13:40'], ['Salim', "Ghamel", '309', '13:40']]
status2 = [['Hamid', "Rahimi", '1998', '13:40'], ['Karim', "Sabri", '405', '13:40'], ['Abdelrahman', "Mrabet", '525', '13:40'], ['Salim', "Ghamel", '309', '13:40']]

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.50)



        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            # if your want to run the script as it is set validation = True
            validation = validate(username, password)
            if validation:
                tk.messagebox.showinfo("Login Successful",
                                       "Welcome {}".format(username))
                root.deiconify()
                top.destroy()
            else:
                tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")

        def validate(username, password):
            if USERNAME == username and PASSWORD == password:
                return True
            return False



class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Plate Detector", menu=menu_file)
        menu_file.add_command(label="Home", command=lambda: parent.show_frame(Some_Widgets))
        menu_file.add_command(label="List of employees", command=lambda: parent.show_frame(PageOne))
        menu_file.add_separator()
        menu_file.add_command(label="Quit", command=lambda: parent.Quit_application())
        

"""         menu_orders = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu2", menu=menu_orders)

        menu_pricing = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu3", menu=menu_pricing)
        menu_pricing.add_command(label="Page One", command=lambda: parent.show_frame(PageOne))

        menu_operations = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu4", menu=menu_operations)
        menu_operations.add_command(label="Page Two", command=lambda: parent.show_frame(PageTwo))
        menu_positions = tk.Menu(menu_operations, tearoff=0)
        menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
        menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu6", menu=menu_help)
        menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())
 """

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        # self.geometry("1024x600") fixes the applications size
        self.frames = {}
        pages = (Some_Widgets, PageOne, PageThree, PageFour)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Some_Widgets)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)


class Some_Widgets(GUI):  # inherits from the GUI class
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.LabelFrame(self, frame_styles, text="Cam 1 (IN)")
        frame1.place(rely=0.05, relx=0.02, relheight=0.4, relwidth=0.6)


        frame2 = tk.LabelFrame(self, frame_styles, text="Cam 2 (OUT)")
        frame2.place(rely=0.5, relx=0.02, relheight=0.4, relwidth=0.6)

        

        frame3 = tk.LabelFrame(self, frame_styles, text="Cam 1 Status")
        frame3.place(rely=0.05, relx=0.65, relheight=0.4, relwidth=0.3)

        frame4 = tk.LabelFrame(self, frame_styles, text="Cam 2 Status")
        frame4.place(rely=0.5, relx=0.65, relheight=0.4, relwidth=0.3)

        # This is a treeview.
        tv1 = ttk.Treeview(frame3)
        column_list_account = ["Name", "Last Name", "Plate Number", "Time"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame3)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data1():
            for row in status1:
                tv1.insert("", "end", values=row)

        Load_data1()

        # This is a treeview.
        tv1 = ttk.Treeview(frame4)
        column_list_account = ["Name", "Last Name", "Plate Number", "Time"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame4)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data2():
            for row in status2:
                tv1.insert("", "end", values=row)

        def Refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            Load_data2()

        Load_data2()




class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        frame1 = tk.LabelFrame(self, frame_styles, text="Registered Employees")
        frame1.place(rely=0.05, relx=0.02, height=400, width=400)


        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["Name", "Last Name", "Plate Number"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data():
            for row in employees:
                tv1.insert("", "end", values=row)

        def Refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            Load_data()

        Load_data()

class PageThree(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Three")
        label1.pack(side="top")


class PageFour(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Four")
        label1.pack(side="top")




top = LoginPage()
top.title("Plate Detector - Login Page")
root = MyApp()


root.withdraw()
root.title("Plate Detector")

root.mainloop()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"video.mp4")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

