import datetime
import sys
from pathlib import Path

def main():
    # Get script directory
    if getattr(sys, 'frozen', False):
        script_dir = Path(sys.executable).parent
    else:
        script_dir = Path(__file__).parent
    
    # Write log
    log_file = script_dir / "execution.log"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] Script executed successfully\n")
    
    print("Done! Log written to execution.log")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
