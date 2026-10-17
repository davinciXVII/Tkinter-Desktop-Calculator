import tkinter

def add():
    nums = getter()
    if nums:
        answer(nums[0] + nums[1])

def sub():
    nums = getter()
    if nums:
        answer(nums[0] - nums[1])

def mult():
    nums = getter()
    if nums:
        answer(nums[0] * nums[1])

def div():
    nums = getter()
    if nums:
        if nums[1] == 0:
            answer("Zero Div Error")
        else:
            answer(nums[0] / nums[1])

def root():
    nums = getter()
    if nums:
        try:
            
            result = nums[0] ** (1 / nums[1])
            answer(result)
        except ZeroDivisionError:
            answer("Zero Div Error")

def getter():
    
    try:
        num1 = text_num1.get()
        num2 = text_num2.get()
        return float(num1), float(num2)  
    except ValueError:
        answer("Input Error")
        return None

def answer(result):
    text_answer.delete(0, "end")
    text_answer.insert(0, result)


window = tkinter.Tk()
window.title("GUI Calculator")
window.geometry("400x400")
window.configure(bg="white")


button_add = tkinter.Button(window, text="+", command=add, bg="white", fg="black", height=5, width=4)
button_sub = tkinter.Button(window, text="-", command=sub, bg="white", fg="black", height=5, width=4)
button_mult = tkinter.Button(window, text="*", command=mult, bg="white", fg="black", height=5, width=4)
button_div = tkinter.Button(window, text="/", command=div, bg="white", fg="black", height=5, width=4)
button_root = tkinter.Button(window, text="sqrt", command=root, bg="white", fg="black", height=5, width=4)


button_add.place(x=100, y=100)
button_sub.place(x=150, y=100)
button_mult.place(x=200, y=100)
button_div.place(x=250, y=100)
button_root.place(x=300, y=100)
                           

text_num1 = tkinter.Entry(window, bg="white", fg="black")
text_num2 = tkinter.Entry(window, bg="white", fg="black")
text_answer = tkinter.Entry(window, bg="white", fg="black")

text_num1.place(x=100, y=40)
text_num2.place(x=100, y=70)
text_answer.place(x=100, y=200)

window.mainloop()
