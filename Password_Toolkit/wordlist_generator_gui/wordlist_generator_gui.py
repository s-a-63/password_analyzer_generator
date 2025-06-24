# ---------------------------------------------------------------
# Password Wordlist Generator with GUI
#
# Author: Sahiti M
# Last Updated: June 2025
#
# 📌 Description:
# A Python-based tool to generate custom password wordlists using:
# - Leetspeak substitutions (e.g., a → @, 4)
# - Case variations (lower, UPPER, Capitalized)
# - User-defined number patterns (e.g., 123, 2001, 007)
#
# ✨ Features:
# - User-friendly GUI using Tkinter
# - Light/Dark mode toggle
# - Automatically saves to 'custom_wordlist.txt'
#
# ⚙️ Customization:
# - Set max output (default = 500 entries)
#
# ✅ For ethical use only — educational, security research, or testing.
# ---------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import itertools
import platform
import subprocess
import os

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

    # Save to file
    file_path = "custom_wordlist.txt"
    try:
        with open(file_path, "w") as f:
            for word in sorted(final_set):
                f.write(word + "\n")

        # Ask if the user wants to open the file
        answer = messagebox.askyesno("Success", f"Wordlist saved as '{file_path}' with {len(final_set)} entries in your current folder.\n\nDo you want to view it now?")
        if answer:
            os_type = platform.system()
            try:
                if os_type == "Windows":
                    os.startfile(file_path)
                elif os_type == "Darwin":  # macOS
                    subprocess.call(["open", file_path])
                elif os_type == "Linux":
                    subprocess.call(["xdg-open", file_path])
                else:
                    messagebox.showinfo("Unknown OS", f"Please open '{file_path}' manually.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the file:\n{e}")

    except Exception as e:
        messagebox.showerror("Error", f"Could not save the file:\n{e}")


# ---------- GUI Design with Theme Toggle ----------

def apply_theme(theme):
    # Color themes
    if theme == "light":
        root.configure(bg="#f2f2f2")
        label_fg = "#333"
        entry_bg = "#ffffff"
        entry_fg = "#000000"
        btn_bg = "#4CAF50"
        btn_fg = "#ffffff"
        footer_fg = "#888"
        toggle_btn.config(text="☾  Dark Mode")
    else:
        root.configure(bg="#1e1e1e")
        label_fg = "#f0f0f0"
        entry_bg = "#2e2e2e"
        entry_fg = "#ffffff"
        btn_bg = "#2196F3"
        btn_fg = "#ffffff"
        footer_fg = "#999"
        toggle_btn.config(text="☀  Light Mode")

    # Apply to widgets
    for widget in root.winfo_children():
        cls = widget.__class__.__name__
        if cls == "Label":
            widget.configure(bg=root['bg'], fg=label_fg)
        elif cls == "Entry":
            widget.configure(bg=entry_bg, fg=entry_fg, insertbackground=entry_fg)
        elif cls == "Button":
            if widget != toggle_btn: 
                widget.configure(bg=btn_bg, fg=btn_fg)

    footer_label.configure(fg=footer_fg, bg=root['bg'])

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme(current_theme)

# Initialize window
root = tk.Tk()
root.title("Password Wordlist Generator")
root.geometry("520x460")
current_theme = "light"

title_font = ("Segoe UI", 14, "bold")
label_font = ("Segoe UI", 10)
entry_font = ("Segoe UI", 10)

tk.Label(root, text="🔐 Password Wordlist Generator", font=title_font).pack(pady=(15, 10))

tk.Label(root, text="Enter common words (comma-separated):", font=label_font).pack()
words_entry = tk.Entry(root, width=60, font=entry_font)
words_entry.pack(pady=5)

tk.Label(root, text="Enter number patterns (birth years, etc., comma-separated):", font=label_font).pack()
numbers_entry = tk.Entry(root, width=60, font=entry_font)
numbers_entry.pack(pady=5)

tk.Label(root, text="Max combinations to generate:", font=label_font).pack()
limit_entry = tk.Entry(root, width=20, font=entry_font)
limit_entry.insert(0, "500")
limit_entry.pack(pady=5)

generate_btn = tk.Button(
    root,
    text="Generate Wordlist",
    font=("Segoe UI", 10, "bold"),
    padx=10,
    pady=5,
    command=generate_wordlist_gui
)
generate_btn.pack(pady=15)

# Dark Mode Toggle Button
toggle_btn = tk.Button(root, text="🌙 Dark Mode", font=("Segoe UI", 9), command=toggle_theme, width=15)
toggle_btn.pack()

footer_label = tk.Label(root, text="© 2025 Sahiti M | For ethical use only", font=("Segoe UI", 8))
footer_label.pack(side="bottom", pady=10)

# Apply initial theme
apply_theme(current_theme)

root.mainloop()
