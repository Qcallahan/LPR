import subprocess

command = [
    'python', 'yolov9/text_reader.py',
    '--conf', '0.4',
    '--device', '0',
    '--weights', 'yolov9/runs/train/exp46/weights/best.pt',
    '--source', '0'
]

subprocess.run(command, check=True)