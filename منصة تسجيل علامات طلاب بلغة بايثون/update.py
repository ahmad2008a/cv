from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import END
from tkinter import messagebox

class Program:
    #----------انشاء نافذة البرنامج---------
    def __init__(self, Window):
        self.Window = Window
        self.Window.geometry('1850x950+1+1')
        self.Window.title('تسجيل الدخول')
        self.Window.configure(background="#2471a3")
        self.Window.resizable(True, True)
        
        # عنوان النافذة
        title = Label(self.Window, 
                      text='BTEC', 
                      background="#2471a3", 
                      font=("monospace", 90), 
                      fg="white")
        title.pack(fill=X)
        
        # الإطار الذي يحتوي على الحقول
        Frame_design = Frame(self.Window, bg="silver")
        Frame_design.place(x=730, y=300, width=400, height=500)
        
        # حقل اسم المستخدم
        Label_1 = Label(Frame_design, text="اسم المستخدم", font=("bold", 25), fg="black", bg="silver")
        Label_1.pack(pady=10)
        self.name = Entry(Frame_design, bd=2, justify=CENTER, width=30)
        self.name.pack(pady=10)
        
        # حقل كلمة المرور
        Label_2 = Label(Frame_design, text="كلمة المرور", font=("bold", 25), fg="black", bg="silver")
        Label_2.pack(pady=10)
        self.password = Entry(Frame_design, bd=2, justify=CENTER, width=30, show='*')  # استخدام '*' لإخفاء كلمة المرور
        self.password.pack(pady=10)
        
        # زر إظهار/إخفاء كلمة المرور
        btn_show = Button(Frame_design, text="👀", bg="silver", font=("bold", 20), command=self.show)
        btn_show.place(x=107, y=180, width=30, height=20)
        
        # زر تسجيل الدخول
        add_btn = Button(Frame_design, text="تسجيل الدخول", bg="orange", font=("bold", 25), command=self.check_login)
        add_btn.place(x=60, y=250, width=300, height=35)

    # دالة التحقق من اسم المستخدم وكلمة المرور
    def check_login(self):
        username = self.name.get()
        password = self.password.get()

        # التحقق من المدخلات
        if username == "ahmad" and password == "ahmad2008":
            messagebox.showerror("مرحبا", "مرحبا بمعلم اللغة العربية!")
            self.open_1_window()
            self.Window.destroy(Program) # إغلاق النافذة الأولى
        elif username == "m" and password == "m":
            messagebox.showerror("مرحبا", "مرحبا بمعلم اللغة الانجليزية!")
            self.open_2_window()  # فتح النافذة الثانية
            self.Window.destroy(Program)  # إغلاق النافذة الأولى
        elif username == "b" and password == "b":
            messagebox.showerror("مرحبا", "مرحبا بمعلم التربية الاسلامية!")
            self.open_3_window()  # فتح النافذة الثانية
            self.Window.destroy(Program)  # إغلاق النافذة الأولى
        elif username == "c" and password == "c":
            messagebox.showerror("مرحبا", "مرحبا بمعلم الحاسوب!")
            self.open_4_window()  # فتح النافذة الثانية
            self.Window.destroy(Program)  # إغلاق النافذة الأولى
            
        elif username == "d" and password == "d":
            messagebox.showerror("مرحبا", "مرحبا بمعلم تاريخ الأردن!")
            self.open_5_window()  # فتح النافذة الثانية
            self.Window.destroy(Program)  # إغلاق النافذة الأولى


        else:
            messagebox.showerror("خطأ", "اسم المستخدم أو كلمة المرور غير صحيحة!")
        
    
    # دالة إظهار/إخفاء كلمة المرور
    def show(self):
        if self.password.cget('show') == '*': 
            self.password.config(show='')  # إظهار كلمة المرور
        else:
            self.password.config(show='*')  # إخفاء كلمة المرور
    
    # دالة فتح النافذة الاولى
    def open_1_window(self):
        self.new_window = Toplevel(self.Window)
        Student(self.new_window)

    #دالة فتح النافدة الثانية
    def open_2_window(self):
        self.new_window = Toplevel(self.Window)
        English(self.new_window)
    #دالة فتح النافذة الثالثة
        # دالة فتح النافذة الثانية
    def open_3_window(self):
        self.new_window = Toplevel(self.Window)
        Islamic(self.new_window)
        
    def open_4_window(self):
        self.new_window = Toplevel(self.Window)
        Computer(self.new_window)
        
    def open_5_window(self):
        self.new_window = Toplevel(self.Window)
        History(self.new_window)



# الصف الخاص بنافذة الطالب (النافذة الثانية)
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1850x950+1+1')
        self.root.title(' برنامج مدرسة القويسمة الثانوية للبنين')
        self.root.configure(background="#2980b9")
        self.root.resizable(False, False)
        title = Label(self.root,
                      text='......{تسجيل علامات الطلاب}.....',
                      background="#1f90bb",
                      font=("monospace", 25),
                      fg="white")
        title.pack(fill=X)
    
   #----------------------(variable)المتغيرات---------------
        self.name_var=StringVar()
        self.num_var=StringVar()
        self.material_var=StringVar()
        self.season_var=StringVar()
        self.month1_var=StringVar()
        self.month2_var=StringVar()
        self.month3_var=StringVar()
        self.month4_var=StringVar()
        self.delete_var=StringVar()
        self.search_var = StringVar()
        self.search_by = StringVar()       
