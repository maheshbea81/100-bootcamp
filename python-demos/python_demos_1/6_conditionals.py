# Testing for system and platform information
import os
import sys

if sys.platform == "win32":
    # print(os.environ)
    home_drive = os.environ["HOMEDRIVE"]
    home_path = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print("Home Drive", home_drive)


# Using MATCH CASE
http_code = "418"

match http_code:
    case "200":
        print("OK")
    case "404":
        print("Not Found")
    case "418":
        print("Some other problem")
        print("I am a teapot")
    case _:
        print("Code not found")
