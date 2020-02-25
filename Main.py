import Class.IHM.MainApp as App
import tkinter as Tk

def main():
   root = Tk.Tk()
   app = App.Application(master=root)
   app.mainloop()

if __name__ == "__main__":
   main()