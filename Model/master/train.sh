#!/bin/bash

output_dir="model_output_"`date +"%Y%m%d%H%M%S"`
# output_dir="model_output" # test
phase="train"
training_set="/home/apurbaa_juit/CS766-MemNet/datasets/tfrecords/snow.tfrecords"
batch_size=1 # MemNet_M6R6, batch_size is 1.
training_steps=100001
summary_steps=50
checkpoint_steps=1000
save_steps=500


python3 main.py --output_dir="$output_dir" \
               --phase="$phase" \
               --training_set="$training_set" \
               --batch_size="$batch_size" \
               --training_steps="$training_steps" \
               --summary_steps="$summary_steps" \
               --checkpoint_steps="$checkpoint_steps" \
               --save_steps="$save_steps"
