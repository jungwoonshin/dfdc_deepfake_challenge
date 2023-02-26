dic = {
    "rmygsfjyvt.mp4": {"label": "REAL", "split": "train"},
    "vcqdmzirff.mp4": {"label": "REAL", "split": "train"},
    "kczkjyntbx.mp4": {"label": "REAL", "split": "train"},
    "msbqgoxxlh.mp4": {"label": "REAL", "split": "train"},
    "sxzddbulvt.mp4": {"label": "REAL", "split": "train"},
    "vqibhetnwa.mp4": {"label": "REAL", "split": "train"},
    "nlvvgrinhn.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "ccggqzuotg.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "jyzfnuaujf.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "jlkzypbjmv.mp4": {"label": "FAKE", "split": "train", "original": "vqibhetnwa.mp4"},
    "btzqiokysa.mp4": {"label": "FAKE", "split": "train", "original": "vqibhetnwa.mp4"},
    "tjpqsayhgq.mp4": {"label": "FAKE", "split": "train", "original": "rmygsfjyvt.mp4"},
    "evnfjvobno.mp4": {"label": "FAKE", "split": "train", "original": "rmygsfjyvt.mp4"},
    "cquhouhgoc.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "vwnuhvbnsq.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
    "kzrbfsoxtj.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "djrfxolqxm.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "kgowzoxjfq.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
    "vcnekqcsgm.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "hidwnstahw.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
    "xbnitlqjop.mp4": {"label": "FAKE", "split": "train", "original": "rmygsfjyvt.mp4"},
    "dcgnumdfoq.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
    "wdhfkfsraq.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "pmkxnqlmbj.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "wmnajexzkj.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "cksjhegwyq.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "nuzbbjlaed.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
    "cdgulhthen.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "ncfkflbbdq.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
    "mtlmydhbyo.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "zdvzavvspr.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "aqrzuafttg.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "lvbyubftbz.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "qxsyrjyuxs.mp4": {"label": "FAKE", "split": "train", "original": "rmygsfjyvt.mp4"},
    "jdffbokydq.mp4": {"label": "FAKE", "split": "train", "original": "rmygsfjyvt.mp4"},
    "qfrxxdiimw.mp4": {"label": "FAKE", "split": "train", "original": "kczkjyntbx.mp4"},
    "dtngwlnmhu.mp4": {"label": "FAKE", "split": "train", "original": "vqibhetnwa.mp4"},
    "moosxkzotj.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "qucelvhhbb.mp4": {"label": "FAKE", "split": "train", "original": "vcqdmzirff.mp4"},
    "tffpdgvdko.mp4": {"label": "FAKE", "split": "train", "original": "rmygsfjyvt.mp4"},
    "dobmkyconz.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "klapyuhmgc.mp4": {"label": "FAKE", "split": "train", "original": "msbqgoxxlh.mp4"},
    "joezmuxfzt.mp4": {"label": "FAKE", "split": "train", "original": "sxzddbulvt.mp4"},
}

result = []
for key in dic.keys():
    result.append(key)
    
print(result)

import json
f = open("C:/Users/user/Documents/GitHub/dfdc_deepfake_challenge/processor/sample_valid_metadata.json")
valid_data = json.load(f)
f = open("C:/Users/user/Documents/GitHub/dfdc_deepfake_challenge/processor/sample_train_metadata.json")
train_data = json.load(f)

train_data.update(valid_data)
print(len(train_data))
fp = open('C:/Users/user/Documents/GitHub/dfdc_deepfake_challenge/processor/combine_metadata.json', 'w')
json.dump(train_data, fp)
