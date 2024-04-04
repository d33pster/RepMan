#
# RepMan Class File
#

from termcolor import colored
from os import getcwd as pwd, popen as getoutputof
from os.path import expanduser, join
import subprocess
import platform

class repman:
    def __init__(self, projectpath:str = None):
        self.version = ''
        self.path = projectpath
        self.workingpath = pwd()
    
    def initialize(self):
        # Requisites:
        #   1. installation of code
        #   2. installation of git
        #   3. project folder creation - ask for location.
        
        ## PRINT INIT ##
        print(colored('RepMan', 'blue'), colored(f'v{self.version}', 'red'))
        print(colored('initializing...', 'yellow'))
        
        ## INSTALLATION OF CODE ##
        # -> check existing installation
        checkcodeinstall = True
        try:
            line = getoutputof('code -v').readline().replace('\n', '').replace('v','').split('.')[0] # should be version
            
            try:
                line = int(line)
            except ValueError:
                checkcodeinstall = False
        except IndexError:
            checkcodeinstall = False
        
        if not checkcodeinstall:
            installvscode()
        else:
            print(colored('RepMan Init Status', 'green'), ': vscode installation found.')
        ## CODE INSTALLATION END ##
        
        ## installation of git ##
        checkgitinstall = True
        try:
            line = getoutputof('git -v').readline().replace('\n','').split(' ')[2].split('.')[0]

            try:
                line = int(line)
            except ValueError:
                checkgitinstall = False
        except IndexError:
            checkgitinstall = False
        
        if not checkgitinstall:
            installgit()
        else:
            print(colored('RepMan Init Status', 'green'), f": git found -> v{getoutputof('git -v').readline().replace('\n','').split(' ')[2]}")

def installgit():
    print(colored('RepMan Init Status', 'red'), ': git not found.')
    print(colored('RepMan Init Status', 'yellow'), ': Installing git...')
    
    if platform.system()=='Linux':
        subprocess.Popen(['sudo', 'apt-get', 'install', 'git'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL).wait()
    
    print(colored('RepMan Init Status', 'green'), f": git installed -> v{getoutputof('git -v').readline().replace('\n','').split(' ')[2]}")

def installvscode():
    print("install")