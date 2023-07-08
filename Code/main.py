from customtkinter import *
from tkinter.messagebox import showerror, showinfo
from typing import Union

main_font = ("Segoe UI", 20)
root = CTk()
root.resizable(False, False)
root.geometry("540x400")
root.title("BMI")


def set_ru_lang() -> None:
    global level0, level1, level2, level3, level4, level5, level6, enter_data_error_title, separator_error_text, \
        length_error_text, value_error_text, less_than_zero_error_text, mass_lbl_txt, height_lbl_txt, \
        calculate_btn_txt, result_lbl_txt, bmi_prog_label_txt

    showinfo(title="Смена языка", message="Для полной смены языка выполните вычисление повторно.")

    level0 = "Выраженный дефицит массы тела"
    level1 = "Недостаточная (дефицит) масса тела"
    level2 = "Норма"
    level3 = "Избыточная масса тела (предожирение)"
    level4 = "Ожирение 1 степени"
    level5 = "Ожирение 2 степени"
    level6 = "Ожирение 3 степени"

    enter_data_error_title = "Входные данные"
    separator_error_text = "В качестве разделителя используется не запятая, а точка."
    length_error_text = "Длина вводимых чисел должна быть от 1 до 5 включительно."
    value_error_text = "Введены не числа."
    less_than_zero_error_text = "Рост или масса должны быть положительными."

    bmi_prog_label_txt = "ИМТ калькулятор"
    mass_lbl_txt = "Введите массу в кг"
    height_lbl_txt = "Введите рост в см"
    calculate_btn_txt = "Рассчитать ИМТ"
    result_lbl_txt = "Ваш ИМТ"

    bmi_lbl.configure(text=bmi_prog_label_txt)
    mass_lbl.configure(text=mass_lbl_txt)
    height_lbl.configure(text=height_lbl_txt)
    calculate_bmi_btn.configure(text=calculate_btn_txt)
    result_lbl.configure(text=result_lbl_txt)


def set_en_lang() -> None:
    global level0, level1, level2, level3, level4, level5, level6, enter_data_error_title, separator_error_text, \
        length_error_text, value_error_text, less_than_zero_error_text, mass_lbl_txt, height_lbl_txt, \
        calculate_btn_txt, result_lbl_txt, bmi_prog_label_txt

    showinfo(title="Change of language", message="To switch the language completely, calculate BMI again.")

    level0 = "Underweight (Severe thinness)"
    level1 = "Underweight (Mild thinness)"
    level2 = "Normal range"
    level3 = "Overweight (Pre-obese)"
    level4 = "Obese (Class I)"
    level5 = "Obese (Class II)"
    level6 = "Obese (Class III)"

    enter_data_error_title = "Input data"
    separator_error_text = "Use point instead of comma as a decimal separator."
    length_error_text = "Lengths of numbers must be in range from 0 to 5 inclusive."
    value_error_text = "You've input not numbers"
    less_than_zero_error_text = "Height and mass must be positive"

    bmi_prog_label_txt = "BMI calculator"
    mass_lbl_txt = "Input your mass in kg"
    height_lbl_txt = "Input your height in cm"
    calculate_btn_txt = "Calculate BMI"
    result_lbl_txt = "Your BMI"

    bmi_lbl.configure(text=bmi_prog_label_txt)
    mass_lbl.configure(text=mass_lbl_txt)
    height_lbl.configure(text=height_lbl_txt)
    calculate_bmi_btn.configure(text=calculate_btn_txt)
    result_lbl.configure(text=result_lbl_txt)


def evaluate_bmi(bmi: Union[int, float]) -> str:
    global level0, level1, level2, level3, level4, level5, level6
    if not level0:
        level0 = "Выраженный дефицит массы тела"
        level1 = "Недостаточная (дефицит) масса тела"
        level2 = "Норма"
        level3 = "Избыточная масса тела (предожирение)"
        level4 = "Ожирение 1 степени"
        level5 = "Ожирение 2 степени"
        level6 = "Ожирение 3 степени"

    if bmi <= 16:
        return level0
    elif 16 < bmi <= 18.5:
        return level1
    elif 18.5 < bmi <= 25:
        return level2
    elif 25 < bmi <= 30:
        return level3
    elif 30 < bmi <= 35:
        return level4
    elif 35 < bmi < 40:
        return level5
    elif bmi >= 40:
        return level6
    else:
        raise Exception


