from tkinter import *
from tkinter import ttk # theme of tk
import csv
from datetime import datetime

datetime.now().strftime('%Y-%m-%d') # website  strftime.org

def savetocsv(data=['Coffee','Drink',50]):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.geometry('700x600')
#GUI.state('zoomed')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')
######################################
# widget 
L = Label(GUI,text='โปรแกรมบันทึกค่าใช้จ่าย',font=('Angsana New',30))
L.pack()
L = ttk.Label(GUI,text='โปรแกรมบันทึกค่าใช้จ่าย',font=('Angsana New',30))
L.pack()
###################################

L = ttk.Label(GUI,text='รายการค่าใช้จ่าย',font=('Angsana New',20))
L.pack(pady=5)

L = Label(GUI,text='Yen = 0.25 บาท/เยน',font=('Angsana New',30))
L.pack()
L = Label(GUI,text='Usd = 35.8 บาท/Usd',font=('Angsana New',30))
L.pack()
######################################

E = Entry(GUI,font=('Angsana New',30))
E.pack()
########################################
C = ttk.Combobox(GUI,font=('Angsana New',20),width=30)
GUI.option_add('*TCombobox*Listbox.font',('Angsana New',30))
C.set('ค่าเดินทาง')
C['values'] = ['ค่าอาหาร','ค่าเดินทาง','บัตรเครดิต']
C.pack(pady=10)
#########################################
v_expense = StringVar()
E = ttk.Entry(GUI,textvariable=v_expense ,font=('Angsana New',30),width=20)
E.pack()


C = ttk.Combobox(GUI)
C.pack()
##########################################
def Save(event=None):
    expense = v_expense.get()
    expense_type = C.get()  
    print(expense)
    print(expense_type)
    # convert price from str to float
    #calvat = float(price) * 1.07
    d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [d,expense,expense_type]
    savetocsv(data)
    # clear data in form
    v_expense.set('')
    E.focus() # move cursor to E

E.bind('<Return>',Save) # event = None

B = Button(GUI,text='Save',command=Save)
B.pack(ipadx=20,ipady=10)
B = ttk.Button(GUI,text='Save')
B.pack(ipadx=20,ipady=10,pady=20)

B = ttk.Button(GUI,text='A')
B.place(x=50,y=50)

B = ttk.Button(GUI,text='B')
B.place(x=500,y=500)
#########################################
F = Frame(GUI)
F.place(x=50,y=500)

B = ttk.Button(F,text='A')
B.grid(row=0,column=0)

B = ttk.Button(F,text='B')
B.grid(row=0,column=1)
########################################

GUI.mainloop()