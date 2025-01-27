from tkinter import *
import math

class Calculator:
    """A simple calculator with enhanced functionality."""

    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="#f0f0f0")

        self.display_var = StringVar()
        self.display_var.set("0")

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        display_frame = Frame(self.root, width=340, height=50, bg="#f0f0f0")
        display_frame.pack()

        Label(display_frame, textvariable=self.display_var, anchor=E,
              bg="#f0f0f0", fg="black", font=("Arial", 48)).pack(expand=True, fill='both')

    def _create_buttons(self):
        buttons_frame = Frame(self.root, width=340, height=340, bg="lightblue")
        buttons_frame.pack()

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
        ]

        row = 0
        for row_buttons in buttons:
            col = 0
            for button_text in row_buttons:
                Button(buttons_frame, text=button_text, fg='black', bg='pink', font=("Arial", 22),
                       width=5, height=2, command=lambda x=button_text: self._on_button_press(x)).grid(row=row, column=col, sticky=NSEW)
                col += 1
            row += 1

        special_buttons = [
            ('√', 'lightgreen', lambda: self._on_button_press("sqrt(")),
            ('^', 'lightgreen', lambda: self._on_button_press("**")),
            ('%', 'lightgreen', lambda: self._on_button_press("/100.")),
            ('!', 'lightgreen', self._factorial),
        ]

        for i, (text, color, command) in enumerate(special_buttons):
            Button(buttons_frame, text=text, fg='black', bg=color, font=("Arial", 22),
                   width=5, height=2, command=command).grid(row=i, column=4, sticky=NSEW)

        Button(buttons_frame, text="C", fg='black', bg='red', font=("Arial", 22),
               width=11, height=2, command=self._clear).grid(row=4, column=0, columnspan=2, sticky=NSEW)

    def _on_button_press(self, button_text):
        current_text = self.display_var.get()
        if button_text == "=":
            try:
                result = eval(current_text)
                self.display_var.set(str(result))
            except Exception:
                self.display_var.set("Error")
        elif button_text == "C":
            self._clear()
        else:
            self.display_var.set(current_text + button_text)

    def _clear(self):
        self.display_var.set("0")

    def _factorial(self):
        try:
            number = int(self.display_var.get())
            if number < 0:
                self.display_var.set("Error")
            else:
                self.display_var.set(str(math.factorial(number)))
        except ValueError:
            self.display_var.set("Error")

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()