def calculate_bmi() -> None:
    global enter_data_error_title, separator_error_text, mass_entry, height_entry, \
        length_error_text, value_error_text, less_than_zero_error_text, bmi_num, bmi_meaning

    bmi_num.configure(state="normal")
    bmi_meaning.configure(state="normal")

    enter_data_error_title = "Входные данные"
    separator_error_text = "В качестве разделителя используется не запятая, а точка."
    length_error_text = "Длина вводимых чисел должна быть от 1 до 5 включительно."
    value_error_text = "Введены не числа."
    less_than_zero_error_text = "Рост или масса должны быть положительными."

    if len(mass_entry.get()) < 1 or len(mass_entry.get()) > 5:
        showerror(title=enter_data_error_title, message=length_error_text)
        bmi_num.configure(state="readonly")
        bmi_meaning.configure(state="readonly")
        return
    if "," in mass_entry.get() + height_entry.get():
        showerror(title=enter_data_error_title, message=separator_error_text)
        bmi_num.configure(state="readonly")
        bmi_meaning.configure(state="readonly")
        return
    try:
        float(mass_entry.get())
        float(height_entry.get())
    except ValueError:
        showerror(title=enter_data_error_title, message=value_error_text)
        bmi_num.configure(state="readonly")
        bmi_meaning.configure(state="readonly")
        return
    if float(mass_entry.get()) <= 0 or float(height_entry.get()) <= 0:
        showerror(title=enter_data_error_title, message=less_than_zero_error_text)
        bmi_num.configure(state="readonly")
        bmi_meaning.configure(state="readonly")
        return

    # bmi = m(kg) / h(m) ^ 2
    mass_kg = round(float(mass_entry.get()), 4)
    height_m = round(round(float(height_entry.get()), 4) / 100, 4)
    bmi = round(mass_kg / height_m ** 2, 2)
    meaning = evaluate_bmi(bmi=bmi)

    bmi_num.delete(0, END)
    bmi_num.insert(END, bmi)
    bmi_meaning.delete(0, END)
    bmi_meaning.insert(0, meaning)

    bmi_num.configure(state="readonly")
    bmi_meaning.configure(state="readonly")


bmi_prog_label_txt = "ИМТ калькулятор"
mass_lbl_txt = "Введите массу в кг"
height_lbl_txt = "Введите рост в см"
calculate_btn_txt = "Рассчитать ИМТ"
result_lbl_txt = "Ваш ИМТ"

bmi_lbl = CTkLabel(master=root, font=("Segoe Ui", 35), text=bmi_prog_label_txt)

change_lang_to_ru = CTkButton(master=root, text="Русский", command=set_ru_lang)
change_lang_to_en = CTkButton(master=root, text="English", command=set_en_lang)

mass_lbl = CTkLabel(master=root, text=mass_lbl_txt, font=main_font)
height_lbl = CTkLabel(master=root, text=height_lbl_txt, font=main_font)
result_lbl = CTkLabel(master=root, text=result_lbl_txt, font=main_font)

mass_entry = CTkEntry(master=root, width=80, font=main_font)
height_entry = CTkEntry(master=root, width=80, font=main_font)

calculate_bmi_btn = CTkButton(master=root, text=calculate_btn_txt, font=main_font, command=calculate_bmi, width=320)
bmi_num = CTkEntry(master=root, width=75, font=main_font)
bmi_meaning = CTkEntry(master=root, width=500, font=main_font)

bmi_lbl.place(x=20, y=20)
change_lang_to_ru.place(x=369, y=20)
change_lang_to_en.place(x=369, y=70)

mass_lbl.place(x=20, y=100)
mass_entry.place(x=260, y=100)
height_lbl.place(x=20, y=150)
height_entry.place(x=260, y=150)

calculate_bmi_btn.place(x=20, y=200)
result_lbl.place(x=20, y=300)
bmi_num.place(x=120, y=300)
bmi_meaning.place(x=20, y=350)

root.mainloop()