#---------------ادوات التحكم في البرنامج-------------
        m = Frame(self.root,bg="#2980b9")
        m.place (x=1350,y=45,width=500,height=550)
        lab_titel =Label(m,text=' إضافة علامات الطلاب ',bg="#2980b9",
        font=("bold",23),
        fg=("black")
        )
        lab_titel.pack()
        lab_id = Label(m,text=' الرقم الوطني لطالب',bg="#d7dbdd",font=("deco",14))
        lab_id.pack()
        id= Entry(m,textvariable=self.num_var,bd='2',justify=CENTER)
        id.pack()
        lab_name = Label(m,text='اسم الطالب',bg="#d7dbdd",font=("deco",14))
        lab_name.pack()
        name= Entry(m,textvariable=self.name_var,bd='2',justify=CENTER)
        name.pack()
        lab_material= Label(m,text='المادة',bg="#d7dbdd",font=("deco",14))
        lab_material.pack()
        compo_material=ttk.Combobox(m,textvariable=self.material_var)
        compo_material = Label(m,text='اللغة العربية',bg="#ecf0f1",fg="black",font=("deco",14))
        compo_material.pack()
        self.material_var.set("اللغة العربية")
        lab_season= Label(m,text='الفصل',bg="#d7dbdd",font=("deco",14))
        lab_season.pack()
        compo_season=ttk.Combobox(m,textvariable=self.season_var)
        compo_season["value"]=("الفصل الثاني","الفصل الاول")
        compo_season.pack()
        lab_bass = Label(m,text='الشهر الاول',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month1= Entry(m,textvariable=self.month1_var,bd='2',justify=CENTER)
        month1.pack()
        lab_bass = Label(m,text='الشهر الثاني',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month2= Entry(m,textvariable=self.month2_var,bd='2',justify=CENTER)
        month2.pack()
        lab_bass = Label(m,text='الشهر الثالث',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month3= Entry(m,textvariable=self.month3_var,bd='2',justify=CENTER)
        month3.pack()
        lab_bass = Label(m,text='نهائي',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month4= Entry(m,textvariable=self.month4_var,bd='2',justify=CENTER)
        month4.pack()
        lab_delete = Label(m,text='حذف الطالب عن طريق الأسم',bg="#d7dbdd",
        font=("monospace",15),
        fg=("red"))
        lab_delete.pack()
        delete= Entry(m,bd='2',justify=CENTER,textvariable=self.delete_var)
        delete.pack()
        #--------------ادوات التحكم (الازرار)------------
        btn_frame=Frame(self.root ,bg=("#2980b9"))
        btn_frame.place(x=1350 , y=550 , width=510 , height=500)
        title1=Label(btn_frame,text="لوحة التحكم",bg="#2980b9",font=("bold",25),fg=("black"))
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text="إضافة",bg="#26dc15", font=("deco",20),command=self.add_student)
        add_btn.place(x=120 , y=60 , width=300 ,height=35 )
        delete_btn=Button(btn_frame,text="حذف الطالب عن طريق الاسم",bg="#dc2b15",font=("deco",20),command = self.delete)
        delete_btn.place(x=120 , y=120 , width=300 ,height=35 )
        update_btn=Button(btn_frame,text="تحديث البيانات الطالب",bg="#1559dc",font=("deco",20),command = self.update)
        update_btn.place(x=120 , y=180 , width=300 ,height=35 )
        cler_btn=Button(btn_frame,text="إفراغ الخانات",bg="#a19d9b",font=("deco",20),command = self.clear )
        cler_btn.place(x=120 , y=240 , width=300 ,height=35 )
        exit_btn=Button(btn_frame,text="خروج",bg="black",fg="white",font=("deco",20),command = root.quit)
        exit_btn.place(x=120 , y=300 , width=300 ,height=35 )
        #--------------------------البحث----------------------
        search_frame=Frame(self.root ,bg=("#2980b9"))
        search_frame.place(x=1 , y=45, width=1350 , height=100)
        lab_search=Label(search_frame,text=("البحث عن طالب عن طريق الرقم الوطني "),bg="white",font=("deco",18))
        lab_search.place(x=1000,y=20)
        compo_search=ttk.Combobox(search_frame,justify="right")
        search_Entry=Entry(search_frame , textvariable=self.search_var ,justify=CENTER , bd=2)
        search_Entry.place(x=850 ,y=30)
        search_btn=Button(search_frame,text="بحث",bg="#d8dddc",fg="black",font=("deco",20),command = self.search)
        search_btn.place(x=780 , y=26 , width=50 ,height=30 )
        #----------------عرض النتائج والبيانات---------------
        data_frame=Frame(self.root,bg="#f2f7f6")
        data_frame.place(x=1 , y=140, width=1345 , height=800)
        #-----------------القائمة-----------------------------
        scroll_x=Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(data_frame,orient=VERTICAL)
        #---------------------- الترتيب البيانات------------------------
        self.student_table=ttk.Treeview(data_frame,
         columns=("الرقم الوطني","اسم الطالب","المادة","الفصل","الشهر الاول","الشهر الثاني","الشهر الثالث","نهائي"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set )
        self.student_table.place(x=18 , y=1 ,width=1345 , height=780)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #---------------لإظهار السكرول---------------
        scroll_x.config(command=self.student_table.xview )
        scroll_y.config(command=self.student_table.yview )
        self.student_table["show"]="headings"
        self.student_table.heading("اسم الطالب",text="اسم الطالب")
        self.student_table.heading("الرقم الوطني",text="الرقم الوطني")
        self.student_table.heading("المادة",text="المادة")
        self.student_table.heading("الفصل",text="الفصل")
        self.student_table.heading("الشهر الاول",text="الشهر الاول")
        self.student_table.heading("الشهر الثاني",text="الشهر الثاني")
        self.student_table.heading("الشهر الثالث",text="الشهر الثالث")
        self.student_table.heading("نهائي",text="نهائي")
        self.student_table.column("الرقم الوطني",width=200)
        self.student_table.column("اسم الطالب",width=200)
        self.student_table.column("المادة",width=200)
        self.student_table.column("الفصل",width=200)
        self.student_table.column("الشهر الاول",width=200)
        self.student_table.column("الشهر الثاني",width=200)
        self.student_table.column("الشهر الثالث",width=200)
        self.student_table.column("نهائي",width=200)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #----------------إضافة البيانات إلى قاعدة البيانات------------
        self.fetch_all()
    def add_student(self):
            con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
            cur=con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.num_var.get(),
                                                                  self.name_var.get(),
                                                                  self.material_var.get(),
                                                                  self.season_var.get(),
                                                                  self.month1_var.get(),
                                                                  self.month2_var.get(),
                                                                  self.month3_var.get(),
                                                                  self.month4_var.get()
                                                                  
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
#------------------------ اضافة البييانات الى الجدول py (tk)بايثون تكنتر--------------------------
    def fetch_all(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("select * from student")
        row=cur.fetchall()
        if len (row)!=0:
            self.student_table.delete(* self .student_table.get_children())
            for ro in row:
                self.student_table.insert("",END,values=ro)
            con.commit()
        con.close()
#----------------حذف عن طريق الاسم-----------------
    def delete (self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud")
        cur=con.cursor()
        cur.execute('delete from student where name=%s', self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()
#-----------------------افراغ الخانات----------------------------
    def clear(self):
        self.num_var.set("")
        self.name_var.set("")
        self.material_var.set("")
        self.season_var.set("")
        self.month1_var.set("")
        self.month2_var.set("")
        self.month3_var.set("")
        self.month4_var.set("")
#------------------------تحديث بيانات الطالب------------------------
    def get_cursor(self,cu):
        cursor_ro = self.student_table.focus()
        co = self.student_table.item(cursor_ro)
        row =co["values"]
        self.num_var.set(row[0])
        self.name_var.set(row[1])
        self.material_var.set(row[2])
        self.season_var.set(row[3])
        self.month1_var.set(row[4])
        self.month2_var.set(row[5])
        self.month3_var.set(row[6])
        self.month4_var.set(row[7])
#----------------لتشغل زر تحديث البيانات---------------------------------
    def update(self) :
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("UPDATE student SET name=%s, material=%s, season=%s, month1=%s, month2=%s, month3=%s, month4=%s WHERE num=%s", (
    self.name_var.get(),
    self.material_var.get(),
    self.season_var.get(),
    self.month1_var.get(),
    self.month2_var.get(),
    self.month3_var.get(),
    self.month4_var.get(),
    self.num_var.get()
))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
#--------------------------البحث-----------------------------
    def search(self):
        con = pymysql.connect(host="localhost", user="root", passwd="", database="stud")
        cur = con.cursor()
        search_column = "name" if self.search_by.get() == "عن طريق الاسم" else "num"
        query = f"SELECT * FROM student WHERE {search_column} LIKE %s"
        search_value = "%" + str(self.search_var.get()) + "%"
        cur.execute(query, (search_value,))
        row = cur.fetchall()
        if len(row) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for ro in row:
                self.student_table.insert("", END, values=ro)
        con.commit()
        con.close()
        

class English:
    
    #----------انشاء نافدة البرنامج---------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1850x950+1+1')
        self.root.title(' برنامج مدرسة القويسمة الثانوية للبنين')
        self.root.configure(background="#2980b9")
        self.root.resizable(False,FALSE)
        title = Label(self.root ,
        text ='......{تسجيل علامات  الطلاب}.....',
        background= "black",
        font=("monospace",25),
        fg="white"
        )
        title.pack(fill=X)
        title.pack()
        #----------------------(variable)المتغيرات---------------
        self.name_var=StringVar()
        self.num_var=StringVar()
        self.material_var=StringVar()
        self.season_var=StringVar()
        self.month1_var=StringVar()
        self.month2_var=StringVar()
        self.month3_var=StringVar()
        self.month4_var=StringVar()
        self.delete_var=StringVar()
        self.search_var = StringVar()
        self.search_by = StringVar()       
#---------------ادوات التحكم في البرنامج-------------
        m = Frame(self.root,bg="#2980b9")
        m.place (x=1350,y=45,width=500,height=550)
        lab_titel =Label(m,text=' إضافة علامات الطلاب ',bg="#2980b9",
        font=("bold",23),
        fg=("black")
        )
        lab_titel.pack()
        lab_id = Label(m,text=' الرقم الوطني لطالب',bg="#d7dbdd",font=("deco",14))
        lab_id.pack()
        id= Entry(m,textvariable=self.num_var,bd='2',justify=CENTER)
        id.pack()
        lab_name = Label(m,text='اسم الطالب',bg="#d7dbdd",font=("deco",14))
        lab_name.pack()
        name= Entry(m,textvariable=self.name_var,bd='2',justify=CENTER)
        name.pack()
        lab_material= Label(m,text='المادة',bg="#d7dbdd",font=("deco",14))
        lab_material.pack()
        compo_material=ttk.Combobox(m,textvariable=self.material_var)
        compo_material = Label(m,text='اللغة الانجليزية',bg="#ecf0f1",fg="black",font=("deco",14))
        compo_material.pack()
        self.material_var.set("اللغة الانجليزية")
        lab_season= Label(m,text='الفصل',bg="#d7dbdd",font=("deco",14))
        lab_season.pack()
        compo_season=ttk.Combobox(m,textvariable=self.season_var)
        compo_season["value"]=("الفصل الثاني","الفصل الاول")
        compo_season.pack()
        lab_bass = Label(m,text='الشهر الاول',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month1= Entry(m,textvariable=self.month1_var,bd='2',justify=CENTER)
        month1.pack()
        lab_bass = Label(m,text='الشهر الثاني',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month2= Entry(m,textvariable=self.month2_var,bd='2',justify=CENTER)
        month2.pack()
        lab_bass = Label(m,text='الشهر الثالث',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month3= Entry(m,textvariable=self.month3_var,bd='2',justify=CENTER)
        month3.pack()
        lab_bass = Label(m,text='نهائي',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month4= Entry(m,textvariable=self.month4_var,bd='2',justify=CENTER)
        month4.pack()
        lab_delete = Label(m,text='حذف الطالب عن طريق الأسم',bg="#d7dbdd",
        font=("monospace",15),
        fg=("red"))
        lab_delete.pack()
        delete= Entry(m,bd='2',justify=CENTER,textvariable=self.delete_var)
        delete.pack()
        #--------------ادوات التحكم (الازرار)------------
        btn_frame=Frame(self.root ,bg=("#2980b9"))
        btn_frame.place(x=1350 , y=550 , width=510 , height=500)
        title1=Label(btn_frame,text="لوحة التحكم",bg="#2980b9",font=("bold",25),fg=("black"))
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text="إضافة",bg="#26dc15", font=("deco",20),command=self.add_student)
        add_btn.place(x=120 , y=60 , width=300 ,height=35 )
        delete_btn=Button(btn_frame,text="حذف الطالب عن طريق الاسم",bg="#dc2b15",font=("deco",20),command = self.delete)
        delete_btn.place(x=120 , y=120 , width=300 ,height=35 )
        update_btn=Button(btn_frame,text="تحديث البيانات الطالب",bg="#1559dc",font=("deco",20),command = self.update)
        update_btn.place(x=120 , y=180 , width=300 ,height=35 )
        cler_btn=Button(btn_frame,text="إفراغ الخانات",bg="#a19d9b",font=("deco",20),command = self.clear )
        cler_btn.place(x=120 , y=240 , width=300 ,height=35 )
        exit_btn=Button(btn_frame,text="خروج",bg="black",fg="white",font=("deco",20),command = root.quit)
        exit_btn.place(x=120 , y=300 , width=300 ,height=35 )
        #--------------------------البحث----------------------
        search_frame=Frame(self.root ,bg=("#2980b9"))
        search_frame.place(x=1 , y=45, width=1350 , height=100)
        lab_search=Label(search_frame,text=("البحث عن طالب عن طريق الرقم الوطني "),bg="white",font=("deco",18))
        lab_search.place(x=1000,y=20)
        compo_search=ttk.Combobox(search_frame,justify="right")
        search_Entry=Entry(search_frame , textvariable=self.search_var ,justify=CENTER , bd=2)
        search_Entry.place(x=850 ,y=30)
        search_btn=Button(search_frame,text="بحث",bg="#d8dddc",fg="black",font=("deco",20),command = self.search)
        search_btn.place(x=780 , y=26 , width=50 ,height=30 )
        #----------------عرض النتائج والبيانات---------------
        data_frame=Frame(self.root,bg="#f2f7f6")
        data_frame.place(x=1 , y=140, width=1345 , height=800)
        #-----------------القائمة-----------------------------
        scroll_x=Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(data_frame,orient=VERTICAL)
        #---------------------- الترتيب البيانات------------------------
        self.student_table=ttk.Treeview(data_frame,
         columns=("الرقم الوطني","اسم الطالب","المادة","الفصل","الشهر الاول","الشهر الثاني","الشهر الثالث","نهائي"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set )
        self.student_table.place(x=18 , y=1 ,width=1345 , height=780)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #---------------لإظهار السكرول---------------
        scroll_x.config(command=self.student_table.xview )
        scroll_y.config(command=self.student_table.yview )
        self.student_table["show"]="headings"
        self.student_table.heading("اسم الطالب",text="اسم الطالب")
        self.student_table.heading("الرقم الوطني",text="الرقم الوطني")
        self.student_table.heading("المادة",text="المادة")
        self.student_table.heading("الفصل",text="الفصل")
        self.student_table.heading("الشهر الاول",text="الشهر الاول")
        self.student_table.heading("الشهر الثاني",text="الشهر الثاني")
        self.student_table.heading("الشهر الثالث",text="الشهر الثالث")
        self.student_table.heading("نهائي",text="نهائي")
        self.student_table.column("الرقم الوطني",width=200)
        self.student_table.column("اسم الطالب",width=200)
        self.student_table.column("المادة",width=200)
        self.student_table.column("الفصل",width=200)
        self.student_table.column("الشهر الاول",width=200)
        self.student_table.column("الشهر الثاني",width=200)
        self.student_table.column("الشهر الثالث",width=200)
        self.student_table.column("نهائي",width=200)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #----------------إضافة البيانات إلى قاعدة البيانات------------
        self.fetch_all()
    def add_student(self):
            con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
            cur=con.cursor()
            cur.execute("insert into english values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.num_var.get(),
                                                                  self.name_var.get(),
                                                                  self.material_var.get(),
                                                                  self.season_var.get(),
                                                                  self.month1_var.get(),
                                                                  self.month2_var.get(),
                                                                  self.month3_var.get(),
                                                                  self.month4_var.get()
                                                                  
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
#------------------------ اضافة البييانات الى الجدول py (tk)بايثون تكنتر--------------------------
    def fetch_all(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("select * from english")
        row=cur.fetchall()
        if len (row)!=0:
            self.student_table.delete(* self .student_table.get_children())
            for ro in row:
                self.student_table.insert("",END,values=ro)
            con.commit()
        con.close()
#----------------حذف عن طريق الاسم-----------------
    def delete (self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud")
        cur=con.cursor()
        cur.execute('delete from english where name=%s', self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()
#-----------------------افراغ الخانات----------------------------
    def clear(self):
        self.num_var.set("")
        self.name_var.set("")
        self.material_var.set("")
        self.season_var.set("")
        self.month1_var.set("")
        self.month2_var.set("")
        self.month3_var.set("")
        self.month4_var.set("")
#------------------------تحديث بيانات الطالب------------------------
    def get_cursor(self,cu):
        cursor_ro = self.student_table.focus()
        co = self.student_table.item(cursor_ro)
        row =co["values"]
        self.num_var.set(row[0])
        self.name_var.set(row[1])
        self.material_var.set(row[2])
        self.season_var.set(row[3])
        self.month1_var.set(row[4])
        self.month2_var.set(row[5])
        self.month3_var.set(row[6])
        self.month4_var.set(row[7])
#----------------لتشغل زر تحديث البيانات---------------------------------
    def update(self) :
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("UPDATE english SET name=%s, material=%s, season=%s, month1=%s, month2=%s, month3=%s, month4=%s WHERE num=%s", (
    self.name_var.get(),
    self.material_var.get(),
    self.season_var.get(),
    self.month1_var.get(),
    self.month2_var.get(),
    self.month3_var.get(),
    self.month4_var.get(),
    self.num_var.get()
))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
#--------------------------البحث-----------------------------
    def search(self):
        con = pymysql.connect(host="localhost", user="root", passwd="", database="stud")
        cur = con.cursor()
        search_column = "name" if self.search_by.get() == "عن طريق الاسم" else "num"
        query = f"SELECT * FROM english WHERE {search_column} LIKE %s"
        search_value = "%" + str(self.search_var.get()) + "%"
        cur.execute(query, (search_value,))
        row = cur.fetchall()
        if len(row) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for ro in row:
                self.student_table.insert("", END, values=ro)
        con.commit()
        con.close()

#--------------نافدة التربية الاسلامية--------------
class Islamic:
    
    #----------انشاء نافدة البرنامج---------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1850x950+1+1')
        self.root.title(' برنامج مدرسة القويسمة الثانوية للبنين')
        self.root.configure(background="#2980b9")
        self.root.resizable(False,FALSE)
        title = Label(self.root ,
        text ='......{تسجيل علامات  الطلاب}.....',
        background= "red",
        font=("monospace",25),
        fg="white"
        )
        title.pack(fill=X)
        title.pack()
        #----------------------(variable)المتغيرات---------------
        self.name_var=StringVar()
        self.num_var=StringVar()
        self.material_var=StringVar()
        self.season_var=StringVar()
        self.month1_var=StringVar()
        self.month2_var=StringVar()
        self.month3_var=StringVar()
        self.month4_var=StringVar()
        self.delete_var=StringVar()
        self.search_var = StringVar()
        self.search_by = StringVar()       
#---------------ادوات التحكم في البرنامج-------------
        m = Frame(self.root,bg="#2980b9")
        m.place (x=1350,y=45,width=500,height=550)
        lab_titel =Label(m,text=' إضافة علامات الطلاب ',bg="#2980b9",
        font=("bold",23),
        fg=("black")
        )
        lab_titel.pack()
        lab_id = Label(m,text=' الرقم الوطني لطالب',bg="#d7dbdd",font=("deco",14))
        lab_id.pack()
        id= Entry(m,textvariable=self.num_var,bd='2',justify=CENTER)
        id.pack()
        lab_name = Label(m,text='اسم الطالب',bg="#d7dbdd",font=("deco",14))
        lab_name.pack()
        name= Entry(m,textvariable=self.name_var,bd='2',justify=CENTER)
        name.pack()
        lab_material= Label(m,text='المادة',bg="#d7dbdd",font=("deco",14))
        lab_material.pack()
        compo_material=ttk.Combobox(m,textvariable=self.material_var)
        compo_material = Label(m,text='التربية الاسلامية',bg="#ecf0f1",fg="black",font=("deco",14))
        compo_material.pack()
        self.material_var.set("التربية الاسلامية")
        lab_season= Label(m,text='الفصل',bg="#d7dbdd",font=("deco",14))
        lab_season.pack()
        compo_season=ttk.Combobox(m,textvariable=self.season_var)
        compo_season["value"]=("الفصل الثاني","الفصل الاول")
        compo_season.pack()
        lab_bass = Label(m,text='الشهر الاول',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month1= Entry(m,textvariable=self.month1_var,bd='2',justify=CENTER)
        month1.pack()
        lab_bass = Label(m,text='الشهر الثاني',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month2= Entry(m,textvariable=self.month2_var,bd='2',justify=CENTER)
        month2.pack()
        lab_bass = Label(m,text='الشهر الثالث',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month3= Entry(m,textvariable=self.month3_var,bd='2',justify=CENTER)
        month3.pack()
        lab_bass = Label(m,text='نهائي',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month4= Entry(m,textvariable=self.month4_var,bd='2',justify=CENTER)
        month4.pack()
        lab_delete = Label(m,text='حذف الطالب عن طريق الأسم',bg="#d7dbdd",
        font=("monospace",15),
        fg=("red"))
        lab_delete.pack()
        delete= Entry(m,bd='2',justify=CENTER,textvariable=self.delete_var)
        delete.pack()
        #--------------ادوات التحكم (الازرار)------------
        btn_frame=Frame(self.root ,bg=("#2980b9"))
        btn_frame.place(x=1350 , y=550 , width=510 , height=500)
        title1=Label(btn_frame,text="لوحة التحكم",bg="#2980b9",font=("bold",25),fg=("black"))
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text="إضافة",bg="#26dc15", font=("deco",20),command=self.add_student)
        add_btn.place(x=120 , y=60 , width=300 ,height=35 )
        delete_btn=Button(btn_frame,text="حذف الطالب عن طريق الاسم",bg="#dc2b15",font=("deco",20),command = self.delete)
        delete_btn.place(x=120 , y=120 , width=300 ,height=35 )
        update_btn=Button(btn_frame,text="تحديث البيانات الطالب",bg="#1559dc",font=("deco",20),command = self.update)
        update_btn.place(x=120 , y=180 , width=300 ,height=35 )
        cler_btn=Button(btn_frame,text="إفراغ الخانات",bg="#a19d9b",font=("deco",20),command = self.clear )
        cler_btn.place(x=120 , y=240 , width=300 ,height=35 )
        exit_btn=Button(btn_frame,text="خروج",bg="black",fg="white",font=("deco",20),command = root.quit)
        exit_btn.place(x=120 , y=300 , width=300 ,height=35 )
        #--------------------------البحث----------------------
        search_frame=Frame(self.root ,bg=("#2980b9"))
        search_frame.place(x=1 , y=45, width=1350 , height=100)
        lab_search=Label(search_frame,text=("البحث عن طالب عن طريق الرقم الوطني "),bg="white",font=("deco",18))
        lab_search.place(x=1000,y=20)
        compo_search=ttk.Combobox(search_frame,justify="right")
        search_Entry=Entry(search_frame , textvariable=self.search_var ,justify=CENTER , bd=2)
        search_Entry.place(x=850 ,y=30)
        search_btn=Button(search_frame,text="بحث",bg="#d8dddc",fg="black",font=("deco",20),command = self.search)
        search_btn.place(x=780 , y=26 , width=50 ,height=30 )
        #----------------عرض النتائج والبيانات---------------
        data_frame=Frame(self.root,bg="#f2f7f6")
        data_frame.place(x=1 , y=140, width=1345 , height=800)
        #-----------------القائمة-----------------------------
        scroll_x=Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(data_frame,orient=VERTICAL)
        #---------------------- الترتيب البيانات------------------------
        self.student_table=ttk.Treeview(data_frame,
         columns=("الرقم الوطني","اسم الطالب","المادة","الفصل","الشهر الاول","الشهر الثاني","الشهر الثالث","نهائي"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set )
        self.student_table.place(x=18 , y=1 ,width=1345 , height=780)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #---------------لإظهار السكرول---------------
        scroll_x.config(command=self.student_table.xview )
        scroll_y.config(command=self.student_table.yview )
        self.student_table["show"]="headings"
        self.student_table.heading("اسم الطالب",text="اسم الطالب")
        self.student_table.heading("الرقم الوطني",text="الرقم الوطني")
        self.student_table.heading("المادة",text="المادة")
        self.student_table.heading("الفصل",text="الفصل")
        self.student_table.heading("الشهر الاول",text="الشهر الاول")
        self.student_table.heading("الشهر الثاني",text="الشهر الثاني")
        self.student_table.heading("الشهر الثالث",text="الشهر الثالث")
        self.student_table.heading("نهائي",text="نهائي")
        self.student_table.column("الرقم الوطني",width=200)
        self.student_table.column("اسم الطالب",width=200)
        self.student_table.column("المادة",width=200)
        self.student_table.column("الفصل",width=200)
        self.student_table.column("الشهر الاول",width=200)
        self.student_table.column("الشهر الثاني",width=200)
        self.student_table.column("الشهر الثالث",width=200)
        self.student_table.column("نهائي",width=200)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #----------------إضافة البيانات إلى قاعدة البيانات------------
        self.fetch_all()
    def add_student(self):
            con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
            cur=con.cursor()
            cur.execute("insert into islamic values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.num_var.get(),
                                                                  self.name_var.get(),
                                                                  self.material_var.get(),
                                                                  self.season_var.get(),
                                                                  self.month1_var.get(),
                                                                  self.month2_var.get(),
                                                                  self.month3_var.get(),
                                                                  self.month4_var.get()
                                                                  
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
#------------------------ اضافة البييانات الى الجدول py (tk)بايثون تكنتر--------------------------
    def fetch_all(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("select * from islamic")
        row=cur.fetchall()
        if len (row)!=0:
            self.student_table.delete(* self .student_table.get_children())
            for ro in row:
                self.student_table.insert("",END,values=ro)
            con.commit()
        con.close()
#----------------حذف عن طريق الاسم-----------------
    def delete (self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud")
        cur=con.cursor()
        cur.execute('delete from islamic where name=%s', self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()
#-----------------------افراغ الخانات----------------------------
    def clear(self):
        self.num_var.set("")
        self.name_var.set("")
        self.material_var.set("")
        self.season_var.set("")
        self.month1_var.set("")
        self.month2_var.set("")
        self.month3_var.set("")
        self.month4_var.set("")
#------------------------تحديث بيانات الطالب------------------------
    def get_cursor(self,cu):
        cursor_ro = self.student_table.focus()
        co = self.student_table.item(cursor_ro)
        row =co["values"]
        self.num_var.set(row[0])
        self.name_var.set(row[1])
        self.material_var.set(row[2])
        self.season_var.set(row[3])
        self.month1_var.set(row[4])
        self.month2_var.set(row[5])
        self.month3_var.set(row[6])
        self.month4_var.set(row[7])
#----------------لتشغل زر تحديث البيانات---------------------------------
    def update(self) :
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("UPDATE islamic SET name=%s, material=%s, season=%s, month1=%s, month2=%s, month3=%s, month4=%s WHERE num=%s", (
    self.name_var.get(),
    self.material_var.get(),
    self.season_var.get(),
    self.month1_var.get(),
    self.month2_var.get(),
    self.month3_var.get(),
    self.month4_var.get(),
    self.num_var.get()
))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
#--------------------------البحث-----------------------------
    def search(self):
        con = pymysql.connect(host="localhost", user="root", passwd="", database="stud")
        cur = con.cursor()
        search_column = "name" if self.search_by.get() == "عن طريق الاسم" else "num"
        query = f"SELECT * FROM islamic WHERE {search_column} LIKE %s"
        search_value = "%" + str(self.search_var.get()) + "%"
        cur.execute(query, (search_value,))
        row = cur.fetchall()
        if len(row) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for ro in row:
                self.student_table.insert("", END, values=ro)
        con.commit()
        con.close()
        
#--------------نافدة الحاسوب--------------
class Computer:
    
    #----------انشاء نافدة البرنامج---------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1850x950+1+1')
        self.root.title(' برنامج مدرسة القويسمة الثانوية للبنين')
        self.root.configure(background="#2980b9")
        self.root.resizable(False,FALSE)
        title = Label(self.root ,
        text ='......{تسجيل علامات  الطلاب}.....',
        background= "blue",
        font=("monospace",25),
        fg="white"
        )
        title.pack(fill=X)
        title.pack()
        #----------------------(variable)المتغيرات---------------
        self.name_var=StringVar()
        self.num_var=StringVar()
        self.material_var=StringVar()
        self.season_var=StringVar()
        self.month1_var=StringVar()
        self.month2_var=StringVar()
        self.month3_var=StringVar()
        self.month4_var=StringVar()
        self.delete_var=StringVar()
        self.search_var = StringVar()
        self.search_by = StringVar()       
#---------------ادوات التحكم في البرنامج-------------
        m = Frame(self.root,bg="#2980b9")
        m.place (x=1350,y=45,width=500,height=550)
        lab_titel =Label(m,text=' إضافة علامات الطلاب ',bg="#2980b9",
        font=("bold",23),
        fg=("black")
        )
        lab_titel.pack()
        lab_id = Label(m,text=' الرقم الوطني لطالب',bg="#d7dbdd",font=("deco",14))
        lab_id.pack()
        id= Entry(m,textvariable=self.num_var,bd='2',justify=CENTER)
        id.pack()
        lab_name = Label(m,text='اسم الطالب',bg="#d7dbdd",font=("deco",14))
        lab_name.pack()
        name= Entry(m,textvariable=self.name_var,bd='2',justify=CENTER)
        name.pack()
        lab_material= Label(m,text='المادة',bg="#d7dbdd",font=("deco",14))
        lab_material.pack()
        compo_material=ttk.Combobox(m,textvariable=self.material_var)
        compo_material = Label(m,text='حاسوب',bg="#ecf0f1",fg="black",font=("deco",14))
        compo_material.pack()
        self.material_var.set("حاسوب")
        lab_season= Label(m,text='الفصل',bg="#d7dbdd",font=("deco",14))
        lab_season.pack()
        compo_season=ttk.Combobox(m,textvariable=self.season_var)
        compo_season["value"]=("الفصل الثاني","الفصل الاول")
        compo_season.pack()
        lab_bass = Label(m,text='الشهر الاول',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month1= Entry(m,textvariable=self.month1_var,bd='2',justify=CENTER)
        month1.pack()
        lab_bass = Label(m,text='الشهر الثاني',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month2= Entry(m,textvariable=self.month2_var,bd='2',justify=CENTER)
        month2.pack()
        lab_bass = Label(m,text='الشهر الثالث',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month3= Entry(m,textvariable=self.month3_var,bd='2',justify=CENTER)
        month3.pack()
        lab_bass = Label(m,text='نهائي',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month4= Entry(m,textvariable=self.month4_var,bd='2',justify=CENTER)
        month4.pack()
        lab_delete = Label(m,text='حذف الطالب عن طريق الأسم',bg="#d7dbdd",
        font=("monospace",15),
        fg=("red"))
        lab_delete.pack()
        delete= Entry(m,bd='2',justify=CENTER,textvariable=self.delete_var)
        delete.pack()
        #--------------ادوات التحكم (الازرار)------------
        btn_frame=Frame(self.root ,bg=("#2980b9"))
        btn_frame.place(x=1350 , y=550 , width=510 , height=500)
        title1=Label(btn_frame,text="لوحة التحكم",bg="#2980b9",font=("bold",25),fg=("black"))
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text="إضافة",bg="#26dc15", font=("deco",20),command=self.add_student)
        add_btn.place(x=120 , y=60 , width=300 ,height=35 )
        delete_btn=Button(btn_frame,text="حذف الطالب عن طريق الاسم",bg="#dc2b15",font=("deco",20),command = self.delete)
        delete_btn.place(x=120 , y=120 , width=300 ,height=35 )
        update_btn=Button(btn_frame,text="تحديث البيانات الطالب",bg="#1559dc",font=("deco",20),command = self.update)
        update_btn.place(x=120 , y=180 , width=300 ,height=35 )
        cler_btn=Button(btn_frame,text="إفراغ الخانات",bg="#a19d9b",font=("deco",20),command = self.clear )
        cler_btn.place(x=120 , y=240 , width=300 ,height=35 )
        exit_btn=Button(btn_frame,text="خروج",bg="black",fg="white",font=("deco",20),command = root.quit)
        exit_btn.place(x=120 , y=300 , width=300 ,height=35 )
        #--------------------------البحث----------------------
        search_frame=Frame(self.root ,bg=("#2980b9"))
        search_frame.place(x=1 , y=45, width=1350 , height=100)
        lab_search=Label(search_frame,text=("البحث عن طالب عن طريق الرقم الوطني "),bg="white",font=("deco",18))
        lab_search.place(x=1000,y=20)
        compo_search=ttk.Combobox(search_frame,justify="right")
        search_Entry=Entry(search_frame , textvariable=self.search_var ,justify=CENTER , bd=2)
        search_Entry.place(x=850 ,y=30)
        search_btn=Button(search_frame,text="بحث",bg="#d8dddc",fg="black",font=("deco",20),command = self.search)
        search_btn.place(x=780 , y=26 , width=50 ,height=30 )
        #----------------عرض النتائج والبيانات---------------
        data_frame=Frame(self.root,bg="#f2f7f6")
        data_frame.place(x=1 , y=140, width=1345 , height=800)
        #-----------------القائمة-----------------------------
        scroll_x=Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(data_frame,orient=VERTICAL)
        #---------------------- الترتيب البيانات------------------------
        self.student_table=ttk.Treeview(data_frame,
         columns=("الرقم الوطني","اسم الطالب","المادة","الفصل","الشهر الاول","الشهر الثاني","الشهر الثالث","نهائي"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set )
        self.student_table.place(x=18 , y=1 ,width=1345 , height=780)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #---------------لإظهار السكرول---------------
        scroll_x.config(command=self.student_table.xview )
        scroll_y.config(command=self.student_table.yview )
        self.student_table["show"]="headings"
        self.student_table.heading("اسم الطالب",text="اسم الطالب")
        self.student_table.heading("الرقم الوطني",text="الرقم الوطني")
        self.student_table.heading("المادة",text="المادة")
        self.student_table.heading("الفصل",text="الفصل")
        self.student_table.heading("الشهر الاول",text="الشهر الاول")
        self.student_table.heading("الشهر الثاني",text="الشهر الثاني")
        self.student_table.heading("الشهر الثالث",text="الشهر الثالث")
        self.student_table.heading("نهائي",text="نهائي")
        self.student_table.column("الرقم الوطني",width=200)
        self.student_table.column("اسم الطالب",width=200)
        self.student_table.column("المادة",width=200)
        self.student_table.column("الفصل",width=200)
        self.student_table.column("الشهر الاول",width=200)
        self.student_table.column("الشهر الثاني",width=200)
        self.student_table.column("الشهر الثالث",width=200)
        self.student_table.column("نهائي",width=200)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #----------------إضافة البيانات إلى قاعدة البيانات------------
        self.fetch_all()
    def add_student(self):
            con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
            cur=con.cursor()
            cur.execute("insert into computer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.num_var.get(),
                                                                  self.name_var.get(),
                                                                  self.material_var.get(),
                                                                  self.season_var.get(),
                                                                  self.month1_var.get(),
                                                                  self.month2_var.get(),
                                                                  self.month3_var.get(),
                                                                  self.month4_var.get()
                                                                  
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
#------------------------ اضافة البييانات الى الجدول py (tk)بايثون تكنتر--------------------------
    def fetch_all(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("select * from computer")
        row=cur.fetchall()
        if len (row)!=0:
            self.student_table.delete(* self .student_table.get_children())
            for ro in row:
                self.student_table.insert("",END,values=ro)
            con.commit()
        con.close()
#----------------حذف عن طريق الاسم-----------------
    def delete (self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud")
        cur=con.cursor()
        cur.execute('delete from computer where name=%s', self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()
#-----------------------افراغ الخانات----------------------------
    def clear(self):
        self.num_var.set("")
        self.name_var.set("")
        self.material_var.set("")
        self.season_var.set("")
        self.month1_var.set("")
        self.month2_var.set("")
        self.month3_var.set("")
        self.month4_var.set("")
#------------------------تحديث بيانات الطالب------------------------
    def get_cursor(self,cu):
        cursor_ro = self.student_table.focus()
        co = self.student_table.item(cursor_ro)
        row =co["values"]
        self.num_var.set(row[0])
        self.name_var.set(row[1])
        self.material_var.set(row[2])
        self.season_var.set(row[3])
        self.month1_var.set(row[4])
        self.month2_var.set(row[5])
        self.month3_var.set(row[6])
        self.month4_var.set(row[7])
#----------------لتشغل زر تحديث البيانات---------------------------------
    def update(self) :
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("UPDATE computer SET name=%s, material=%s, season=%s, month1=%s, month2=%s, month3=%s, month4=%s WHERE num=%s", (
    self.name_var.get(),
    self.material_var.get(),
    self.season_var.get(),
    self.month1_var.get(),
    self.month2_var.get(),
    self.month3_var.get(),
    self.month4_var.get(),
    self.num_var.get()
))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
#--------------------------البحث-----------------------------
    def search(self):
        con = pymysql.connect(host="localhost", user="root", passwd="", database="stud")
        cur = con.cursor()
        search_column = "name" if self.search_by.get() == "عن طريق الاسم" else "num"
        query = f"SELECT * FROM computer WHERE {search_column} LIKE %s"
        search_value = "%" + str(self.search_var.get()) + "%"
        cur.execute(query, (search_value,))
        row = cur.fetchall()
        if len(row) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for ro in row:
                self.student_table.insert("", END, values=ro)
        con.commit()
        con.close()

#--------------نافدة التاريخ--------------
class History:
    
    #----------انشاء نافدة البرنامج---------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1850x950+1+1')
        self.root.title(' برنامج مدرسة القويسمة الثانوية للبنين')
        self.root.configure(background="#2980b9")
        self.root.resizable(False,FALSE)
        title = Label(self.root ,
        text ='......{تسجيل علامات  الطلاب}.....',
        background= "silver",
        font=("monospace",25),
        fg="white"
        )
        title.pack(fill=X)
        title.pack()
        #----------------------(variable)المتغيرات---------------
        self.name_var=StringVar()
        self.num_var=StringVar()
        self.material_var=StringVar()
        self.season_var=StringVar()
        self.month1_var=StringVar()
        self.month2_var=StringVar()
        self.month3_var=StringVar()
        self.month4_var=StringVar()
        self.delete_var=StringVar()
        self.search_var = StringVar()
        self.search_by = StringVar()       
#---------------ادوات التحكم في البرنامج-------------
        m = Frame(self.root,bg="#2980b9")
        m.place (x=1350,y=45,width=500,height=550)
        lab_titel =Label(m,text=' إضافة علامات الطلاب ',bg="#2980b9",
        font=("bold",23),
        fg=("black")
        )
        lab_titel.pack()
        lab_id = Label(m,text=' الرقم الوطني لطالب',bg="#d7dbdd",font=("deco",14))
        lab_id.pack()
        id= Entry(m,textvariable=self.num_var,bd='2',justify=CENTER)
        id.pack()
        lab_name = Label(m,text='اسم الطالب',bg="#d7dbdd",font=("deco",14))
        lab_name.pack()
        name= Entry(m,textvariable=self.name_var,bd='2',justify=CENTER)
        name.pack()
        lab_material= Label(m,text='المادة',bg="#d7dbdd",font=("deco",14))
        lab_material.pack()
        compo_material=ttk.Combobox(m,textvariable=self.material_var)
        compo_material = Label(m,text='تاريخ الأردن',bg="#ecf0f1",fg="black",font=("deco",14))
        compo_material.pack()
        self.material_var.set("تاريخ الأردن")
        lab_season= Label(m,text='الفصل',bg="#d7dbdd",font=("deco",14))
        lab_season.pack()
        compo_season=ttk.Combobox(m,textvariable=self.season_var)
        compo_season["value"]=("الفصل الثاني","الفصل الاول")
        compo_season.pack()
        lab_bass = Label(m,text='الشهر الاول',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month1= Entry(m,textvariable=self.month1_var,bd='2',justify=CENTER)
        month1.pack()
        lab_bass = Label(m,text='الشهر الثاني',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month2= Entry(m,textvariable=self.month2_var,bd='2',justify=CENTER)
        month2.pack()
        lab_bass = Label(m,text='الشهر الثالث',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month3= Entry(m,textvariable=self.month3_var,bd='2',justify=CENTER)
        month3.pack()
        lab_bass = Label(m,text='نهائي',bg="#d7dbdd",font=("deco",14))
        lab_bass.pack()
        month4= Entry(m,textvariable=self.month4_var,bd='2',justify=CENTER)
        month4.pack()
        lab_delete = Label(m,text='حذف الطالب عن طريق الأسم',bg="#d7dbdd",
        font=("monospace",15),
        fg=("red"))
        lab_delete.pack()
        delete= Entry(m,bd='2',justify=CENTER,textvariable=self.delete_var)
        delete.pack()
        #--------------ادوات التحكم (الازرار)------------
        btn_frame=Frame(self.root ,bg=("#2980b9"))
        btn_frame.place(x=1350 , y=550 , width=510 , height=500)
        title1=Label(btn_frame,text="لوحة التحكم",bg="#2980b9",font=("bold",25),fg=("black"))
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text="إضافة",bg="#26dc15", font=("deco",20),command=self.add_student)
        add_btn.place(x=120 , y=60 , width=300 ,height=35 )
        delete_btn=Button(btn_frame,text="حذف الطالب عن طريق الاسم",bg="#dc2b15",font=("deco",20),command = self.delete)
        delete_btn.place(x=120 , y=120 , width=300 ,height=35 )
        update_btn=Button(btn_frame,text="تحديث البيانات الطالب",bg="#1559dc",font=("deco",20),command = self.update)
        update_btn.place(x=120 , y=180 , width=300 ,height=35 )
        cler_btn=Button(btn_frame,text="إفراغ الخانات",bg="#a19d9b",font=("deco",20),command = self.clear )
        cler_btn.place(x=120 , y=240 , width=300 ,height=35 )
        exit_btn=Button(btn_frame,text="خروج",bg="black",fg="white",font=("deco",20),command = root.quit)
        exit_btn.place(x=120 , y=300 , width=300 ,height=35 )
        #--------------------------البحث----------------------
        search_frame=Frame(self.root ,bg=("#2980b9"))
        search_frame.place(x=1 , y=45, width=1350 , height=100)
        lab_search=Label(search_frame,text=("البحث عن طالب عن طريق الرقم الوطني "),bg="white",font=("deco",18))
        lab_search.place(x=1000,y=20)
        compo_search=ttk.Combobox(search_frame,justify="right")
        search_Entry=Entry(search_frame , textvariable=self.search_var ,justify=CENTER , bd=2)
        search_Entry.place(x=850 ,y=30)
        search_btn=Button(search_frame,text="بحث",bg="#d8dddc",fg="black",font=("deco",20),command = self.search)
        search_btn.place(x=780 , y=26 , width=50 ,height=30 )
        #----------------عرض النتائج والبيانات---------------
        data_frame=Frame(self.root,bg="#f2f7f6")
        data_frame.place(x=1 , y=140, width=1345 , height=800)
        #-----------------القائمة-----------------------------
        scroll_x=Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(data_frame,orient=VERTICAL)
        #---------------------- الترتيب البيانات------------------------
        self.student_table=ttk.Treeview(data_frame,
         columns=("الرقم الوطني","اسم الطالب","المادة","الفصل","الشهر الاول","الشهر الثاني","الشهر الثالث","نهائي"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set )
        self.student_table.place(x=18 , y=1 ,width=1345 , height=780)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #---------------لإظهار السكرول---------------
        scroll_x.config(command=self.student_table.xview )
        scroll_y.config(command=self.student_table.yview )
        self.student_table["show"]="headings"
        self.student_table.heading("اسم الطالب",text="اسم الطالب")
        self.student_table.heading("الرقم الوطني",text="الرقم الوطني")
        self.student_table.heading("المادة",text="المادة")
        self.student_table.heading("الفصل",text="الفصل")
        self.student_table.heading("الشهر الاول",text="الشهر الاول")
        self.student_table.heading("الشهر الثاني",text="الشهر الثاني")
        self.student_table.heading("الشهر الثالث",text="الشهر الثالث")
        self.student_table.heading("نهائي",text="نهائي")
        self.student_table.column("الرقم الوطني",width=200)
        self.student_table.column("اسم الطالب",width=200)
        self.student_table.column("المادة",width=200)
        self.student_table.column("الفصل",width=200)
        self.student_table.column("الشهر الاول",width=200)
        self.student_table.column("الشهر الثاني",width=200)
        self.student_table.column("الشهر الثالث",width=200)
        self.student_table.column("نهائي",width=200)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #----------------إضافة البيانات إلى قاعدة البيانات------------
        self.fetch_all()
    def add_student(self):
            con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
            cur=con.cursor()
            cur.execute("insert into history values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                  self.num_var.get(),
                                                                  self.name_var.get(),
                                                                  self.material_var.get(),
                                                                  self.season_var.get(),
                                                                  self.month1_var.get(),
                                                                  self.month2_var.get(),
                                                                  self.month3_var.get(),
                                                                  self.month4_var.get()
                                                                  
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
#------------------------ اضافة البييانات الى الجدول py (tk)بايثون تكنتر--------------------------
    def fetch_all(self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("select * from history")
        row=cur.fetchall()
        if len (row)!=0:
            self.student_table.delete(* self .student_table.get_children())
            for ro in row:
                self.student_table.insert("",END,values=ro)
            con.commit()
        con.close()
#----------------حذف عن طريق الاسم-----------------
    def delete (self):
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud")
        cur=con.cursor()
        cur.execute('delete from history where name=%s', self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()
#-----------------------افراغ الخانات----------------------------
    def clear(self):
        self.num_var.set("")
        self.name_var.set("")
        self.material_var.set("")
        self.season_var.set("")
        self.month1_var.set("")
        self.month2_var.set("")
        self.month3_var.set("")
        self.month4_var.set("")
#------------------------تحديث بيانات الطالب------------------------
    def get_cursor(self,cu):
        cursor_ro = self.student_table.focus()
        co = self.student_table.item(cursor_ro)
        row =co["values"]
        self.num_var.set(row[0])
        self.name_var.set(row[1])
        self.material_var.set(row[2])
        self.season_var.set(row[3])
        self.month1_var.set(row[4])
        self.month2_var.set(row[5])
        self.month3_var.set(row[6])
        self.month4_var.set(row[7])
#----------------لتشغل زر تحديث البيانات---------------------------------
    def update(self) :
        con=pymysql.connect(host="localhost",user="root",passwd="",database="stud" )
        cur=con.cursor()
        cur.execute("UPDATE history SET name=%s, material=%s, season=%s, month1=%s, month2=%s, month3=%s, month4=%s WHERE num=%s", (
    self.name_var.get(),
    self.material_var.get(),
    self.season_var.get(),
    self.month1_var.get(),
    self.month2_var.get(),
    self.month3_var.get(),
    self.month4_var.get(),
    self.num_var.get()
))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
#--------------------------البحث-----------------------------
    def search(self):
        con = pymysql.connect(host="localhost", user="root", passwd="", database="stud")
        cur = con.cursor()
        search_column = "name" if self.search_by.get() == "عن طريق الاسم" else "num"
        query = f"SELECT * FROM history WHERE {search_column} LIKE %s"
        search_value = "%" + str(self.search_var.get()) + "%"
        cur.execute(query, (search_value,))
        row = cur.fetchall()
        if len(row) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for ro in row:
                self.student_table.insert("", END, values=ro)
        con.commit()
        con.close()


root = Tk()
app = Program(root)
root.mainloop()
root = Tk()
apppp = English(root)
root.quit()
root = Tk()
appp = Islamic(root)
root.quit()
root =Tk()
appppp=Computer(root)
root.quit()
root =Tk()
apppppp=History(root)
root.quit()
