import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("🧠 NeuroGuess")
app.geometry("460x400")
app.resizable(False, False)
app.configure(bg="#000000")

number = random.randint(1, 10)
attempts = 0
max_attempts = 3

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess == number:
            result_label.configure(
                text=f"✅ Hurray! You guessed it right! It was {number}.",
                text_color="#00ff88"
            )
            guess_button.configure(state="disabled")
        elif attempts < max_attempts:
            hint = "🔼 Too high!" if guess > number else "🔽 Too low!"
            result_label.configure(
                text=f"❌ Wrong guess. {hint} Attempts left: {max_attempts - attempts}",
                text_color="#ff9900"
            )
        else:
            result_label.configure(
                text=f"❌ Game Over! The number was {number}.",
                text_color="#ff0033"
            )
            guess_button.configure(state="disabled")
    except ValueError:
        result_label.configure(text="⚠️ Please enter a valid number!", text_color="red")

def reset_game():
    global number, attempts
    number = random.randint(1, 10)
    attempts = 0
    entry.delete(0, 'end')
    result_label.configure(text="")
    guess_button.configure(state="normal")

main_frame = ctk.CTkFrame(app, fg_color="#000000", bg_color="#000000")
main_frame.pack(fill="both", expand=True)

title_label = ctk.CTkLabel(
    main_frame, text="🧠 NeuroGuess",
    font=("Segoe UI", 24, "bold"),
    text_color="white",
    justify="center",
    bg_color="#000000"
)
title_label.pack(pady=(25, 15))

entry = ctk.CTkEntry(
    main_frame, placeholder_text="Enter a number (1–10)",
    font=("Segoe UI", 18),
    width=260,
    justify="center",
    border_color="#ff0033",
    border_width=2,
    fg_color="#000000",
    text_color="white",
    bg_color="#000000"
)
entry.pack(pady=16)

button_width = 130
button_height = 40
corner_radius = 20
button_font = ("Segoe UI", 16, "bold")

button_row = ctk.CTkFrame(main_frame, fg_color="#000000", bg_color="#000000")
button_row.pack(pady=18)

guess_button = ctk.CTkButton(
    button_row, text="Guess 🔍",
    font=button_font,
    command=check_guess,
    width=button_width,
    height=button_height,
    corner_radius=corner_radius,
    fg_color="#ff0033",
    hover_color="#cc0022",
    text_color="white",
    bg_color="#000000"
)
guess_button.pack(side="left", padx=6)

reset_button = ctk.CTkButton(
    button_row, text="🔄 Again",
    font=button_font,
    command=reset_game,
    width=button_width,
    height=button_height,
    corner_radius=corner_radius,
    fg_color="#000000",
    hover_color="#111111",
    text_color="#ff0033",
    border_color="#ff0033",
    border_width=2,
    bg_color="#000000"
)
reset_button.pack(side="left", padx=6)

result_label = ctk.CTkLabel(
    main_frame, text="",
    font=("Segoe UI", 14),
    wraplength=400,
    justify="center",
    text_color="white",
    bg_color="#000000"
)
result_label.pack(pady=12)

footer = ctk.CTkLabel(
    main_frame, text="🔎 Powered by Y7X 💗",
    font=("Segoe UI", 11, "italic"),
    justify="center",
    text_color="#ff0033",
    bg_color="#000000"
)
footer.pack(side="bottom", pady=10)

app.mainloop()