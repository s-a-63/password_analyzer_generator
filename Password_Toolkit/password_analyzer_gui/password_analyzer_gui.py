# ---------------------------------------------------------------
# 🔐 Password Strength Analyzer GUI
#
# Author: Sahiti M
# Last Updated: June 2025
#
# 📌 Description:
# A user-friendly Python application to analyze the strength of passwords
# using the zxcvbn algorithm. It evaluates the password score (0–4) and 
# provides feedback on weaknesses or suggestions for improvement.
#
# ✨ Features:
# - GUI built using Tkinter
# - Password input field (masked)
# - Show/Hide password toggle
# - Strength score display (0 = weak, 4 = strong)
# - Feedback with suggestions or warnings
#
# ⚙️ How It Works:
# The tool uses the zxcvbn library, which tests passwords against dictionary words, common patterns, substitutions, and brute-force resistance. The result includes a score and human-readable feedback.
#
# For educational or ethical use only.
# ---------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

# ---------- Password Analyzer ----------
def check_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Empty Input", "Please enter a password to analyze.")
        return

    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']

    score_label.config(text=f"Score (0–4): {score}", fg=score_colors[score])

    warning = feedback.get('warning', '')
    suggestions = "\n".join(feedback.get('suggestions', []))
    feedback_text = f"{warning}\n{suggestions}".strip()
    feedback_label.config(text=feedback_text if feedback_text else "✅ Strong password!")

# ---------- GUI Layout ----------
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("460x350")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

title_font = ("Segoe UI", 14, "bold")
label_font = ("Segoe UI", 10)
entry_font = ("Segoe UI", 10)

# Title
tk.Label(root, text="🔐 Password Strength Analyzer", font=title_font, bg="#f2f2f2").pack(pady=10)

# Password Entry
tk.Label(root, text="Enter password:", font=label_font, bg="#f2f2f2").pack()
entry = tk.Entry(root, width=30, show="*", font=entry_font, bg="#ffffff")
entry.pack(pady=5)

# Show/Hide Password Toggle
show_password = tk.BooleanVar()
show_password.set(False)

def toggle_password():
    entry.config(show="" if show_password.get() else "*")

toggle_btn = tk.Checkbutton(
    root,
    text="👁 Show Password ",
    variable=show_password,
    command=toggle_password,
    font=("Segoe UI", 10),
    bg="#f2f2f2",
    padx=10,
    pady=5
)

toggle_btn.pack()

# Analyze Button
tk.Button(
    root,
    text="Check Strength",
    font=label_font,
    bg="#4CAF50",
    fg="black",
    command=check_strength
).pack(pady=10)

# Score Display
score_colors = ["#e53935", "#fb8c00", "#fdd835", "#43a047", "#2e7d32"]
score_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#f2f2f2")
score_label.pack(pady=5)

# Feedback Display
feedback_label = tk.Label(root, text="", font=("Segoe UI", 9), wraplength=400, justify="center", bg="#f2f2f2")
feedback_label.pack(pady=10)

# Footer
tk.Label(root, text="© 2025 Sahiti M | zxcvbn powered", font=("Segoe UI", 8), bg="#f2f2f2", fg="#888").pack(side="bottom", pady=10)

# Start the App
root.mainloop()
