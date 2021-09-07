#eval import os

path = 'downloads/Kaizoku480p'

for f in os.listdir(path):
    f_name, f_ext = os.path.splitext(f)
    f_num, f_title = f_name.split('.')
    f_title = f_title.strip()

    new_name = path+'/'+' Ep-{} AnimeName{}'.format(f_num, f_ext)
    os.rename(path+'/'+f, new_name)
