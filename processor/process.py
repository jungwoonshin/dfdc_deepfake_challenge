import json
import shutil

import os, sys
root_folder = os.path.abspath(
   os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.append(root_folder)
from training.datasets.validation_set import PUBLIC_SET

f = open("/home/jungwoon/github/dfdc_deepfake_challenge/processor/metadata.json")
data = json.load(f)

file_name_lst = []
index = 0
for key in (list(data.keys())):
    if not key in data: continue
    if data[key].get("original", "") == "":
        file_name_lst.append(key)
        # new_dict[key] = data[key]
        index += 1
        if index > 16:
            break
        
file_name_lst_01 = file_name_lst[:len(file_name_lst)//2]
file_name_lst_02 = file_name_lst[len(file_name_lst)//2:]
new_dict_01 = {}
new_dict_02 = {}

for key in file_name_lst_01:
    new_dict_01[key] = data[key]
for key in file_name_lst_02:
    new_dict_02[key] = data[key]
    
for key in data.keys():
    if data[key].get("original", "") in file_name_lst_01:
        new_dict_01[key] = data[key]
    if data[key].get("original", "") in file_name_lst_02:
        new_dict_02[key] = data[key]
print(new_dict_01)
print(len(new_dict_01))
print(new_dict_02)
print(len(new_dict_02))

fp = open('/home/jungwoon/github/dfdc_deepfake_challenge/processor/sample_train_metadata.json', 'w')
json.dump(new_dict_01, fp)
fp = open('/home/jungwoon/github/dfdc_deepfake_challenge/processor/sample_valid_metadata.json', 'w')
json.dump(new_dict_02, fp)

for key in new_dict_01.keys():
    shutil.copyfile('/home/jungwoon/github/dfdc_deepfake_challenge/full_dataset/' + key, '/home/jungwoon/github/dfdc_deepfake_challenge/dataset/dfdc_train_001/' + key)
for key in new_dict_02.keys():
    shutil.copyfile('/home/jungwoon/github/dfdc_deepfake_challenge/full_dataset/' + key, '/home/jungwoon/github/dfdc_deepfake_challenge/dataset/dfdc_train_001/' + key)
    
