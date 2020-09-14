
from tkinter import*
import sys

root = Tk()
root.title("SNR CALCULATOR")

icon = PhotoImage(file="CALCULATOR.png")
root.tk.call('wm','iconphoto',root._w,icon)

def quit():
    sys.exit()

def snr_calculator(source, side):
    storing_snr_objects = Frame (source, borderwidth=4, bd=4, bg="goldenrod3")
    storing_snr_objects.pack(side=side, expand=YES, fill=BOTH)
    return storing_snr_objects
def snr_equal(source, side, text, command=None,activebackground = "blue"):
    storing_snr_objects = Button(source, bg="goldenrod3", fg="gray5", text=text, command=command, activebackground = "blue")
    storing_snr_objects.pack(side=side, expand=YES, fill=BOTH)
    return storing_snr_objects
class snr(Frame):
    def __init__(self):
        Frame. __init__(self)
        self.option_add('*Font', 'sens-serif 18 bold', )
        self.pack(expand=YES, fill=BOTH)


        show_snr_value = StringVar()
        Entry(self, relief=RIDGE,
                textvariable=show_snr_value,justify='right',bd=26,fg="black",bg="goldenrod3").pack(side=TOP, expand=YES,
                        fill=BOTH)
        for Clearing_snr_value in(["CLEAR"],):
            erasing_snr_value = snr_calculator(self, TOP)
            for adding_snr_chars in Clearing_snr_value:
                snr_equal(erasing_snr_value, LEFT, adding_snr_chars,
                       lambda storing_snr_objects=show_snr_value, q=adding_snr_chars: storing_snr_objects.set(''))
        for Snr_Button_Values in ("789/", "456*", "123-", "0.+"):
            Snr_Functioalizing_Numbers = snr_calculator(self, TOP)
            for snr_char_values in Snr_Button_Values:
                snr_equal(Snr_Functioalizing_Numbers, LEFT, snr_char_values,
                       lambda storing_snr_objects=show_snr_value, q=snr_char_values: storing_snr_objects.set(storing_snr_objects.get() + q))
        Snr_Button_for_equal = snr_calculator(self, TOP)
        for lets_make_it in "=":
            if lets_make_it == '=':
                Button_Snr_dashing = snr_equal(Snr_Button_for_equal, LEFT, lets_make_it)
                Button_Snr_dashing.bind('<ButtonRelease-1>',
                         lambda e, s=self, storing_snr_objects=show_snr_value: s.showing_error_of_snr(storing_snr_objects), '+')
            else:
                Button_Snr_dashing = snr_equal(Snr_Button_for_equal, LEFT, lets_make_it,
                   lambda storing_snr_objects=show_snr_value, s=' %s '%lets_make_it: storing_snr_objects.set(storing_snr_objects.get()+s))
       
    def showing_error_of_snr(self, show_snr_value):
        try:
            show_snr_value.set(eval(show_snr_value.get()))
        except:
            show_snr_value.set("Fatal Error In Snr Value")
if __name__ == '__main__':

    button1 = Button(root, text = "Snr Calculator ""Quit",font=('sens-serif','20','bold'),bd=26,fg="black",bg="goldenrod3",activebackground = "blue" , command = quit).pack(side=TOP, expand=YES,
                        fill=BOTH)


    snr().mainloop()                                              

#ctrl+s save and ctrl+B to run