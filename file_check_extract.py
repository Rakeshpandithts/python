import os
import re
from pyunpack import Archive
import Archive

final_files_list = []
extractext = ['7z' , 'ace' , 'alz' ,'a' ,'arc','arj','bz2','cab','Z','cpio','deb','dms','gz','lrz','lha','lzh','lz','lzma','lzo','rpm','rar','rz','tar','xz','zip','jar','zoo']
file_folder = '/home/rakesh/zipfileext_new'

def extract_file(i, j, archive_file_path, archive_file_name, exten_type, final_files_list):
    print('archive_file_path = {}'.format(archive_file_path))
    print('archive_file_name = {}'.format(archive_file_name))
    os.chdir(archive_file_path)
    print('ch dir')
    print('filename = {}'.format(archive_file_name))
    ext_folder = archive_file_name.strip('{}'.format(exten_type))
    print('filename ext = {}'.format(ext_folder))
    current_folder = re.sub("[!@#$%^&*()}[]{;:,./<>?\|`~-=_+]", "_", str(ext_folder))
    current_folder = str(current_folder.split('.')[0])
    print('cureent folder{}'.format(current_folder))
    new_ext_folder = os.path.join(str(archive_file_path),str(current_folder.replace(" ","_")))
    print('cureent folder2{}'.format(new_ext_folder))
    if  os.path.exists(str(new_ext_folder)):
        print('path exisits')
        duplicate_folder = 'duplicate('+str(i)+str(j)+')' 
        print(duplicate_folder)
        new_ext_folder = os.path.join(str(new_ext_folder + duplicate_folder))
        print('current folder= {}' .format(current_folder))
        os.mkdir(new_ext_folder)
        print('path created')
    else:
        print('else')
        os.mkdir(new_ext_folder)
    
    Archive(archive_file_name).extractall(new_ext_folder)

    print('archive done')
    folder_path = os.path.join(str(archive_file_path), str(new_ext_folder))
    print('extracted folder path ={}'.format(folder_path))
    check_folder(folder_path, final_files_list)

def check_folder(files_folder, final_files_list):
    list_current_folder_files = os.listdir(files_folder)
    print('list_current_folder_files = {}'.format(list_current_folder_files))
    i =0
    for each_files in list_current_folder_files:
        print('each_files = {}'.format(each_files))
        folder_path = os.path.join(str(files_folder), str(each_files))
        print('folder path = {}'.format(folder_path))
        archivefile = False
        j =0
        for exten in extractext:
            pattern = str("\."+str(exten)+"$")
            if re.search(pattern, str(each_files)):
                print('{} is a {} file'.format(each_files, exten))

                archivefile = True
                extract_file(i, j, files_folder, each_files, exten,final_files_list)
                break
            j = j+1
        if archivefile is True:
            continue
        elif os.path.isdir(folder_path): 
            print('{} is a directry'.format(each_files))
            folder_path = os.path.join(str(files_folder), str(each_files))
            print('folder path = {}'.format(folder_path))
            check_folder(folder_path, final_files_list)
        else:
            final_file_path = os.path.join(str(files_folder), str(each_files))
            print('final_file_path = {}'.format(final_file_path))
            final_files_list.append(final_file_path)
        i = i+1

check_folder(file_folder, final_files_list)
print('final_files_list = {}'.format(final_files_list))


print('DONE')