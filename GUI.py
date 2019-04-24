
# This code is run under python 3

import tkinter as tk
import tkinter.filedialog as tkf
import encode_i
import decode_i
import time


def gui():
    tittle = 'DNA storage'
    root = tk.Tk()
    root.title(tittle)
    lb = tk.Label(root, text='')
    lb.grid(row=0, columnspan=3)
    lb2 = tk.Label(root, text='This is the GUI for encoding file to DNA and convert it back.')
    lb2.grid(row=1, columnspan=3)
    lb3 = tk.Label(root, text='')
    lb3.grid(row=2, columnspan=3)
    lb4 = tk.Label(text='Please enter the format of the file you choose: ')
    lb4.grid(row=3, column=0)
    lb5 = tk.Label(root, text='')
    lb5.grid(row=5, columnspan=3)
    lb6 = tk.Label(text='Please specific error rate: ')
    lb6.grid(row=4, column=0)
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e2.insert(tk.END, '0.0001')
    e2.grid(row=4, column=1)
    e1.grid(row=3, column=1)
    def Encode():
        folder_path = tkf.askdirectory()
        entry = e1.get()
        try:
            # determine if you choose a file or not
            do_nothing = folder_path[0]
            lb5.config(text='encoding ...')
            lb5.update()
            encode_i.main(folder_path, entry)
            lb5.config(text='Done!')
            lb5.update()

        except:
            lb3.config(text='Please choose a file folder')
    def Decode():
        folder_path = tkf.askdirectory()
        error_rate = e2.get()
        try:
            error_rate = float(error_rate)
        except:
            error_rate = 0.0001
        try:
            # determine if you choose a file or not
            do_nothing = folder_path[0]
            lb5.config(text='decoding ....')
            lb5.update()
            decode_i.main(folder_path, error_rate=error_rate)
            e2.delete(0, tk.END)
            e2.insert(tk.END, '0.0001')
            lb5.config(text='Done!')
            lb5.update()
        except:
            lb3.config(text='Please choose a file folder')
    bt1 = tk.Button(root, text='decode', width=10, command=Decode)
    bt2 = tk.Button(root, text='encode', width=10, command=Encode)
    bt3 = tk.Button(root, text='exit', width=10, command=root.quit)
    bt1.grid(row=6, column=2, sticky='E', padx=10, pady=5)
    bt2.grid(row=6, column=0, sticky='W', padx=10, pady=5)
    bt3.grid(row=6, column=1, sticky='W', padx=10, pady=5)

    root.mainloop()


if __name__ =='__main__':
    gui()