from tkinter import *
from tkinter import messagebox as mb


def cancel_booking(event=None):
    seat = cancel_seat_entry.get().upper()
    if seat in seats and seats[seat] == "забронировано":
        seats[seat] = "свободно"
        mb.showinfo('Успех', f"Бронь места {seat} успешно отменена.")
        update_canvas()
    elif seat in seats:
        mb.showinfo('Ошибка', f"Место {seat} уже свободно.")
    else:
        mb.showinfo('Ошибка', f"Место не забронировано {seat} не существует.")
    seat_entry.delete(0, END)


def book_seat(event=None):
    seat = seat_entry.get().upper()
    if seat in seats and seats[seat] == "свободно":
        seats[seat] = "забронировано"
        mb.showinfo('Успех', f"Место {seat} успешно забронировано.")
        update_canvas()
    elif seat in seats:
        mb.showinfo('Ошибка', f"Место {seat} уже забронировано.")
    else:
        mb.showinfo('Ошибка', f"Место {seat} не существует.")
    seat_entry.delete(0, END)


def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat, fill="white")


window = Tk()
window.title('Бронирование мест')
window.geometry('400x300')

canvas = Canvas(width=400, height=80)
canvas.pack(pady=10)

seats = {f"Б{i}": "свободно" for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind('<Return>', book_seat)

Button(text='Забронировать', command=book_seat).pack(pady=10)

cancel_seat_entry = Entry()
cancel_seat_entry.pack(pady=10)
cancel_seat_entry.bind('<Return>', cancel_booking)

Button(text='Отменить бронь', command=cancel_booking).pack(pady=10)

window.mainloop()