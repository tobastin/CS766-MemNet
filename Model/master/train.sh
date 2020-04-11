#!/bin/bash

output_dir="model_output_"`date +"%Y%m%d%H%M%S"`
# output_dir="model_output" # test
phase="train"
training_set="./datasets/tfrecords/VOC0712.tfrecords"
batch_size=2 # MemNet_M6R6, batch_size is 1.
training_steps=3000
summary_steps=10
checkpoint_steps=100
save_steps=100


python3 main.py --output_dir="$output_dir" \
               --phase="$phase" \
               --training_set="$training_set" \
               --batch_size="$batch_size" \
               --training_steps="$training_steps" \
               --summary_steps="$summary_steps" \
               --checkpoint_steps="$checkpoint_steps" \
               --save_steps="$save_steps"
