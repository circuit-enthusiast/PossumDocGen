import sys
from datetime import datetime

#==================== LOAD VARIABLES ====================#

#TODO - setup a system where a setting files is made for the project and is used by the make script

#==================== DIRECTORIES ====================#
proj_root = ''
library_dir_name = 'lib'
binary_dir_name = 'bin'
source_dir_name = 'src'
files = [library_dir_name, binary_dir_name, source_dir_name]

#==================== HANDLE ARGUMENT ====================#
main_ext = ''
compiler = ''

def usage():
    usageMsg = 'usage: python papbuilder.py [option] ...[-l language]\nOptions:'
    options = ['-l', '-h','-n']
    option_desc = ['defines the main programming language used for the project', 'prints out this message']
    print(usageMsg)
    for o in options:
        print('\t',o,' ',option_desc[options.index(o)])
        

for x in sys.argv:
    if '-' in x:
        if x == '-h':
            usage()
        elif x == '-l':

            language = sys.argv[sys.argv.index(x)+1]

            if language.lower() == 'c':

                main_ext = '.c'
                compiler = 'gcc -o ' + binary_dir_name+'/templateBIN' + ' -g -Wall' + source_dir_name + '/' #add later the main file

            elif language.lower() == 'cpp':

                main_ext = '.cpp'
                compiler = 'gcc' #to be completed
            
            elif language.lower() == 'java':
            
                main_ext = '.java'
                compiler = 'java'
            
            elif language.lower() == 'cs':
            
                main_ext = '.cs'
                compiler = 'dotnet build' #to be completed
            
            elif language.lower() == 'py':
            
                main_ext = '.py'
                compilet = 'python'
            
            else:
            
                print('Unknown language...')
        
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
template_main = 'src/Main'+main_ext
makefile = 'make'+make_ext


#==================== FILE-CONTENTS ====================#
readme_content = 'static initial :: To be removed :: '+datetime.today().strftime('%Y-%m-%d %H:%M:%S')

makefile_content = ''
if make_ext == '.ps1':
    makefile_content = compiler+''
