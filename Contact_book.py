#importam modulul tkinter cu toate atributele lui --> folosim elemente GUI din ea
from tkinter import *

#initializam fereastra care se deschide
root = Tk() #### ---cream fereastra principala (tkinter window)
root.geometry('450x350') ### --- fixam dimensiunea ferestrei
root.config(bg='darksalmon') ### -- setam culoarea de background
root.title('Agenda de contacte') ### - setam titlul ferestrei
root.resizable(0,0) ### - dimensiunile ferestrei nu pot fi modificqate
listaContacte = [
    ['Panturu Elena', '0727825194', 'elenapanturu29@gmailcom'],
    ['Mos Craciun', '1234567890', 'mos_craciun_veriffied@gmail.com']

] ### - lista intiala de contacte, pentru exemplu
nume=StringVar()
telefon=StringVar()
email=StringVar()

#cream frame-ul (un fel de chenar imaginar care ne permita sa ne jucam cu widgeturile)
frame=Frame(root)
#frame.pack(side = LEFT)
frame.place(x=270, y=100) ## - unde e pozitionat in frame
scroll = Scrollbar(frame, orient=VERTICAL)
select=Listbox(frame, yscrollcommand=scroll.set, height=8, bg='peachpuff') ## - controlam cum arata listboxul
scroll.config (command=select.yview) # sa fie scrollat vertical
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)



#functie de selectat contactul
def Selected():
    return int(select.curselection()[0])

#functie in care adaugam un nou contact
def AddContact():
    listaContacte.append([nume.get(), telefon.get(), email.get()])
    Select_set()

#functie de editat contactele deja exitente
def EDIT():
    listaContacte[Selected()]=[nume.get(), telefon.get(), email.get()]
    Select_set()

#functie de sters contacte
def DELETE():
    del listaContacte[Selected()]
    Select_set()

#sa vedem datele contactului selectat
def VIEW():
    NUME, TELEFON, EMAIL=listaContacte[Selected()]
    nume.set(NUME)
    telefon.set(TELEFON)
    email.set(EMAIL)

def Select_set():
    listaContacte.sort()
    select.delete(0, END)
    for nume, telefon, email in listaContacte:
        select.insert(END, nume)
Select_set()

#butoane, labels si entry
Label(root, text='Nume:', font='Arial 11', bg='darksalmon').place(x=40, y=100)
Entry(root, textvariable=nume, bg='peachpuff').place(x=110, y=100)
Label(root, text="Telefon:", font='Arial 11', bg='darksalmon').place(x=40, y=150)
Entry(root, textvariable=telefon, bg='peachpuff').place(x=110, y=150)
Label(root, text='Email:', font='helvetica 11', bg='darksalmon').place(x=40, y=200)
Entry(root, textvariable=email, bg='peachpuff').place(x=110, y=200)

Button(root,text=" ADD", font='arial 8',bg='peachpuff', command = AddContact).place(x= 40, y=250)
Button(root,text="EDIT", font='arial 8',bg='peachpuff',command = EDIT).place(x= 90, y=250)
Button(root,text="VIEW", font='arial 8',bg='peachpuff', command = VIEW).place(x= 140, y=250)
Button(root,text="DELETE", font='arial 8',bg='peachpuff',command = DELETE).place(x= 190, y=250)

#canvas=Canvas(root, width=200, height=180)
#canvas.pack()
#photo = PhotoImage(file = r'C:\Users\Delltemir\Desktop\ContactBook\logo.png')
#canvas.create_image(100,60, anchor=N,  image=photo)
#photo = PhotoImage. resize(100, 150)
#Button(root, image=photo).place(x=40, y= 30)

root.mainloop() ### ---executam tot (execute tkinter)


##problema 1 -- de ce nu merg fonturile tnr, helvetica, verdana, whatever
##problema 2 -- nu merg functiile:)))
##problema 3 -- some automatic testing
##problema 4 --
