# Password Toolkit: Strength Analyzer + Wordlist Generator

## Overview

Weak passwords remain one of the most common causes of account compromise and credential-based attacks. This project combines password strength evaluation and custom wordlist generation into a single GUI-based toolkit for security awareness, password analysis, and controlled security testing.

The toolkit uses the zxcvbn password estimation library to analyze password strength and generates customized wordlists using common password mutation techniques such as leetspeak substitutions, case variations, and numeric patterns.

A complete Python GUI application combining:

1. **Password Strength Analyzer** — evaluates passwords using zxcvbn
2. **Custom Wordlist Generator** — creates password lists with leetspeak, case variants, and number patterns

Built with `Tkinter`, styled with Light/Dark mode, and designed for ethical use.

---

## Features

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

## Tech Stack

- Python
- Tkinter
- zxcvbn

---

## Installation


### 1. Clone the repository or download the `.py` file
```bash
git clone https://github.com/s-a-63/password_analyzer_generator.git
cd Password_Toolkit
```

### 2. Install the required Python package:
```bash
pip install zxcvbn
```

## Running the Toolkit
```bash
python pw_toolkit_gui.py
```

---

## Project Structure

```
📁 Password_Toolkit/
├── pw_toolkit_gui.py              # Combined GUI (tabs)
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

## Screenshots

### Password Strength Analyzer

<img src="Password_Toolkit/screenshots/pw_analyzer.png" width="700" height="500"/>

---

### Wordlist Generator

<img src="Password_Toolkit/screenshots/wordlist_generator.png" width="700"/>

---

### Generated Custom Wordlist

<img src="Password_Toolkit/screenshots/generated_wordlist.png" width="700"/>

---

## Challenges Faced

- Designing a responsive Tkinter GUI with tab-based navigation
- Managing multiple password mutation combinations efficiently
- Maintaining usability across Light and Dark mode themes
- Generating meaningful password feedback using zxcvbn outputs

---

## Limitations

- Password strength analysis depends on the zxcvbn estimation model
- Generated wordlists are rule-based and do not include probabilistic attack models
- The toolkit is intended for educational and authorized security testing only
- Extremely large mutation combinations may increase generation time and output size

---

## Ethical Use Notice
This tool is for educational, ethical, and awareness purposes only.
Do not use it for unauthorized access or illegal activities.

---

## Author
Sahiti M | All rights reserved
