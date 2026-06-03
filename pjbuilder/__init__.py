import requests, os, subprocess

version = ""
ext = ""

class Operator:
    order:list[Operator] = []
    def __init__(self, name:str, location:tuple[int, int], seperator:str = ""):
        self.name = name
        self.location = location
        self.seperator = seperator
        Operator.order.append(self)
    
    def __repr__(self):
        return f"Operator({self.name})"


class Repos:
    repos:list[str] = []
    definitions:list[str] = []

    @classmethod
    def add(cls, repository_location:str):
        cls.repos.append(repository_location)
        cls.definitions.append(None)

    @classmethod
    def define(cls, definition, repository_index:int=-1):
        cls.definitions[repository_index] = definition

class Locations:
    libraries = ["libcache"]

    output_dir = "out"

    project_srcs = ["src"]
    project_main_file = "Main.class"


class Libraries:
    lib:list[str] = []

    @classmethod
    def add(cls, lib):

        cls.lib.append(lib)

class Tasks:
    @staticmethod
    def download():
        # response = requests.get(f"{repo}/{module}/{version}{ext}")


        # print("0. requested libraries:", Libraries.lib)
        for lib in Libraries.lib:
            if ":" not in lib:
                version = "latest"
            else:
                lib, version = lib.split(":")
            print(lib)
            print(version)
            location = ""
            for repo in Repos.repos:
                try:
                    response = requests.get(f"{repo}/repo.pjb")
                except requests.exceptions.ConnectionError as e:
                    print(f"could not connect to {repo}")
                    continue

                if response.status_code != 200:
                    print(f"error getting repo from {repo}")
                    continue

                for line in response.content.decode("utf-8").split("\n"):
                    if line.startswith("#"):
                        continue
                    if ".pjb" in line and lib == line[:-4]:
                        try:
                            response = requests.get(f"{repo}/{line}")
                        except requests.exceptions.ConnectionError as e:
                            print(f"could not connect to {repo}")
                            continue

                        for line in response.content.decode("utf-8").split("\n"):
                            start:list[str] = []
                            end:list[str] = []
                            for index in range(len(line)):
                                match line[index]:
                                    case "{":
                                        start.append(index)
                                match line[index]:
                                    case "}":
                                        end.append(index)
                            if len(start) != len(end):
                                raise (ValueError(f"line \"{line}\" is not formatted properly"))

                            name = None
                            primary = None
                            secondary = None
                            tertiary = None
                            ext = None
                            meta = None
                            
                            for i in range(len(start)):
                                if line[start[i]:end[i]] in ["{name", "{primary", "{secondary", "{tertiary", "{ext", "{meta"]:
                                        #put the name and location then it cuts from the end of this
                                        # operator to the start of the next one and sets that as the seperator
                                        try:
                                            name = Operator(line[start[i]+1:end[i]], tuple([start[i], end[i]]), line[end[i]+1:][:line[end[i]+1:].index("{")])
                                        except ValueError as e:
                                            if "substring not found" in str(e):
                                                name = Operator(line[start[i]+1:end[i]], tuple([start[i], end[i]]))
                                            else:
                                                raise ValueError(e)
                                    # case _:
                                    #     if line[start[i]+1:end[i]] == "":
                                    #         print(ValueError(f"There is an empty operator at {start[i]}"))
                                    #     else:
                                    #         print(ValueError(f"There is an unkown operator at {start[i]}: \"{line[start[i]+1:end[i]]}\""))
                                

                            for op in Operator.order:
                                print(f"{op.name}{op.seperator}", end="")
                            print()


                            


        # for i in Repos.repos:
        #     response = requests.get(f"{i}/repo.pjb")
        #     if response.status_code != 200:
        #         print(f"error getting repo.pjb from repository {i}")
        #         continue

        #     for line in response.content.decode("utf-8").split("\n"):
        #         if line.startswith("#"):
        #             continue

                
        #         print(f"{i}/{line}")

    @staticmethod
    def build():
        files = set()
        locations = set(Locations.project_srcs)
        while len(locations) > 0:
            for src in set(locations):
                if len(os.listdir(src)) <= 0:
                    locations.remove(src)
                    continue
                for item in os.listdir(src):
                    item = f"{src}/{item}"
                    if os.path.isfile(item) and item.endswith(".java"):
                        files.add(item)
                    elif os.path.isdir(item):
                        locations.add(item)
                locations.remove(src)

        jars = set()
        locations = set(Locations.libraries)
        while len(locations) > 0:
            for src in set(locations):
                if len(os.listdir(src)) <= 0:
                    locations.remove(src)
                    continue
                for item in os.listdir(src):
                    item = f"{src}/{item}"
                    if os.path.isfile(item) and item.endswith(".jar"):
                        jars.add(item)
                    elif os.path.isdir(item):
                        locations.add(item)
                locations.remove(src)
        
    
        command = []
        command.append("javac")
        command.append("-cp")

        js = ""

        for jar in jars:
            js += f"{jar}:"

        js = js[:-1]

        command.append(js)

        command.append("-d")
        command.append(Locations.output_dir)
        
        for file in files:
            command.append(file)

        print(command)
        subprocess.run(command)

    @staticmethod
    def run():
        jars = set()
        locations = set(Locations.libraries)
        while len(locations) > 0:
            for src in set(locations):
                if len(os.listdir(src)) <= 0:
                    locations.remove(src)
                    continue
                for item in os.listdir(src):
                    item = f"{src}/{item}"
                    if os.path.isfile(item) and item.endswith(".jar"):
                        jars.add(item)
                    elif os.path.isdir(item):
                        locations.add(item)
                locations.remove(src)
        command = []
        command.append("java")
        command.append("-cp")
        
        files = ""
        files += Locations.output_dir+":"
        for jar in jars:
            files += jar+":"
        files = files[:-1]

        command.append(files)

        command.append(Locations.project_main_file)
        subprocess.run(command)