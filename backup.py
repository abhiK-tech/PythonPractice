import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    
    shutil.make_archive(backup_file_name, 'gztar', source)
    print("Backup created:", backup_file_name + ".tar.gz")

source = r"C:\Users\Abhijeet\Documents\Project\python-workshop"
destination = r"C:\Users\Abhijeet\Documents\Project\python-workshop\backups"

backup_files(source, destination)
