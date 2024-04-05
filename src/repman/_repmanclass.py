#
# RepMan Class File
#

from termcolor import colored
from os import getcwd as pwd, popen as getoutputof, system as run, chdir, listdir
from os.path import expanduser, join
from tkinter import filedialog
from re import search
import subprocess
import platform

class repman:
    def __init__(self, projectpath:str = None):
        self.version = ''
        self.path = projectpath
        self.workingpath = pwd()
    
    def 
    
    def initialize(self):
        # Requisites:
        #   1. installation of code
        #   2. installation of git
        #   3. project folder creation - ask for location.
        try:
            ## PRINT INIT ##
            print(colored('RepMan', 'blue'), colored(f'v{self.version}', 'red'))
            print('RepMan:', colored('Jumpstart', 'yellow'))
            
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
                print('RepMan:', colored(f"vscode found -> {getoutputof('code -v').readline().replace('\n','')}", 'green'))
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
                print('RepMan:', colored(f"git found -> v{getoutputof('git -v').readline().replace('\n','').split(' ')[2]}", 'green'))
            ## GIT INSTALL END ##
            
            ## Project Folder check ##
            if self.path == '':
                print(colored(' Choose a Project folder...', 'blue'), end='\r')
                # -> get filepath
                self.path = filedialog.askdirectory(initialdir=self.workingpath, title='select project path')
                
            # -> resolve where to save the project path
            if platform.system()=='Linux' or platform.system()=='Darwin':
                # -> go to home dir
                chdir(expanduser('~'))
                # -> resolve shell
                shells = []
                filenames = listdir()
                # count shells
                for filename in filenames:
                    if search('^.\w+rc$', filename):
                        shells.append(filename)
                # update every shell
                for shell in shells:
                    # -> remove pre-existing entry of path if any
                    with open(join(expanduser('~'), f'{shell}'), 'r') as shfile:
                        entries = shfile.read().split('\n')
                    
                    for i in range(len(entries)):
                        if search(r'^export\s+REPMAN_PROJECT_PATH=/\w+', entries[i]):
                            # index = entries.index(entry)
                            entries[i] = '\n'
                    
                    with open(join(expanduser('~'), f'{shell}'), 'w') as shfile:
                        for entry in entries:
                            if entry=='\n':
                                entry = ''
                                shfile.write(entry)
                            else:
                                shfile.write(entry+'\n')
                    
                    run(f"echo \"export REPMAN_PROJECT_PATH={self.path}\" >> ~/{shell}")
            print('RepMan:', colored(f'Project Folder set to {self.path}', 'green'))
            print('RepMan:', colored('Jumpstart END', 'green'))
            print('RepMan:', colored('Terminal restart requested!', 'red'))
            exit(0)
        except KeyboardInterrupt:
            exit(1)

def installgit():
    print('RepMan:', colored('git not found.', 'red'))
    print('RepMan:', colored('Installing git.', 'yellow'), end='\r')
    
    if platform.system()=='Linux':
        subprocess.Popen(['sudo', 'apt-get', 'install', 'git'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL).wait()
    
    print('RepMan:', colored(f"git installed -> v{getoutputof('git -v').readline().replace('\n','').split(' ')[2]}", 'green'))

def installvscode():
    print('RepMan:', colored('vscode not found.', 'red'))
    print('RepMan:', colored('Downloading vscode.', 'yellow'), end='\r')
    
    if platform.system()=='Linux':
        if getoutputof('arch').read().replace('\n','')=='aarch64':
            subprocess.Popen(['gdown', 'https://drive.google.com/uc?id=1-PlorBHwmve5-rYx4LGgEsVdcVcsxigE'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL).wait()
            print('RepMan:', colored('Downloaded vscode', 'green'))
            print('RepMan:', colored('Installing vscode', 'yellow'), end='\r')
            subprocess.Popen(['sudo', 'dpkg', '-i', './code-arm64.deb'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL).wait()
            print('RepMan:', colored(f"vscode installed -> v{getoutputof('code -v').readline().replace('\n','')}", 'green'))
