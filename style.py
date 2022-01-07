from rich.progress import track
from rich.console import Console
import time
from rich.table import Table
console = Console()

def add(x, y):
    a = "Salom"
    console.log("Hacker qalesan", log_locals="zor")
    return x + y

add(1, 2)

"""table = Table(title="Hackers community")

table.add_column("info", style="cyan")
table.add_column("Title", style="magenta")
table.add_column("Box office", justify="right", style="green")

table.add_row("Hacker", "cracker", "Fisher")

console = Console()
console.print(table)


for i in track(range(20), description="Yuklanmoqda..."):
    print(f"Yuklandi: {i}")
    time.sleep(0.5)"""
