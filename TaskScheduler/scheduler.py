import schedule
import time
import os

def backup_files():
    os.system('cp /path/to/source /path/to/destination')
    print("Backup completed.")

schedule.every().day.at("10:00").do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(1)

