import requests
import os
import tqdm

f_train = open('fashion_train.txt', "r")
f_test = open('fashion_test.txt', "r")

train_files = f_train.readlines()
test_files = f_test.readlines()

if not os.path.exists("train"):
    os.mkdir('train')
    os.mkdir('test')

for video_url in tqdm.tqdm(train_files):
    r = requests.get(video_url[:-1])
    file_name = video_url[:-1].split("/")[-1]
    with open("train/"+file_name,'wb') as f:
        f.write(r.content)

for video_url in tqdm.tqdm(test_files):
    r = requests.get(video_url[:-1])
    file_name = video_url[:-1].split("/")[-1]
    with open("test/"+file_name,'wb') as f:
        f.write(r.content)
