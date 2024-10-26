import subprocess
import json


try:
        subprocess.run(["python", "Python Files/files.py"], check=True)
        for i in range(0,3, 1):
                
                subprocess.run(["python", "Python Files/data/read.py"], check=True)
                subprocess.run(["python", "Python Files/download.py"], check=True)
                subprocess.run(["python", "Python Files/fps.py"], check=True)
                subprocess.run(["python", "Python Files/join.py"], check=True)
                subprocess.run(["python", "Python Files/bgm.py"], check=True)
                subprocess.run(["python", "Python Files/delete.py"], check=True)
                subprocess.run(["python", "Python Files/upload.py"], check=True)
                subprocess.run(["python", "Python Files/data/write.py"], check=True)

                print("##########################################################")
                print(f"###################### video {i+1} ###########################")
                print("##########################################################")

except json.decoder.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
