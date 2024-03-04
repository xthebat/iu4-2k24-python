from argparse import ArgumentParser
from colorama import Fore
import os


class Tree:

    def __init__(self):
        self.__parseOption()

    def __parseOption(self) -> None:
        """Parses the arguments passed on the command line
        """        

        parser = ArgumentParser(description="Build tree of filesystem")

        parser.add_argument("path",type=str, help="start directory")
        parser.add_argument("-d", "--depth", dest="depth", default=None, type=int,
                            help="tree display depth [default: %(default)s]")
        parser.add_argument("-s", "--sort", dest="sort", default=None, type=str,
                            choices=["asc", "desc"], help="sorting asc/desc [default: %(default)s]")
        self.__option = parser.parse_args()


    def print(self) -> None:
        """The main method. Print tree of filesystem
        """        

        if os.path.isdir(self.__option.path):
            print(f"{Fore.BLUE}{self.__option.path}{Fore.RESET}")
            self.__printDir(self.__option.path)
        else:
            print(f"Directory {self.__option.path} does not exist!") 

    
    def __printDir(self, path : str, tmp_depth : int = 0, prefix : str = "") -> None:
        """Prints all objects in the directory recursively

        Args:
            path: directory path
            tmp_depth: current recursion depth
            prefix: current prefix for printing
        """        
        
        if tmp_depth == self.__option.depth:
            return
        
        path_list = os.listdir(path)

        if self.__option.sort is not None:
            path_list.sort(reverse=(self.__option.sort == "desc"))

        for tmp_path in path_list:
            tmp_prefix = prefix + ("'---" if tmp_path == path_list[-1] else "|---")
            next_prefix = prefix + ("    " if tmp_path == path_list[-1] else "|   ")

            abs_path = os.path.join(path, tmp_path)

            self.__printName(tmp_prefix, abs_path)

            if os.path.isdir(abs_path):
                self.__printDir(abs_path, tmp_depth + 1, next_prefix)


    def __printName(self, prefix : str, abs_path : str) -> None:
        """Prints the object located in the directory in a certain color depending on the type

        Args:
            prefix (str): prefix for printing
            abs_path (str): absolute path of the object
        """        
        
        path = os.path.basename(abs_path)

        if os.path.isdir(abs_path):
            print(f"{prefix}{Fore.BLUE}{path}{Fore.RESET}")

        if os.path.isfile(abs_path):
            if os.path.islink(abs_path):
                print(f"{prefix}{Fore.GREEN}{path} -> {os.readlink(abs_path)}{Fore.RESET}")
            else:
                print(f"{prefix}{path}")
