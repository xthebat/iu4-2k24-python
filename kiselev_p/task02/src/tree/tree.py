from colorama import Fore
import os

class TreeException(Exception):
    pass

class Tree:

    def build(self, path: str, depth: int=None, sort: str=None) -> None:
        """The main method

        Args:
            path: directory path
            depth: recursion depth
            sort: sort content in directory
        """

        if not os.path.isdir(path):
            raise TreeException(f"{path} is an incorrect directory!")
        if (depth is not None) and (depth < 0):
            raise TreeException(f"{depth} is an incorrect depth!")
        if sort not in ["asc", "desc", None]:
            raise TreeException(f"{sort} is an incorrect sort option!")
        
        self.__depth = depth
        self.__sort = sort
        self.__printDir(path)

    def __printDir(self, path: str, tmp_depth: int=0, tmp_preffix: str="") -> None:
        """Prints all objects in the directory recursively

        Args:
            path: directory path
            tmp_depth: current recursion depth
            tmp_prefix: current prefix for printing
        """

        if not tmp_depth:
            print(f"{Fore.BLUE}{path}{Fore.RESET}")

        if tmp_depth == self.__depth:
            return
        
        path_list = os.listdir(path)

        if self.__sort is not None:
            path_list.sort(reverse=(self.__sort == "desc"))

        for tmp_path in path_list:
            tmp_prefix = tmp_preffix + ("'---" if tmp_path == path_list[-1] else "|---")
            next_prefix = tmp_preffix + ("    " if tmp_path == path_list[-1] else "|   ")

            abs_path = os.path.join(path, tmp_path)

            self.__printContent(tmp_prefix, abs_path)

            if os.path.isdir(abs_path):
                self.__printDir(abs_path, tmp_depth + 1, next_prefix)

    def __printContent(self, prefix: str, abs_path: str) -> None:
            """Prints the object located in the directory
            in a certain color depending on the type

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
