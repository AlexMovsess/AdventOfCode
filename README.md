# 🎄 Advent of Code

Repository containing my solutions for the Advent of Code challenges.

---

## Project structure

Each year is organized in its own folder:

```

AdventOfCode/
├── AdventOfCode2023/
├── AdventOfCode2024/
└── AdventOfCode2025/

````

Each day contains:
- the input file
- the solutions for each problems

---

## AoC File Creator

The script `AoCFileCreator.py` helps you:
- create folders for a given year/day
- download your personal input
- generate starter Python files

---

##  Authentication (required)

To download inputs from Advent of Code, you must set your session cookie as an environment variable.

###  Windows (PowerShell)

```powershell
$env:AOC_SESSION="your_cookie_here"
````

---

## How to get your session cookie

1. Go to [https://adventofcode.com](https://adventofcode.com) and log in
2. Open Developer Tools (`F12`)
3. Go to **Application** tab
4. Navigate to:
   **Cookies → [https://adventofcode.com](https://adventofcode.com)**
5. Copy the value of the `session` cookie


## ⚠️ Important

* Do NOT share your session cookie publicly
* Do NOT commit it to version control
* Treat it like a password


##  Usage

Run the script:

```bash
python AoCFileCreator.py
```

Then enter:

* the year
* the day

The script will automatically generate a txt file of your input and python files with that input loaded and ready.

