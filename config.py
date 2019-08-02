import numpy as np
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # sets device for model and PyTorch tensors

input_size = 512
annotation_file = 'data/COCO_Text.json'
max_image_large_side = 1280  # max image size of training
max_text_size = 800  # if the text in the input image is bigger than this, then we resize the image according to this
min_text_size = 10  # if the text size is smaller than this, we ignore it during training
min_crop_side_ratio = 0.1  # when doing random crop from input image, the min length of min(H, W)
geometry = 'RBOX'  # which geometry to generate, RBOX or QUAD
background_ratio = 3. / 8
random_scale = np.array([0.5, 1, 2.0, 3.0])
epsilon = 1e-8

train_ratio = 0.9
num_train = 43686
num_val = 10000
num_test = 10000

# Training parameters
num_workers = 4  # for data-loading
grad_clip = 5.  # clip gradients at an absolute value of
print_freq = 10  # print training/validation stats  every __ batches
checkpoint = None  # path to checkpoint, None if none
