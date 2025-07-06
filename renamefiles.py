import argparse
import glob
import os


def renamefiles(args):
    if args.filesextension is None:
        extension = ".*"
    else:
        extension = args.filesextension
        if not extension.startswith('.'):
            extension = '.' + extension

    
    # Create search pattern
    pattern = os.path.join(args.path, f'*{extension}')
    
    # Get all matching files
    files = glob.glob(pattern)

    for file in files:
        print(file)
        filename = os.path.basename(file)
        directory = os.path.dirname(file)
        if (args.replaceword is not None) and (args.newword is not None):
            filename = filename.replace(args.replaceword,args.newword)
        if args.addprefix is not None:
            filename = f"{args.addprefix}{filename}"
        if args.returnlowcasenames == 1:
            filename = filename.lower()
        
        print(filename)

        os.rename(file,f"{directory}/{filename}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='The scripts rename files')
    
    # Add arguments
    parser.add_argument('path', help='Path to the directory where the files are. (required)')
    parser.add_argument('--filesextension', '-x', help='File extention of the files (optional)')
    parser.add_argument('--returnlowcasenames', '-l', default=1, help='Either the renamed files will in be low case (default: l)')
    parser.add_argument('--addprefix', '-d', help='Add a prefix in the files (optional)')
    parser.add_argument('--replaceword', '-w', help='Replace a word in the filename with a new word (optional)')
    parser.add_argument('--newword', '-r', help='The word to replace the replaceword(optional)')
    
    # Parse arguments
    args = parser.parse_args()

    renamefiles(args)



if __name__ == '__main__':
    main()