import Application
import tkinter as Tk

def main():
   root = Tk.Tk()
   app = Application.Application(master=root)
   app.mainloop()

if __name__ == "__main__":
   main()