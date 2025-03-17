Download model_small.pt from https://drive.google.com/drive/folders/1oFZKeHdPO4kpvvBy2xtMCzpo4BPjwiiq?usp=sharing
and place it in the LPR folder

To run in git bash:

cd to this folder

python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

python run.py

if there are issues with torch it may be related to the python version, try downloading Python 3.9.13
