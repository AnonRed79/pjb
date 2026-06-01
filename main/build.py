from pjbuilder import *
import os, subprocess






#TODO 1. define repos
#TODO 2. define output locations
#TODO 3. select and download libraries
#TODO     1. download pjb.cfg
#TODO     2. check pjb.cfg's for requested libraries
#TODO     3. download requested libraries.

#TODO 4. compile java project

#TODO 5. run project
#TODO 6. jar compiled project project
#TODO 7. run jar'd project



Repos.add("http://localhost:400")
Repos.add("http://localhost:401")
Repos.add("http://localhost:402")

Libraries.add("Lib")



Tasks.download()

# print(os.listdir())

# Tasks.build()
# Locations.project_main_file = "net.anonhub.here.Main"
# Tasks.run()

# for location in dirs:
#     if not os.path.exists(location):
#         print(f"this path does not exist: {location}")
#         continue
#     if os.path.isdir(location):
#         for spot in os.listdir(location):
#             dirs.append(spot)
#     elif os.path.isfile(location):
#         files.append(location)
#     else:
#         print(f"not a file, not a folder, what is this: {location}")
