# ---------------------------------------------------------------
# 🔐 Password Toolkit: Strength Analyzer + Wordlist Generator
#
# Author: Sahiti M
# Last Updated: June 2025
#
# 📌 Description:
# This Python GUI application combines two tools:
# 1. Password Strength Analyzer using zxcvbn
# 2. Custom Wordlist Generator with leetspeak + year patterns
#
# ✨ Features:
# - GUI with tabbed layout (Tkinter)
# - Show/Hide password toggle
# - Dark Mode / Light Mode switch
# - Exports wordlist to .txt for cracking tools
# - Clear buttons and generation status indicator
#
# ✅ For ethical use only — education, testing, awareness.
# ---------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, ttk
from zxcvbn import zxcvbn
import itertools
import os
import platform
import subprocess

# ---------- Wordlist Logic ----------
leet_dict = {
    'a': ['a', '4', '@'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
    'l': ['l', '1']
}

def generate_leetspeak_combinations(word, max_variants):
    char_options = []
    for char in word.lower():
        if char in leet_dict:
            char_options.append(leet_dict[char])
        else:
            char_options.append([char])

    variants = set()
    for i, combo in enumerate(itertools.product(*char_options)):
        if i >= max_variants:
            break
        variants.add(''.join(combo))
    return variants

def add_number_variations(word_variants, number_patterns, max_total):
    result = set()
    for word in word_variants:
        if len(result) >= max_total:
            break
        cases = [word, word.upper(), word.capitalize()]
        for variant in cases:
            result.add(variant)
            for number in number_patterns:
                if len(result) >= max_total:
                    break
                result.add(variant + number)
                result.add(number + variant)
    return result

def generate_wordlist_gui():
    status_label.config(text="Generating wordlist...", fg="blue")
    root.update_idletasks()

    base_words = words_entry.get().split(',')
    number_patterns = [num.strip() for num in numbers_entry.get().split(',') if num.strip().isdigit()]
    try:
        max_total = int(limit_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the limit.")
        return

    final_set = set()
    for word in base_words:
        word = word.strip()
        leet_variants = generate_leetspeak_combinations(word, 50)
        wordlist = add_number_variations(leet_variants, number_patterns, max_total - len(final_set))
        final_set.update(wordlist)
        if len(final_set) >= max_total:
            break

    file_path = "custom_wordlist.txt"
    try:
        with open(file_path, "w") as f:
            for word in sorted(final_set):
                f.write(word + "\n")

        status_label.config(text=f"✅ Wordlist generated with {len(final_set)} entries.", fg="green")

        answer = messagebox.askyesno("Success", f"Wordlist saved as '{file_path}' with {len(final_set)} entries in your current folder.\n\nDo you want to view it now?")
        if answer:
            os_type = platform.system()
            try:
                if os_type == "Windows":
                    os.startfile(file_path)
                elif os_type == "Darwin":
                    subprocess.call(["open", file_path])
                elif os_type == "Linux":
                    subprocess.call(["xdg-open", file_path])
                else:
                    messagebox.showinfo("Unknown OS", f"Please open '{file_path}' manually.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the file:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save the file:\n{e}")

def clear_wordlist_output():
    status_label.config(text="")
    words_entry.delete(0, tk.END)
    numbers_entry.delete(0, tk.END)
    limit_entry.delete(0, tk.END)
    limit_entry.insert(0, "500")

def clear_analyzer_output():
    password_entry.delete(0, tk.END)
    score_label.config(text="")
    feedback_label.config(text="")

# ---------- Password Analyzer Logic ----------
def check_strength():
    password = password_entry.get()
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

def toggle_password():
    password_entry.config(show="" if show_password.get() else "*")

# ---------- Theme Toggle ----------
def apply_theme(theme):
    bg_light = "#f2f2f2"
    bg_dark = "#1e1e1e"
    entry_light = "#ffffff"
    entry_dark = "#2e2e2e"
    fg_light = "#000000"
    fg_dark = "#ffffff"

    root.configure(bg=bg_light if theme == "light" else bg_dark)

    for frame in [analyzer_tab, generator_tab]:
        frame.configure(bg=bg_light if theme == "light" else bg_dark)
        for widget in frame.winfo_children():
            cls = widget.__class__.__name__
            if cls == "Label":
                widget.configure(bg=frame['bg'], fg=fg_light if theme == "light" else fg_dark)
            elif cls == "Entry":
                widget.configure(bg=entry_light if theme == "light" else entry_dark,
                                 fg=fg_light if theme == "light" else fg_dark,
                                 insertbackground=fg_light if theme == "light" else fg_dark)
            elif cls == "Checkbutton":
                widget.configure(bg=frame['bg'], fg=fg_light if theme == "light" else fg_dark)
            elif cls == "Button":
                if widget != toggle_btn:
                    widget.configure(bg="#4CAF50" if theme == "light" else "#2196F3", fg="white")

    toggle_btn.config(text="☾  Dark Mode" if theme == "light" else "☀  Light Mode")

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme(current_theme)

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Password Toolkit - Analyzer + Generator")
root.geometry("600x580")
current_theme = "light"

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ---------- Tab 1: Password Analyzer ----------
analyzer_tab = tk.Frame(notebook, bg="#f2f2f2")
notebook.add(analyzer_tab, text="🔐 Password Strength Analyzer")

tk.Label(analyzer_tab, text="🔐 Password Strength Analyzer", font=("Segoe UI", 14, "bold")).pack(pady=10)
tk.Label(analyzer_tab, text="Enter password:", font=("Segoe UI", 10)).pack()
password_entry = tk.Entry(analyzer_tab, width=30, show="*", font=("Segoe UI", 10), bg="#ffffff")
password_entry.pack(pady=5)

show_password = tk.BooleanVar()
show_password.set(False)

tk.Checkbutton(
    analyzer_tab,
    text="👁 Show Password",
    variable=show_password,
    command=toggle_password,
    font=("Segoe UI", 10),
    bg="#f2f2f2",
    padx=10,
    pady=5
).pack()

tk.Button(
    analyzer_tab,
    text="Check Strength",
    font=("Segoe UI", 10),
    bg="#4CAF50",
    fg="black",
    command=check_strength
).pack(pady=5)

tk.Button(
    analyzer_tab,
    text="Clear",
    font=("Segoe UI", 9),
    command=clear_analyzer_output
).pack()

score_colors = ["#e53935", "#fb8c00", "#fdd835", "#43a047", "#2e7d32"]
score_label = tk.Label(analyzer_tab, text="", font=("Segoe UI", 12, "bold"), bg="#f2f2f2")
score_label.pack(pady=5)

feedback_label = tk.Label(analyzer_tab, text="", font=("Segoe UI", 9), wraplength=500, justify="center", bg="#f2f2f2")
feedback_label.pack(pady=10)

# ---------- Tab 2: Wordlist Generator ----------
generator_tab = tk.Frame(notebook, bg="#f2f2f2")
notebook.add(generator_tab, text="🧠 Wordlist Generator")

tk.Label(generator_tab, text="🔐 Password Wordlist Generator", font=("Segoe UI", 14, "bold")).pack(pady=15)

tk.Label(generator_tab, text="Enter common words (comma-separated):", font=("Segoe UI", 10)).pack()
words_entry = tk.Entry(generator_tab, width=60, font=("Segoe UI", 10))
words_entry.pack(pady=5)

tk.Label(generator_tab, text="Enter number patterns (birth years, lucky numbers etc., comma-separated):", font=("Segoe UI", 10)).pack()
numbers_entry = tk.Entry(generator_tab, width=60, font=("Segoe UI", 10))
numbers_entry.pack(pady=5)

tk.Label(generator_tab, text="Max combinations to generate:", font=("Segoe UI", 10)).pack()
limit_entry = tk.Entry(generator_tab, width=20, font=("Segoe UI", 10))
limit_entry.insert(0, "500")
limit_entry.pack(pady=5)

tk.Button(generator_tab, text="Generate Wordlist", font=("Segoe UI", 10), bg="#4CAF50", fg="white", command=generate_wordlist_gui).pack(pady=5)

tk.Button(generator_tab, text="Clear", font=("Segoe UI", 9), command=clear_wordlist_output).pack()

status_label = tk.Label(generator_tab, text="", font=("Segoe UI", 9), fg="green", bg="#f2f2f2")
status_label.pack(pady=5)

# ---------- Theme Toggle ----------
toggle_btn = tk.Button(root, text="☾  Dark Mode", font=("Segoe UI", 9), command=toggle_theme, width=15)
toggle_btn.pack()

# ---------- Footer ----------
footer_label = tk.Label(root, text="© 2025 Sahiti M | For ethical use only", font=("Segoe UI", 8))
footer_label.pack(side="bottom", pady=5)

# Apply theme and launch
apply_theme(current_theme)
root.mainloop()
