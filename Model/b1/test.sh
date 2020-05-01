#!/bin/bash


#model_output_pretrained/checkpoint/./modelPreTrained
output_dir="model_output_jpgdeblock"
phase="test"
# modify testing_set. Image has already added noise.
# testing_set="./datasets/test/*.jpg" # single image.
testing_set="/home/apurbaa_juit/MemNet-Tensorflow-GPU/data/Set12_Quality10/*.jpg" # multiple images.
#testing_set="/home/apurbaa_juit/MemNet-Tensorflow-GPU/datasets/VOC0712_Quality10/VOC2007/000005.jpg"

#testing_set="./datasets/Set2TestNoise/*.jpg"
checkpoint="model-2901"

python3 main.py --output_dir="$output_dir" \
               --phase="$phase" \
               --testing_set="$testing_set" \
               --checkpoint="$checkpoint"
