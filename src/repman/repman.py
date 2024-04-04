#!/usr/bin/env python3

__version__ = '1.0'

from repman._repmanclass import repman
from optioner import options
from sys import argv
from termcolor import colored

# function to print general help
def helper():
    print(colored('RepMan', 'blue'), ': Repository Manager (alias: Project Manager)')
    print(colored(f'v{__version__}\n', 'red'))
    print('help\n')
    print('  |  -h or --help      : show this help text and exit.')
    print('  |  -v or --version   : show version and exit.')
    print('  |  -i or --init      : initialize settings, configurations and exit.')
    print('  |  -a or --add       : add a git repository under RepMan\'s care.')
    print('  |  -o or --open      : open a project/repository.\n')
    print(colored('NOTE', 'blue'), ': For further help, run', colored('\'repman <argument> -h\'', 'red'), 'or', colored('\'repman <argument> --help\'.', 'red'))
    print('\nEND')
    exit(0)

# function to print specialized help on '-v' or '--version'
def version_h(arg:str):
    print(colored('RepMan', 'blue'), ': Repository Manager (alias: Project Manager)')
    print(colored(f'v{__version__}\n', 'red'))
    print('help', colored('EXTENDED', 'blue'), f': help for \'{arg}\'\n')
    print('  | This Argument shows the version information  |')
    print('  | of RepMan.                                   |')
    print('\nEND')
    exit(0)

# function to print specialized help on '-i' or '--init'
def init_h(arg:str):
    print(colored('RepMan', 'blue'), ': Repository Manager (alias: Project Manager)')
    print(colored(f'v{__version__}\n', 'red'))
    print('help', colored('EXTENDED', 'blue'), f': help for \'{arg}\'\n')
    print('  | This argument is used to initialize RepMan.  |')
    print('  |                                              |')
    print('  | It will automatically detect and try to Ini- |')
    print('  | tialize RepMan and all its Configurations.   |')
    print('  |                                              |')
    print('  | This Argument may ask input from the user a- |')
    print('  | bout few Configurations.                     |')
    print('  |                                              |')
    print('  |', colored('Format', 'red'), ': \'repman -i\' or \'repman --init\'      |')
    print('  |                                              |')
    print('\nEND')
    exit(0)

# function to print specialized help on '-a' or '--add'
def add_h(arg:str):
    print(colored('RepMan', 'blue'), ': Repository Manager (alias: Project Manager)')
    print(colored(f'v{__version__}\n', 'red'))
    print('help', colored('EXTENDED', 'blue'), f': help for \'{arg}\'\n')
    print('  | This argument is used to add git repositori- |')
    print('  | es under RepMan\'s care. This basically means |')
    print('  | RepMan will manage that repository for you.  |')
    print('  |                                              |')
    print('  |', colored('Format', 'red'), ': \'repman -a <link>\'                  |')
    print('  |                 or                           |')
    print('  |          \'repman -a <username>/<repo>\'       |')
    print('  |                                              |')
    print('\nEND')
    exit(0)

# function to print specialized help on '-o' or '--open'
def open_h(arg:str):
    print(colored('RepMan', 'blue'), ': Repository Manager (alias: Project Manager)')
    print(colored(f'v{__version__}\n', 'red'))
    print('help', colored('EXTENDED', 'blue'), f': help for \'{arg}\'\n')
    print('  | This argument is used to open projects and   |')
    print('  | work on them as you please.                  |')
    print('  |                                              |')
    print('  | RepMan will automatically add .gitignore fi- |')
    print('  | le if it is not present in the opened proje- |')
    print('  | ct.                                          |')
    print('  |                                              |')
    print('  | Since this is a python project itself, RepMan|')
    print('  | will add the necessary files in the .gitign- |')
    print('  | ore file. such as \'dist\' if the destination  |')
    print('  | is found to be a python project.             |')
    print('  |                                              |')
    print('  |',colored('Format', 'red'), ': \'repman -o <project-name>\'          |')
    print('  |                                              |')
    print('\nEND')
    exit(0)

# function to display version and exit
def version():
    print(colored('RepMan', 'blue'), ': Repository Manager (alias: Project Manager)')
    print('         version', colored(f'v{__version__}', 'red'))
    print('         author:', colored('d33pster', 'light_blue'))
    print('         GitHub:', colored('https://github.com/d33pster', 'light_blue'))
    exit(0)

# function to initialize repman
def init(path: str = None):
    global repmanctrl
    repmanctrl = repman(path)
    
    repmanctrl.version = __version__
    repmanctrl.initialize()

