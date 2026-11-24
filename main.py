import os

os.umask(0o022)

LINE = "Gravity: Always drags me down when I'm trying to be productive. Ruins all my dreams of flying. 1/5"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
os.chmod("/output/entry.txt", 0o644)