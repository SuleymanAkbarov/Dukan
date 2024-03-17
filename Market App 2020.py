import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
import datetime
from datetime import date
import winsound

window = Tk()
icon = PhotoImage(file='DukanApp.png')
window.iconphoto(False, icon)


class Application(object):
    Mahsul = []
    with open('mahsul_ad.txt', 'r') as data1:
        if data1:
            for line in data1:
                pl = line[:-1]
                Mahsul.append([])
                key = Mahsul[len(Mahsul)-1]
                key.append(pl)
            data1.close()
    with open('mahsul_ist.txt', 'r') as data1:
        if data1:
            k = 0
            for line in data1:
                pl = line[:-1]
                key = Mahsul[k]
                key.append(pl)
                k += 1
            data1.close()
    with open('mahsul_son.txt', 'r') as data1:
        if data1:
            k = 0
            for line in data1:
                pl = line[:-1]
                key = Mahsul[k]
                key.append(pl)
                k += 1
            data1.close()
    with open('mahsul_id.txt', 'r') as data1:
        if data1:
            k = 0
            for line in data1:
                pl = line[:-1]
                key = Mahsul[k]
                key.append(int(pl))
                k += 1
            data1.close()

    def __init__(self, window):
        self.window = window
        self.tree = None
        self.setWidget()

    def setWidget(self):
        self.yer = StringVar()
        self.yer.trace("w", self.istifademuddeti)

        # Fram1
        self.fram1 = Frame(master=window, height=45, bg="silver")
        self.fram1.pack(fill=X, side=TOP)

        self.bugun = Entry(self.fram1, textvariable=self.yer, state="disabled")
        self.bugun.place(x=0, y=0)

        # Fram
        self.fram = Frame(master=window, height=100, bg="yellowgreen")
        self.fram.place(y=100)
        self.fram.pack(fill=X)

        # Font
        self.Font = tkFont.Font(size=15)

        self.search_var = StringVar()
        self.search_var.trace("w", self.Search)

        # Searching
        self.searching = Entry(master=self.fram, textvariable=self.search_var, width=32, font=self.Font)
        self.searching.place(x=180, y=30)

        # Label
        self.text = Label(master=self.fram, text='Product Search:', fg="white", bg="yellowgreen", font=self.Font)
        self.text.place(x=30, y=26)

        # Add Button
        self.add = Button(master=self.fram, text="Add", command=self.new_window, width=9,
                          height=2, bg="darkgreen", fg="white", font=self.Font)
        self.add.place(x=700, y=18)

        # Delete Button
        self.delete = Button(master=self.fram, text="Delete", command=self.deleting, width=9, height=2, bg="red",
                             fg="white",
                             font=self.Font)
        self.delete.place(x=850, y=18)

        # Edit Button
        self.edit = Button(master=self.fram, text="Edit", command=self.editing, width=9, height=2, bg="yellow",
                           fg="black",
                           font=self.Font)
        self.edit.place(x=1000, y=18)

        # Tree frame
        self.tre = Frame(window, height=100, width=1120)
        self.tre.place(x=40, y=180)

        # Scrollbar
        self.scrollbar = Scrollbar(window)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.tree = ttk.Treeview(self.tre)
        self.tree["columns"] = "one", "two", "three", "four"
        self.tree.column("#0", width=50, minwidth=50, stretch=NO)
        self.tree.column("one", width=267, minwidth=267, stretch=NO)
        self.tree.column("two", width=267, minwidth=267, stretch=NO)
        self.tree.column("three", width=267, minwidth=267, stretch=NO)
        self.tree.column("four", width=267, minwidth=267, stretch=NO)

        self.tree.heading("#0", text="№", anchor=CENTER)
        self.tree.heading("one", text="Product Name", anchor=CENTER)
        self.tree.heading("two", text="Production Date", anchor=CENTER)
        self.tree.heading("three", text="Expiry Date", anchor=CENTER)
        self.tree.heading("four", text="Usage Period", anchor=CENTER)

        self.style1 = ttk.Style()
        self.style1.theme_use("default")
        self.style1.configure("Treeview", fieldbackground="lightgoldenrodyellow", rowheight=30,
                              font=(None, 15), )
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 18), background="skyblue")
        self.tree.pack(fill=BOTH, expand=1)
        self.Search()
        self.istifademuddeti()
        self.upd()

    def new_window(self):
        self.searching.config(state="disabled")
        self.add.config(state="disabled")
        self.delete.config(state="disabled")
        self.edit.config(state="disabled")

        self.newWin = Toplevel(master=window, bg="palegoldenrod")
        self.newWin.resizable(width=FALSE, height=FALSE)
        self.newWin.title("New Product")
        self.newWin.attributes("-toolwindow", True)
        self.newWin.attributes("-topmost", True)
        self.newWin.geometry('500x300+500+300')
        self.nam = Label(master=self.newWin, text="Product Name:", fg="black", bg="palegoldenrod")
        self.nam.place(x=30, y=40)
        self.entry1 = Entry(master=self.newWin, width=45)
        self.entry1.place(x=150, y=40)
        self.entry1.focus()

        # Production date
        def calendar():
            def ok():
                self.entry2.configure(state='normal')
                x = cal.selection_get()
                self.entry2.delete(0, END)
                self.entry2.insert(0, x)
                self.entry2.configure(state='disabled')
                top.destroy()

            top = Toplevel(self.newWin)
            top.attributes("-toolwindow", True)
            top.attributes("-topmost", True)
            top.geometry("300x240+920+420")
            top.resizable(0, 0)
            Button(top, bg="red", width=5, text="OK", command=ok).pack(side=BOTTOM)
            now = datetime.datetime.now()

            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand1", day=now.day, month=now.month, year=now.year)
            cal.pack(fill="both", expand=True)

        # ****************
        def record():
            a = self.entry1.get()
            b = self.entry2.get()
            c = self.entry3.get()

            if a == "":
                a = "Product {k:3d}".format(k=len(Application.Mahsul) + 1)
            if b == "":
                b = str(date.today())
            if c == "":
                c = str(date.today())

            Application.Mahsul.append([])
            r = Application.Mahsul[len(Application.Mahsul) - 1]
            r.append(a)
            r.append(b)
            r.append(c)
            r.append(len(Application.Mahsul))

            self.istifademuddeti()

            self.Activ()
            winsound.Beep(3000, 150)

        # ***************

        def calendar2():
            def ok2():
                self.entry3.configure(state='normal')
                y = cal1.selection_get()
                self.entry3.delete(0, END)
                self.entry3.insert(0, y)
                self.entry3.configure(state='disabled')
                top1.destroy()

            top1 = Toplevel(self.newWin)
            top1.attributes("-toolwindow", True)
            top1.attributes("-topmost", True)
            top1.geometry("300x240+920+420")
            top1.resizable(0, 0)
            Button(top1, bg="red", width=5, text="OK", command=ok2).pack(side=BOTTOM)
            now = datetime.datetime.now()
            cal1 = Calendar(top1,
                            font="Arial 14", selectmode='day',
                            cursor="hand1", day=now.day, month=now.month, year=now.year)
            cal1.pack(fill="both", expand=True)

        self.datePr = Label(master=self.newWin, text="Production Date:", fg="black", bg="palegoldenrod")
        self.datePr.place(x=30, y=100)
        x = StringVar()
        self.entry2 = Entry(self.newWin, state='disabled', textvariable=x, width=35)
        self.entry2.place(x=150, y=100)
        self.cho = Button(master=self.newWin, text="Select", width=5, command=calendar)
        self.cho.place(x=370, y=95)
        self.lastDat = Label(master=self.newWin, text="Expiry Date:", fg="black", bg="palegoldenrod")
        self.lastDat.place(x=30, y=160)

        y = StringVar()
        self.entry3 = Entry(self.newWin, state='disabled', textvariable=y, width=35)
        self.entry3.place(x=150, y=160)
        self.cho2 = Button(self.newWin, text="Select", width=5, command=calendar2)
        self.cho2.place(x=370, y=155)

        save = Button(master=self.newWin, text="Add", command=record)
        save.place(x=290, y=230)
        cancel = Button(master=self.newWin, text="Cancel", command=self.Activ)
        cancel.place(x=360, y=230)
        self.newWin.protocol('WM_DELETE_WINDOW', self.Activ)

        # Delete

    def deleting(self):
        if self.tree.focus() != "":
            result = messagebox.askyesno("Delete", "Are you sure to delete?")
            if result:
                selected_item = str(self.tree.selection()[0])
                for itemIID in Application.Mahsul:
                    IID = str(itemIID[3])
                    if IID == selected_item:
                        Application.Mahsul.remove(itemIID)
                        break
                self.tree.delete(selected_item)
                for nu in range(0, len(Application.Mahsul), 1):
                    meh = Application.Mahsul[nu][3]
                    mah = Application.Mahsul[nu]
                    mah.remove(meh)
                    mah.append(nu + 1)
                self.istifademuddeti()

    def Search(self, *args):
        val = self.search_var.get()
        if val != "":
            self.tree.delete(*self.tree.get_children())
            ka = 0

            for item in Application.Mahsul:
                item1 = item[0]
                item2 = item[3]
                if val.lower() in item1.lower():
                    ka += 1
                    d1 = date.today()
                    d2 = date.fromisoformat(item[2])
                    delta1 = (d2 - d1).days
                    if delta1 <= 0:
                        delta1 = "Expired"
                    elif 0 == delta1 // 30:
                        delta1 = "{yem:2d} day".format(yem=delta1 % 30)
                    elif 1 <= delta1 // 30 < 12 and delta1 % 30 == 0:
                        delta1 = "{rem:2d} month".format(rem=delta1 // 30)
                    elif 1 <= delta1 // 30 < 12:
                        delta1 = "{rem:2d} month {yem:2d} day".format(rem=delta1 // 30, yem=delta1 % 30)
                    elif delta1 // 365 == 1 and delta1 % 365 == 0:
                        delta1 = "{ye:5d} year".format(ye=delta1 // 365)
                    elif delta1 // 365 >= 1 and 30 > (delta1 - (delta1 // 365) * 365):
                        delta1 = "{ye:5d} year {day1:2d} day".format(ye=delta1 // 365,
                                                                   day1=delta1 - (delta1 // 365) * 365)
                    else:
                        delta1 = "{ye:5d} year {mon:2d} month {da:2d} day".format(ye=delta1 // 365,
                                                                             mon=(delta1 - (
                                                                                     delta1 // 365) * 365) // 30,
                                                                             da=(delta1 - (
                                                                                     delta1 // 365) * 365) % 30)
                    self.tree.insert("", 30, text=ka,
                                     values=(item[0], item[1], item[2], delta1), iid=item2)
        else:
            self.istifademuddeti()

    def editing(self):
        if self.tree.focus() != "":
            selected_item = self.tree.selection()[0]  # get selected item
            self.searching.config(state="disabled")
            self.add.config(state="disabled")
            self.delete.config(state="disabled")
            self.edit.config(state="disabled")
            self.editor = Toplevel(master=window, bg="palegoldenrod")
            self.editor.title("Edit")
            self.editor.resizable(width=FALSE, height=FALSE)
            self.editor.attributes("-toolwindow", True)
            self.editor.attributes("-topmost", True)
            self.editor.geometry('500x300+500+300')
            self.nam = Label(master=self.editor, text="Product Name:", fg="black", bg="palegoldenrod")
            self.nam.place(x=30, y=40)
            self.entry1 = Entry(master=self.editor, width=45)
            self.entry1.place(x=150, y=40)
            self.entry1.focus()

            # Production date
            def calendar():
                def ok():
                    self.entry2.configure(state='normal')
                    x = cal.selection_get()
                    self.entry2.delete(0, END)
                    self.entry2.insert(0, x)
                    self.entry2.configure(state='disabled')
                    top.destroy()

                top = Toplevel(self.editor)
                top.attributes("-toolwindow", True)
                top.attributes("-topmost", True)
                top.geometry("300x240+920+420")
                top.resizable(0, 0)
                Button(top, bg="red", width=5, text="OK", command=ok).pack(side=BOTTOM)
                now = datetime.datetime.now()

                cal = Calendar(top,
                               font="Arial 14", selectmode='day',
                               cursor="hand1", day=now.day, month=now.month, year=now.year)
                cal.pack(fill="both", expand=True)

            # ****************
            def record():
                for itemIID in Application.Mahsul:
                    IID = str(itemIID[3])
                    if IID == selected_item:
                        Application.Mahsul.remove(itemIID)
                        break
                self.tree.delete(selected_item)

                a = self.entry1.get()
                b = self.entry2.get()
                c = self.entry3.get()

                Application.Mahsul.append([])
                r = Application.Mahsul[len(Application.Mahsul) - 1]
                r.append(a)
                r.append(b)
                r.append(c)
                r.append(len(Application.Mahsul))

                for nu in range(0, len(Application.Mahsul), 1):
                    meh = Application.Mahsul[nu][3]
                    mah = Application.Mahsul[nu]
                    mah.remove(meh)
                    mah.append(nu + 1)
                self.istifademuddeti()
                self.Activ2()
                winsound.Beep(3000, 150)

            # ***************

            def calendar2():
                def ok2():
                    self.entry3.configure(state='normal')
                    y = cal1.selection_get()
                    self.entry3.delete(0, END)
                    self.entry3.insert(0, y)
                    self.entry3.configure(state='disabled')
                    top1.destroy()

                top1 = Toplevel(self.editor)
                top1.attributes("-toolwindow", True)
                top1.attributes("-topmost", True)
                top1.geometry("300x240+920+420")
                top1.resizable(0, 0)
                Button(top1, bg="red", width=5, text="OK", command=ok2).pack(side=BOTTOM)
                now = datetime.datetime.now()

                cal1 = Calendar(top1,
                                font="Arial 14", selectmode='day',
                                cursor="hand1", day=now.day, month=now.month, year=now.year)
                cal1.pack(fill="both", expand=True)

            self.datePr = Label(master=self.editor, text="Production Date:", fg="black", bg="palegoldenrod")
            self.datePr.place(x=30, y=100)
            x = StringVar()
            self.entry2 = Entry(self.editor, state='disabled', textvariable=x, width=35)
            self.entry2.place(x=150, y=100)
            self.cho = Button(master=self.editor, text="Select", width=5, command=calendar)
            self.cho.place(x=370, y=95)
            self.lastDat = Label(master=self.editor, text="Expiry Date:", fg="black", bg="palegoldenrod")
            self.lastDat.place(x=30, y=160)

            y = StringVar()
            self.entry3 = Entry(self.editor, state='disabled', textvariable=y, width=35)
            self.entry3.place(x=150, y=160)
            self.cho2 = Button(self.editor, text="Select", width=5, command=calendar2)
            self.cho2.place(x=370, y=155)

            # Writing
            self.entryIndex = self.tree.focus()
            self.entry2.configure(state='normal')
            self.entry3.configure(state='normal')
            for child in self.tree.get_children():
                if child == self.entryIndex:
                    self.values = self.tree.item(child)["values"]
                    break
            self.entry1.insert(0, self.values[0])
            self.entry2.insert(0, self.values[1])
            self.entry3.insert(0, self.values[2])
            self.entry2.configure(state='disabled')
            self.entry3.configure(state='disabled')

            save = Button(master=self.editor, text="Save", command=record)
            save.place(x=270, y=230)
            cancel = Button(master=self.editor, text="Cancel", command=self.Activ2)
            cancel.place(x=360, y=230)
            self.editor.protocol('WM_DELETE_WINDOW', self.Activ2)
        else:
            messagebox.showwarning("Info", "Please select a product to edit")

    def Activ(self):
        self.add.config(state="normal")
        self.delete.config(state="normal")
        self.edit.config(state="normal")
        self.searching.config(state="normal")
        self.newWin.destroy()

    def Activ2(self):
        self.add.config(state="normal")
        self.delete.config(state="normal")
        self.edit.config(state="normal")
        self.searching.config(state="normal")
        self.editor.destroy()

    def istifademuddeti(self, *args):
        Num = []
        for fn in range(0, len(Application.Mahsul), 1):
            h = Application.Mahsul[fn][2]
            d2 = date.fromisoformat(h)
            d1 = date.today()
            delta1 = (d2 - d1).days
            Num.append([])
            er = Num[len(Num) - 1]
            er.append(fn)
            er.append(delta1)
        self.tree.delete(*self.tree.get_children())
        sira = 1
        self.tree.tag_configure('fg', foreground="#fa6800")
        for i in range(0, len(Application.Mahsul), 1):
            i = 0
            delta1 = Num[i][1]
            ind = Num[i][0]
            indi = i
            for j in range(0, len(Num), 1):
                delta2 = Num[j][1]
                if delta1 < delta2:
                    pass
                else:
                    delta1 = delta2
                    ind = Num[j][0]
                    indi = j

            if delta1 <= 0:
                delta1 = "Expired"
            elif 0 == delta1 // 30:
                delta1 = "{yem:2d} day".format(yem=delta1 % 30)
            elif 1 <= delta1 // 30 < 12 and delta1 % 30 == 0:
                delta1 = "{rem:2d} ay".format(rem=delta1 // 30)
            elif 1 <= delta1 // 30 < 12:
                delta1 = "{rem:2d} ay {yem:2d} gün".format(rem=delta1 // 30, yem=delta1 % 30)
            elif delta1 // 365 == 1 and delta1 % 365 == 0:
                delta1 = "{ye:5d} year".format(ye=delta1 // 365)
            elif delta1 // 365 >= 1 and 30 > (delta1 - (delta1 // 365) * 365):
                delta1 = "{ye:5d} year {day1:2d} day".format(ye=delta1 // 365,
                                                           day1=delta1 - (delta1 // 365) * 365)
            else:
                delta1 = "{ye:5d} year {mon:2d} month {da:2d} day".format(ye=delta1 // 365,
                                                                     mon=(delta1 - (
                                                                             delta1 // 365) * 365) // 30,
                                                                     da=(delta1 - (
                                                                             delta1 // 365) * 365) % 30)
            self.tree.insert("", 'end', text=sira,
                             values=(Application.Mahsul[ind][0],
                                     Application.Mahsul[ind][1],
                                     Application.Mahsul[ind][2], delta1), iid=Application.Mahsul[ind][3], tags='fg')
            sira += 1
            Num.remove(Num[indi])
        with open('mahsul_ad.txt', 'w', encoding="utf-8") as data:
            data.truncate()
            for itemm in Application.Mahsul:
                f = itemm[0]
                data.write('%s\n' % f)
            data.close()
        with open('mahsul_ist.txt', 'w', encoding="utf-8") as data:
            data.truncate()
            for itemm in Application.Mahsul:
                s = itemm[1]
                data.write('%s\n' % s)
            data.close()
        with open('mahsul_son.txt', 'w', encoding="utf-8") as data:
            data.truncate()
            for itemm in Application.Mahsul:
                p = itemm[2]
                data.write('%s\n' % p)
            data.close()
        with open('mahsul_id.txt', 'w', encoding="utf-8") as data:
            data.truncate()
            for itemm in Application.Mahsul:
                n = itemm[3]
                data.write('%s\n' % n)
            data.close()

    def upd(self):

        self.bugun.config(state="normal")
        self.bugun.delete(0, END)
        self.bugun.insert(0, date.today())
        self.bugun.config(state="disabled")
        self.bugun.after(600000, self.upd)


window.geometry("1200x690+220+90")
window.title("Dükan")
App = Application(window)
window.mainloop()
