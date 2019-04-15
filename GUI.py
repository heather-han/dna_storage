
# This code is run under python 3

import tkinter as tk
import tkinter.filedialog as tkf


def gui():
    tittle = 'DNA storage'
    root = tk.Tk()
    root.title(tittle)
    lb = tk.Label(root, text='')
    lb.grid(row=1, columnspan=3)
    lb2 = tk.Label(root, text='This is the GUI for encode zip or tar file to DNA encoding and convert it back.')
    lb2.grid(row=2, columnspan=3)
    lb3 = tk.Label(root, text='')
    lb3.grid(row=3, columnspan=3)
    def encode():
        folder_path = tkf.askdirectory()
        try:
            # determine if you choose a file or not
            do_nothing = folder_path[0]
        # ###########################################
        #                                           #
        #                                           #
        #   PUT encode main function here           #
        #                                           #
        # ###########################################
        except:
            lb3.config(text='Please choose a file folder')
    def decode():
        folder_path = tkf.askdirectory()
        try:
            # determine if you choose a file or not
            do_nothing = folder_path[0]
        # ###########################################
        #                                           #
        #                                           #
        #   PUT decode main function here           #
        #                                           #
        # ###########################################
        except:
            lb3.config(text='Please choose a file folder')
    bt1 = tk.Button(root, text='decode', width=10, command=decode)
    bt2 = tk.Button(root, text='encode', width=10, command=encode)
    bt3 = tk.Button(root, text='exit', width=10, command=root.quit)
    bt1.grid(row=4, column=2, sticky='E', padx=10, pady=5)
    bt2.grid(row=4, column=0, sticky='W', padx=10, pady=5)
    bt3.grid(row=4, column=1, sticky='W', padx=10, pady=5)

    root.mainloop()


if __name__ =='__main__':
    gui()