# main function
def main():
    # create arguments
    shortargs = ['h', 'v', 'a', 'i', 'o']
    longargs = ['help', 'version', 'add', 'init', 'open']
    
    # mutually exclusive args
    mutex = [
        ['v', 'version'],['a', 'add', 'i', 'init', 'o', 'open'],
        ['a', 'add'],['o','open', 'i', 'init', 'v', 'version'],
        ['o','open'],['a', 'add', 'i', 'init', 'v', 'version'],
        ['i', 'init'],['o','open', 'v', 'version', 'a', 'add']
    ]
    
    optctrl = options(shortargs, longargs, argv[1:], ifthisthennotthat=mutex)
    
    args, check, error, falseargs = optctrl._argparse()
    
    if not check:
        print(colored('RepMan Err', 'red'), f': {error}')
        exit(1)
    else:
        if len(args)==0:
            print(colored('RepMan Err', 'red'), ': Please tell me what to do.')
            exit(1)
        else:
            # help
            if '-h' in args:
                # check for other args if there, and show help accordingly
                otherarg = ''
                if len(args)==2:
                    # if length of all args = 2, i.e some other arg is there
                    # find -h's index, the other one must be the arg, the user is asking help for.
                    index = args.index('-h')
                    if index==0:
                        otherarg = args[1]
                    else:
                        otherarg = args[0]
                    
                    if otherarg=='-h' or otherarg=='--help':
                        helper()
                    elif otherarg=='-v' or otherarg=='--version':
                        version_h(otherarg)
                    elif otherarg=='-i' or otherarg=='--init':
                        init_h(otherarg)
                    elif otherarg=='-a' or otherarg=='--add':
                        add_h(otherarg)
                    elif otherarg=='-o' or otherarg=='--open':
                        open_h(otherarg)
                    else:
                        print(colored('RepMan Err', 'red'), f': argument \'{otherarg}\' is not recognised.')
                elif len(args)<2:
                    helper()
                elif len(args)>2:
                    print(colored('RepMan Err', 'red'), ': Please use one argument at a time to show help on that argument.')
                    print(colored('Format', 'blue'), ': \'repman <argument> -h\' or \'repman <argument> --help\'.')
                    exit(1)
                else:
                    print(colored('RepMan Err', 'red'), ': Could not resolve arguments.')
                    print(colored('RepMan Hint', 'blue'), ': Run \'repman -h\' or \'repman --help\'.')
                    exit(1)
            elif '--help' in args:
                # check for other args if there, and show help accordingly
                otherarg = ''
                if len(args)==2:
                    # if length of all args = 2, i.e some other arg is there
                    # find -h's index, the other one must be the arg, the user is asking help for.
                    index = args.index('--help')
                    if index==0:
                        otherarg = args[1]
                    else:
                        otherarg = args[0]
                    
                    if otherarg=='-h' or otherarg=='--help':
                        helper()
                    elif otherarg=='-v' or otherarg=='--version':
                        version_h(otherarg)
                    elif otherarg=='-i' or otherarg=='--init':
                        init_h(otherarg)
                    elif otherarg=='-a' or otherarg=='--add':
                        add_h(otherarg)
                    elif otherarg=='-o' or otherarg=='--open':
                        open_h(otherarg)
                    else:
                        print(colored('RepMan Err', 'red'), f': argument \'{otherarg}\' is not recognised.')
                elif len(args)<2:
                    helper()
                elif len(args)>2:
                    print(colored('RepMan Err', 'red'), ': Please use one argument at a time to show help on that argument.')
                    print(colored('Format', 'blue'), ': \'repman <argument> -h\' or \'repman <argument> --help\'.')
                    exit(1)
                else:
                    print(colored('RepMan Err', 'red'), ': Could not resolve arguments.')
                    print(colored('RepMan Hint', 'blue'), ': Run \'repman -h\' or \'repman --help\'.')
                    exit(1)
            else:
                pass
            
            # version
            if '-v' in args or '--version' in args:
                version()
            
            # init
            if '-i' in args:
                index = args.index('-i')
                try:
                    value = args[index+1]
                except IndexError:
                    value = None
                
                if value==None:
                    init()
                else:
                    init(value)
            elif '--init' in args:
                index = args.index('--init')
                try:
                    value = args[index+1]
                except IndexError:
                    value = None
                
                if value==None:
                    init()
                else:
                    init(value)
            
            # all others
                    

if __name__=='__main__':
    repmanctrl: repman
    main()