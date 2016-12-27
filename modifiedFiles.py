import os, glob
import shutil
from datetime import datetime,timedelta


source = 'C:\Users\Wil\Desktop\Folder A'
dest = 'C:\Users\Wil\Desktop\Folder B'

for file in glob.glob(os.path.join(source, '*.txt')):
    file_name = os.path.basename(file)
    time_info = os.path.getmtime(file)
    date = datetime.fromtimestamp(time_info)
    if date > (datetime.today() - timedelta(1)):
        shutil.move(file,dest)
        print file_name + ' -Moved'
    else:
        print file_name + ' -Not Moved'
