import sys
import os
from datetime import datetime

#==================== LOAD VARIABLES ====================#

#TODO - setup a system where a setting files is made for the project and is used by the make script
cust_lib = []#TODO -  figure out how to add to array


#==================== DIRECTORIES ====================#
proj_root = ''
library_dir_name = 'lib'
binary_dir_name = 'bin'
testing_dir_name = 'tbin'
source_dir_name = 'src'
files = [library_dir_name, binary_dir_name, testing_dir_name, source_dir_name]

#==================== HANDLE ARGUMENT ====================#
main_ext = ''
compiler_str = ''
script_name = sys.argv[0]

def usage():
    usageMsg = 'usage: python ' + script_name + ' [option] ...[-l language]\nOptions:'
    options = ['-l', '-h','-n']
    option_desc = ['defines the main programming language used for the project', 'prints out this message', 'defines the project name']
    print(usageMsg)
    for o in options:
        print('\t',o,' ',option_desc[options.index(o)])
    exit()

for x in sys.argv:
    if '-' in x:
        if x == '-h':
            usage()
        elif x == '-l':

            language = sys.argv[sys.argv.index(x)+1]

            if language.lower() == 'c':

                main_ext = '.c'
                compiler_str = 'gcc -o ' + binary_dir_name+'/templateBIN' + ' -g -Wall' + source_dir_name + '/' #add later the main file

            elif language.lower() == 'cpp':

                main_ext = '.cpp'
                compiler_str = 'g++' #to be completed
            
            elif language.lower() == 'java':
            
                main_ext = '.java'
                compiler_str = 'java'
            
            elif language.lower() == 'cs':
            
                main_ext = '.cs'
                compiler_str = 'dotnet build' #to be completed
            
            elif language.lower() == 'py':
            
                main_ext = '.py'
                compilet = 'python'
            
            else:
            
                print('Unknown option...')
        
        elif x == '-n':
            proj_root = sys.argv[sys.argv.index(x)+1]

        else:
            usage()
    else:
        usage()


#==================== FILE-PATHS ====================#
make_ext = ''
if 'win' in os.name.lower():
    make_ext = '.ps1'
else:
    make_ext = '.sh'

readme_path = './README.txt'
template_main = source_dir_name+'/Main'+main_ext
makefile = 'make'+make_ext


#==================== FILE-CONTENTS ====================#
readme_content = 'static initial :: To be removed :: '+datetime.today().strftime('%Y-%m-%d %H:%M:%S')#deprecated
readme_template = "TODO"
with open(readme_template, "r") as f:
    readme_content = f.read()

makefile_content = ''
if make_ext == '.ps1':
    makefile_content = compiler_str+''#TODO - Complete teh makefile content


#==================== BUILDING-PROJECT ====================#
def create_project():
    os.mkdir(proj_root)
    for file in files:
        os.mkdir(proj_root+"/"+file)
    