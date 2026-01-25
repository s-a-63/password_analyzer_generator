# 🔐 Password Toolkit: Strength Analyzer + Wordlist Generator

A complete Python GUI application combining:

1. **Password Strength Analyzer** — evaluates passwords using zxcvbn
2. **Custom Wordlist Generator** — creates password lists with leetspeak, case variants, and number patterns

Built with `Tkinter`, styled with Light/Dark mode, and designed for ethical use.

---

## 🚀 Features

- Graphical user interface with tabbed layout
- Password strength scoring (0 to 4)
- Feedback on password weaknesses
- Show/Hide password toggle (👁)
- Dark Mode / Light Mode switch (☾/☀)
- Clear Output button for both tabs to reset inputs/results
- Status message during wordlist generation for better feedback
- Wordlist generator supports:
  - Leetspeak substitutions (e.g., a → @, 4)
  - Case variations (lower, upper, title)
  - Custom numbers (birth years, patterns)
- Saves output to `custom_wordlist.txt`

---

## 📦 Installation


### 1. Clone the repository or download the `.py` file
```bash
git clone https://github.com/s-a-63/password_analyzer_generator.git
cd password_analyzer_generator
```

### 2. Install the required Python package:
```bash
pip install zxcvbn
```

## ▶️ Running the Toolkit
```bash
python password_toolkit_gui.py
```

---

## 📁 Project Structure

```
📁 Password_Toolkit/
├── password_toolkit_gui.py              # Combined GUI (tabs)
├── requirements.txt                     # Lists zxcvbn
├── custom_wordlist.txt                  # Output wordlist
├── README.md                            # This file
├── 📁 password_analyzer_gui/            # Standalone password analyzer
│   └── password_analyzer_gui.py
├── 📁 wordlist_generator_gui/           # Standalone wordlist generator
│   └── wordlist_generator_gui.py
└── 📁 screenshots/                      
```

---

## 🛡️ Ethical Use Notice
This tool is for educational, ethical, and awareness purposes only.
Do not use it for unauthorized access or illegal activities.

---

## 👩‍💻 Author
Sahiti M
© 2025 | All rights reserved
