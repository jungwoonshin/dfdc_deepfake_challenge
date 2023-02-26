#!/bin/bash

ROOT_DIR=$1
NUM_GPUS=$2
python -u -m torch.distributed.launch --nproc_per_node=$NUM_GPUS --master_port 9901 training/pipelines/train_classifier_vessl.py \
 --distributed --config configs/b7.json --freeze-epochs 0 --test_every 1 --opt-level O1 --label-smoothing 0.01 --folds-csv folds.csv   --fold 0 --seed 111 --data-dir $ROOT_DIR --prefix b7_111_ > logs/b7_111
