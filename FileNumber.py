import glob
import os

sorted_files = sorted(
    glob.glob('path/to/your/directory/*.txt'), key=os.path.getmtime)

print(sorted_files)
for i, f in enumerate(sorted_files, 1):
    try:
        head, tail = os.path.split(f)
        os.rename(f, os.path.join(head, str(i).zfill(2) + '_' + tail))
    except OSError:
        print('Invalid operation')
# import os
# i = 1
# for file in os.listdir("/Users/Piotrek/Desktop/HTML_JS_CSS/FilesNumber"):
#     if file.endswith(".pdf"):
#         print('{0:02d}'.format(i) + '_' + file)
#         i+=1
