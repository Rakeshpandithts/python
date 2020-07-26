import sys
import os
import zipfile
import re
from pyunpack import Archive
files_collected = []
files_collection = {}
extractext = ['7z' , 'ace' , 'alz' ,'a' ,'arc','arj','bz2','cab','Z','cpio','deb','dms','gz','lrz','lha','lzh','lz','lzma','lzo','rpm','rar','rz','tar','xz','zip','jar','zoo']
def check_folder(current_folder, files_collection):
    #print "CHECKING THE EXISITING ZIP FILE IN FOLDER"
    all_zip_file = []
    list_files = os.listdir(current_folder)
    #print list_files
    for each_file_in in list_files:
        #print each_file_in
        return_accept = False
        for each_exten in extractext:
            each_pattren =str("\."+str(each_exten)+"$")
            if re.search(each_pattren,str(each_file_in)):
                all_zip_file.append(os.path.join(str(current_folder),str(each_file_in)))
                return_accept = True

        if return_accept == False: 
            if current_folder not in files_collection.keys():
                files_collection[current_folder] = []
                files_collection[current_folder].append(each_file_in)
            else:
                files_collection[current_folder].append(each_file_in)

    return all_zip_file

def extract(i, filename, folder_name, files_collection, exten):
    #print "EXTRACT PROCESSING STARTED"
    os.chdir(folder_name)
    print('filename = {}'.format(filename))
    filename = filename.strip('{}'.format(exten))
    print('filename ext = {}'.format(filename))
    
    current_folder = re.sub("[!@#$%^&*()}[]{;:,./<>?\|`~-=_+]", "_", str(filename))
    current_folder = str(current_folder.split('.')[0])
    print('cureent folder{}'.format(current_folder))
    current_folder = os.path.join(str(folder_name),str(current_folder.replace(" ","_")))
    print('cureent folder2{}'.format(current_folder))
    

    #current_folder = os.path.join(folder_name,str(filename.strip('.zip').punctuation.replace(" ","_")))
    if  os.path.exists(str(current_folder)):
        print('path exisits')
        duplicate_folder = 'duplicate({})'.format(i) 
        print()
        current_folder = os.path.join(str(current_folder + duplicate_folder))
        print('current folder= {}' .format(current_folder))
        os.mkdir(str(current_folder))
        print('path created')
    else:
        print('else')
        os.mkdir(str(current_folder))
    
    archfile = Archive(filename)
    print('archfile {}'.format(archfile))
    archfile.extractall(current_folder)
    print('archdone')
    return_list = check_folder(current_folder, files_collection)
    #print "RETURN LIST {}".format(return_list)
    if return_list!=[]:
        for each_one in return_list:
            ret, files_collection =  extract(i,each_one,current_folder, files_collection,exten)
            print(ret)
            print('file collection in extract {}'.format(files_collection))
            i = i+1
            print('i in unzip {}'.format(i))

    else:
        print (files_collection)
        print ("Compleated Process")
        #print "AFTER COMPLTE {}".format(self.files_collection)
        return True, files_collection


def unzipping_process(file_folder, files_collection):
    '''merging and unzip the files and return the only files(no zip and other formats)'''
    print ("unzip PROCESS")
    listfiles = os.listdir(file_folder)
    i =0
    for each_file in listfiles:
        print ('each folder {}'.format(each_file))
        observed_accept = False
        for exten in extractext:
            #print "EXTN {}".format(exten)
            pattern = str("\."+str(exten)+"$")
            #print "PATTERN {}".format(pattern)
            if re.search(pattern,str(each_file)):
                print ("Started UNZIPPING")
                ret, files_collection =  extract(i, each_file,file_folder, files_collection, exten)
                print(ret)
                print('unzip file collection {}'.format(files_collection))     
                observed_accept = True
            
           

        if observed_accept == False:
            print('observerd false')
            if file_folder not in files_collection.keys():
                files_collection[file_folder] = []
                files_collection[file_folder].append(each_file)
            else:
                files_collection[file_folder].append(each_file)
            
    
    print ("COLLECTED THE FILE TO MERAGE {}".format(files_collection))

file_folder = 'C:\projects\myfolder'
unzipping_process(file_folder, files_collection)
