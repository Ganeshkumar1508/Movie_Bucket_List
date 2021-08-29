import tkinter as tk
import sqlite3



def main():
    global root
    root = tk.Tk()
    root.title("Movie List")
    root.geometry("500x500")
    root.resizable(0, 0)
    root.configure(background="#e5edf1")
    root.columnconfigure(0,weight=1)
    l1 = tk.Label(root, text="Movie List", fg="black", bg="#e5edf1", borderwidth=3, relief="solid", font=("Rockwell",22,"bold")).grid(row=0, column=0, padx=10, pady=20,ipadx=10)
    b1 = tk.Button(root, height=3, width=40, bg="#add8e6", fg="#0a0a0a", text="Add Movie Details", font=("Franklin Gothic",10,"bold"), command=movielist).grid(row=1, column=0, pady=50, padx=15)
    b2 = tk.Button(root, height=3, width=40, bg="#add8e6", fg="#0a0a0a", text="Show Movie Details", font=("Franklin Gothic",10,"bold"), command=viewlist).grid(row=2, column=0, pady=50, padx=15)

    root.mainloop()

def back():
    newWindow.destroy()
    main()

def back1():
    newWindow2.destroy()
    main()

def dat():
    conn = sqlite3.connect(r'C:\Users\GANESH KUMAR M A\Desktop\Movie Bucket List\movies.db')
    conn.execute("""CREATE TABLE IF NOT EXISTS MOVIES(Movie_Name Text, Lead_Actor_Name CHAR(255),Lead_Actress_Name CHAR(255), Year_Of_Release CHAR(255),Director CHAR(255));""")
    conn.execute("""INSERT INTO MOVIES (Movie_Name, Lead_Actor_Name, Lead_Actress_Name, Year_Of_Release, Director) VALUES (?,?,?,?,?)""" , (mname.get(), aname.get(), aname2.get(), year.get(), dirc.get()))
    conn.commit()
    conn.close()
    l7 = tk.Label(newWindow, text="Submitted Succesfully", fg="black", bg="#e5edf1", font=("Garamond",15,"bold")).grid(row=7, column=1, pady=15, padx=10)
    #back()
    



def movielist():
    root.destroy()
    global newWindow
    newWindow = tk.Tk()
    newWindow.title("Movie List")
    newWindow.geometry("500x500")
    newWindow.resizable(0, 0)
    newWindow.configure(background="#e5edf1")

    global mname,aname,aname2,year,dirc
   
   
    b3 = tk.Button(newWindow, width=10, bg="#add8e6", fg="#0a0a0a", text="Back", font=("Franklin Gothic",10,"bold"), command=back).grid(row=0, column=0, pady=15, padx=10, sticky="w")
    l2 = tk.Label(newWindow,text="Movie Name: ", fg="black", bg="#e5edf1", font=("Garamond",15,"bold")).grid(row=1, column=0, pady=20, padx=25, sticky="w")
    mname = tk.Entry(text="", font=12, width=25)
    mname.grid(row=1, column=1, pady=10, padx=5, sticky="w", ipady=8)
    l3 = tk.Label(newWindow, text="Lead Actor Name: ", fg="black", bg="#e5edf1", font=("Garamond",15,"bold")).grid(row=2, column=0, pady=20, padx=25, sticky="w")
    aname = tk.Entry(text="", font=12, width=25)
    aname.grid(row=2, column=1, pady=10, padx=5, sticky="w", ipady=8)
    l4 = tk.Label(newWindow, text="Lead Actress Name: ", fg="black", bg="#e5edf1", font=("Garamond",15,"bold")).grid(row=3, column=0, pady=20, padx=25)
    aname2 = tk.Entry(text="", font=12, width=25)
    aname2.grid(row=3, column=1, pady=10, padx=5, sticky="w", ipady=8)
    l5 = tk.Label(newWindow, text="Year Of Release: ", fg="black", bg="#e5edf1", font=("Garamond",15,"bold")).grid(row=4, column=0, pady=20, padx=25, sticky="w")
    year = tk.Entry(text="", font=12, width=25)
    year.grid(row=4, column=1, pady=10, padx=5, sticky="w", ipady=8)
    l6 = tk.Label(newWindow, text="Director: ", fg="black", bg="#e5edf1", font=("Garamond",15,"bold")).grid(row=5, column=0, pady=20, padx=25, sticky="w")
    dirc = tk.Entry(text="", font=12, width=25)
    dirc.grid(row=5, column=1, pady=10, padx=5, sticky="w", ipady=8)
    b2 = tk.Button(newWindow, width=10, bg="#add8e6", fg="#0a0a0a", text="Submit", font=("Franklin Gothic",10,"bold"), command=dat).grid(row=6, column=1, pady=15, padx=10)
    

    newWindow.mainloop()

def viewlist():
    root.destroy()
    global newWindow2
    newWindow2 = tk.Tk()
    newWindow2.title("Movie List")
    newWindow2.geometry("850x600")
    newWindow2.resizable(0, 0)
    newWindow2.configure(background="#e5edf1")
    
    b3 = tk.Button(newWindow2, width=10, bg="#add8e6", fg="#0a0a0a", text="Back", font=("Franklin Gothic",12,"bold"), command=back1).grid(row=0, column=0, pady=15, padx=10, sticky="w")
    l6 = tk.Label(newWindow2, text="Movie Name", fg="black", bg="#e5edf1", font=("Garamond",12,"bold")).grid(row=1, column=0, pady=15, padx=20)
    l1 = tk.Label(newWindow2, text="Lead Actor Name", fg="black", bg="#e5edf1", font=("Garamond",12,"bold")).grid(row=1, column=1, pady=15, padx=20)
    l2 = tk.Label(newWindow2, text="Lead Actress Name", fg="black", bg="#e5edf1", font=("Garamond",12,"bold")).grid(row=1, column=2, pady=15, padx=20)
    l3 = tk.Label(newWindow2, text="Year Of Release", fg="black", bg="#e5edf1", font=("Garamond",12,"bold")).grid(row=1, column=3, pady=15, padx=20)
    l4 = tk.Label(newWindow2, text="Director", fg="black", bg="#e5edf1", font=("Garamond",12,"bold")).grid(row=1, column=4, pady=15, padx=20)
    conn = sqlite3.connect(r'C:\Users\GANESH KUMAR M A\Desktop\Movie Bucket List\movies.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM MOVIES")
    rows = cur.fetchall()
    k=0
    i=int()
    j=2
    
    for i in rows:
        l7 = tk.Label(newWindow2, text=i[0], fg="black", bg="#e5edf1", font=("Garamond",10,"bold")).grid(row=j, column=0, pady=12, padx=20)
        l8 = tk.Label(newWindow2, text=i[1], fg="black", bg="#e5edf1", font=("Garamond",10,"bold")).grid(row=j, column=1, pady=12, padx=20)
        l9 = tk.Label(newWindow2, text=i[2], fg="black", bg="#e5edf1", font=("Garamond",10,"bold")).grid(row=j, column=2, pady=12, padx=20)
        l10 = tk.Label(newWindow2, text=i[3], fg="black", bg="#e5edf1", font=("Garamond",10,"bold")).grid(row=j, column=3, pady=12, padx=20)
        l11 = tk.Label(newWindow2, text=i[4], fg="black", bg="#e5edf1", font=("Garamond",10,"bold")).grid(row=j, column=4, pady=12, padx=20)
        
        j=j+1              

    newWindow2.mainloop()

    

if __name__=="__main__":
    main()