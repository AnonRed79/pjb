import requests, os, subprocess

version = ""
ext = ""


class Repos:
    repos:list[str] = []

    @classmethod
    def add(cls, repository_location):

        cls.repos.append(repository_location)


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


        print("0. requested libraries:", Libraries.lib)


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