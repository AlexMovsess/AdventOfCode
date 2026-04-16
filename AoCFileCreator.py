import os
import requests

while True:
    try:
        year = int(input("Enter AoC year :"))
        if year < 2015:
            print("Year must be after 2015.")
        else:
            break
    except ValueError:
        print("Please input a valid integer.")

while True:
    try:
        day = int(input("Enter AoC day :"))
        if day > 26 or day < 1:
            print("Day must be between 1 and 25.")
        else:
            break
    except ValueError:
        print("Please input a valid integer.")

assert 0 < day < 26

assert 2015 <= year

path = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__), f"AdventOfCode{year}/Day{day}")
)
cookie = os.getenv("AOC_SESSION")
url = f"https://adventofcode.com/{year}/day/{day}/input"

if not cookie:
    raise ValueError("AOC_SESSION not set")

cookies = {"session": cookie}

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    raise Exception("Failed to fetch input (cookie probably invalid)")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__), f"AdventOfCode{year}")
)
try:
    os.mkdir(__location__)
except:
    pass

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__), f"AdventOfCode{year}/Day{day}")
)
try:
    os.mkdir(__location__)
except:
    pass

with open(f"{path}/AdventOfCodeDay{day}.txt", "w") as f:
    f.write(response.text)

try:
    f = open(f"{path}/AdventOfCodeDay{day}_1.py", "x")
except FileExistsError:
    print(f"The file '{f"{path}/AdventOfCodeDay{day}_1.py"}' already exists.")
else:
    f.write(f"""import os
            
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'AdventOfCodeDay1.txt')) as f:
    lines = f.readlines()
""")

    f.close()

try:
    f = open(f"{path}/AdventOfCodeDay{day}_2.py", "x")
except FileExistsError:
    print(f"The file '{f"{path}/AdventOfCodeDay{day}_2.py"}' already exists.")
else:
    f.write(f"""import os
            
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'AdventOfCodeDay{day}.txt')) as f:
    lines = f.readlines()
""")

    f.close()
