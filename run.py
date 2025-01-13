import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Run YOLOv9 text reader with customizable confidence threshold.")
parser.add_argument('--conf', type=float, default=0.4, help='Confidence threshold for text detection (default: 0.4)')
parser.add_argument('--device', type=int, default=0, help='Device ID (default: 0)')
parser.add_argument('--weights', type=str, default='model.pt', help='Path to weights file (default: model.pt)')
parser.add_argument('--source', type=str, default='0', help='Source for input (default: 0)')

args = parser.parse_args()

print(args.conf)

command = [
    sys.executable,
    'yolov9/text_reader.py',
    '--conf', str(args.conf),
    '--device', str(args.device),
    '--weights', args.weights,
    '--source', args.source
]

subprocess.run(command, check=True)
