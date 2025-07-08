import customtkinter as ctk
import random

# ---------- App Setup ----------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🎯 Guess the Number - Premium Edition")
app.geometry("500x400")
app.resizable(False, False)

# ---------- Game Variables ----------
number = random.randint(1, 10)
attempts = 0
max_attempts = 3

# ---------- Game Logic ----------
def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess == number:
            result_label.configure(
                text=f"✅ Hurray! You guessed it right! It was {number}.",
                text_color="green"
            )
            guess_button.configure(state="disabled")
        elif attempts < max_attempts:
            hint = "🔼 Too high!" if guess > number else "🔽 Too low!"
            result_label.configure(
                text=f"❌ Wrong guess. {hint} Attempts left: {max_attempts - attempts}",
                text_color="orange"
            )
        else:
            result_label.configure(
                text=f"❌ Game Over! The number was {number}.",
                text_color="red"
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

# ---------- UI Elements ----------
title_label = ctk.CTkLabel(
    app, text="🎯 Guess the Number", 
    font=("Segoe UI", 26, "bold"), 
    justify="center"
)
title_label.pack(pady=20)

entry = ctk.CTkEntry(
    app, placeholder_text="Enter a number (1–10)", 
    font=("Segoe UI", 18), 
    width=200, 
    justify="center"
)
entry.pack(pady=10)

guess_button = ctk.CTkButton(
    app, text="Guess 🔍", 
    font=("Segoe UI", 18, "bold"), 
    command=check_guess, 
    height=45, corner_radius=25
)
guess_button.pack(pady=10)

reset_button = ctk.CTkButton(
    app, text="🔄 Play Again", 
    font=("Segoe UI", 14), 
    command=reset_game, 
    height=35, fg_color="#777777"
)
reset_button.pack(pady=5)

result_label = ctk.CTkLabel(
    app, text="", 
    font=("Segoe UI", 16), 
    wraplength=400,
    justify="center"
)
result_label.pack(pady=20)

footer = ctk.CTkLabel(
    app, text="🔎 Powered by Y7X 💗", 
    font=("Segoe UI", 12, "italic"),
    justify="center"
)
footer.pack(side="bottom", pady=10)

# ---------- Run App ----------
app.mainloop()