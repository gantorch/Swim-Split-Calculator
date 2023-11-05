import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

window = tk.CTk()
window.title(" Swim Splits Calculator ")
window.geometry("700x500")


def meters():
    print("meters pressed")

def yards():
    print("yards pressed")

button = tk.CTkButton(window, text="Yards", command=yards)
# button.place(relx=10.5, rely=10.5, anchor=tk.CENTER)

# button = tk.CTkButton(master=window, text="Meters", command=meters)
# button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

window.mainloop()