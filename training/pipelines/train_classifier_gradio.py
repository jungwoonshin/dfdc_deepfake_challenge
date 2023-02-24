import gradio as gr
import argparse
import os
import re
import time

import torch
import pandas as pd

import os, sys
root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
sys.path.append(root_folder)
from kernel_utils import VideoReader, FaceExtractor, confident_strategy, predict_on_video_set
from training.zoo.classifiers import DeepFakeClassifier

    
    
def predict(video_index):
    video_index = int(video_index)
    
    frames_per_video = 32
    video_reader = VideoReader()
    video_read_fn = lambda x: video_reader.read_frames(x, num_frames=frames_per_video)
    face_extractor = FaceExtractor(video_read_fn)
    input_size = 380
    strategy = confident_strategy
    
    test_videos = sorted([x for x in os.listdir(args.test_dir) if x[-4:] == ".mp4"])[video_index]
    print(f"Predicting {video_index} videos")
    predictions = predict_on_video_set(face_extractor=face_extractor, input_size=input_size, models=models,
                                       strategy=strategy, frames_per_video=frames_per_video, videos=test_videos,
                                       num_workers=6, test_dir=args.test_dir)
    return predictions

def get_args_models():
    parser = argparse.ArgumentParser("Predict test videos")
    arg = parser.add_argument
    arg('--weights-dir', type=str, default="weights", help="path to directory with checkpoints")
    arg('--models', type=str, default='classifier_DeepFakeClassifier_tf_efficientnet_b7_ns_1_best_dice', help="checkpoint files")  # nargs='+',
    arg('--test-dir', type=str, default='test_dataset', help="path to directory with videos")
    arg('--output', type=str, required=False, help="path to output csv", default="submission.csv")
    args = parser.parse_args()

    models = []
    # model_paths = [os.path.join(args.weights_dir, model) for model in args.models]
    model_paths = [os.path.join(args.weights_dir, args.models)]
    for path in model_paths:
        model = DeepFakeClassifier(encoder="tf_efficientnet_b7_ns").to("cuda")
        print("loading state dict {}".format(path))
        checkpoint = torch.load(path, map_location="cpu")
        state_dict = checkpoint.get("state_dict", checkpoint)
        model.load_state_dict({re.sub("^module.", "", k): v for k, v in state_dict.items()}, strict=True)
        model.eval()
        del checkpoint
        models.append(model.half())
    return args, models

if __name__ == '__main__':
    global models, args
    stime = time.time()
    print("Elapsed:", time.time() - stime)
    args, models = get_args_models()
    demo = gr.Interface(fn=predict, inputs="video", outputs="text")
    demo.launch()  

