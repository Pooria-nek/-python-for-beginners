from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget for displaying result
        self.result = Entry(master, width=20, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create buttons for digits
        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        self.buttons = []
        for i in range(10):
            button = Button(master, text=digits[i], width=5, height=2, 
                            font=('Arial', 12),
                            command=lambda x=digits[i]: self.button_click(x))
            button.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
            self.buttons.append(button)

        # create buttons for operators
        operators = ['+', '-', '*', '/', '=', 'C']
        self.op_buttons = []
        for i in range(6):
            op_button = Button(master, text=operators[i], width=5, height=2, 
                               font=('Arial', 12), 
                               command=lambda x=operators[i]: self.op_button_click(x))
            op_button.grid(row=i+1, column=3, padx=5, pady=5)
            self.op_buttons.append(op_button)

        # initialize variables
        self.first_num = 0
        self.operator = ''
        self.is_new_num = True

    def button_click(self, digit):
        if self.is_new_num:
            self.result.delete(0, END)
            self.is_new_num = False
        self.result.insert(END, digit)

    def op_button_click(self, operator):
        if self.operator == '':
            self.first_num = float(self.result.get())
            self.operator = operator
            self.is_new_num = True
        elif operator == 'C':
            self.result.delete(0, END)
            self.first_num = 0
            self.operator = ''
            self.is_new_num = True
        elif operator == '=':
            second_num = float(self.result.get())
            if self.operator == '+':
                result = self.first_num + second_num
            elif self.operator == '-':
                result = self.first_num - second_num
            elif self.operator == '*':
                result = self.first_num * second_num
            elif self.operator == '/':
                result = self.first_num / second_num
            self.result.delete(0, END)
            self.result.insert(END, result)
            self.first_num = 0
            self.operator = ''
            self.is_new_num = True
        else:
            self.first_num = float(self.result.get())
            self.operator = operator
            self.is_new_num = True

root = Tk()
calculator = Calculator(root)
root.mainloop()
