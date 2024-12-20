import sys
import subprocess

command = [
    sys.executable,
    'yolov9/text_reader.py',
    '--conf', '0.4',
    '--device', '0',
    '--weights', 'model.pt',
    '--source', '0'
]

subprocess.run(command, check=True)
