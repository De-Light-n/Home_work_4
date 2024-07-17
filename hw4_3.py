import sys
from pathlib import Path
from colorama import Fore


def color_path(path, k:int=0):
    current_path = Path(path)
    if current_path.exists():
        if current_path.is_dir():
            print(" | "*k + f" {Fore.YELLOW}{current_path.name}{Fore.RESET}")
            items = current_path.iterdir()
            for item in items:
                color_path(item, k+1)
        else:
            print(" | "*k + f" {Fore.BLUE}{current_path.name}{Fore.RESET}")
    else:
        print("Шляху не існує")
    

if __name__=="__main__":
    if len(sys.argv)<2:
        path = ""
    else:
        path = sys.argv[1]
    color_path(path)
