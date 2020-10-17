""" Predict flower name from an image with predict.py along with the probability of that name.
    That is, you'll pass in a single image /path/to/image and
    return the flower name and class probability.

Basic usage: python predict.py /path/to/image checkpoint
Options:
Return top KK most likely classes:         python predict.py input checkpoint --top_k 3
Use a mapping of categories to real names: python predict.py input checkpoint --category_names cat_to_name.json
Use GPU for inference:                     python predict.py input checkpoint --gpu
"""
# Importing all the modules
import torch
from torch import nn
from torch import optim
from torchvision import datasets, transforms, models

import json
import os

from PIL import Image
import numpy as np
import argparse

# Create object
parser = argparse.ArgumentParser(description='Predict Flower Name')
parser.add_argument('-n', '--image_no', metavar='', type=int, help='Path to image')
parser.add_argument('-p', '--image', metavar='', type=str, help='Path to image')
#parser.add_argument('-p', '--image', metavar='in-file', type=argparse.FileType('rt'), help='Path to image')
parser.add_argument('-i', '--input', type=str, metavar='', default='checkpoint.pth', help='Path to checkpoint')
parser.add_argument('-k', '--top_k', type=int, metavar='', required=False, default=5, help='Number of top K classes to return')
parser.add_argument('-c', '--category_names', type=str, metavar='', required=False, default= 'cat_to_name.json', help='Jason file to map categories to real names')
parser.add_argument('--gpu', action='store_true', help='Boolean flag to use GPU for inference')
args = parser.parse_args()

print(f"image_no: {args.image_no}")
print(f"image path: {args.image}")
print(f"input checkpoint: {args.input}")
print(f"top_k: {args.top_k}")
print(f"category_names: {args.category_names}\n")

def load_checkpoint(filepath, model_architecture):
    """ Creates a model based on the saved checkpoint dictionary.
        It then loads the model state dictionary."""
    if torch.cuda.is_available():
        map_location=lambda storage, loc: storage.cuda()
    else:
        map_location='cpu'

    checkpoint    = torch.load(filepath, map_location=map_location)
    arch          = checkpoint['arch']
    hidden_units  = checkpoint['hidden_units']
    learning_rate = checkpoint['l_rate']
    epochs        = checkpoint['epochs']
    print(f"Loading the model: {arch}")

    if arch == 'vgg19':
        model = models.vgg19(pretrained=True)
    elif arch == 'vgg16':
        model = models.vgg16(pretrained=True)
    else:
        print(f"*** ERROR *** model architecture is {arch} => should be vgg19 or vgg16")
        sys.exit(1)

    for param in model.parameters():            # freeze parameters
        param.requires_grad = False

    model.class_to_idx = checkpoint['class_to_idx']

    # Create the clasifier again
    input_size  = 25088
    output_size = 102

    model.classifier = nn.Sequential(nn.Linear(input_size, hidden_units),
                                     nn.ReLU(),
                                     nn.Linear(hidden_units, output_size),
                                     nn.LogSoftmax(dim=1))

    model.load_state_dict(checkpoint['state_dict'])

    return model

def valid_model(model, loader, criterion, optimizer):
    """ Test the accuracy of the model.
        Parameters:
        ===========
        inputs:  object - model, loader, criterion, optimizer
        outputs: float - loss, accuracy
    """
    valid_loss, accuracy = 0, 0
    model.eval()           # Turn model into "inference mode"

    with torch.no_grad():
        for idx, (inputs, labels) in enumerate(loader):
            inputs, labels = inputs.to(device), labels.to(device)

            logps = model.forward(inputs)
            batch_loss = criterion(logps, labels)
            valid_loss += batch_loss.item()

            # Calculate accuracy
            ps = torch.exp(logps)
            top_p, top_class = ps.topk(1, dim=1)
            equals = top_class == labels.view(*top_class.shape)
            accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

    model.train()      # Turn model back into learning mode
    return valid_loss, accuracy

def process_image(img):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model.
        Paremeters:
        ============
        img:     single PIL image object
        returns: single image tensor [3, width, height]
    '''

    # These are the ImageNet normalizing mean and std
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])

    # Create a transformation that converts PIL to Tensor and normalizes the image
    image_transform = transforms.Compose([transforms.Resize(256),
                                          transforms.CenterCrop(224),
                                          transforms.ToTensor(),
                                          transforms.Normalize(mean, std)])
    pil_to_tensor = image_transform(img)

    return pil_to_tensor

def predict(image_path, model, top_k=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
        Parameters:
        ===========
        image_path: string - location of the image
        model:      object - model
        top_k:      integer - number of class we want to review
        returns:
        =========
        top_p:      list of float - probabilities
        top_class:  list of integers - index of the classes
    '''
    model.to(device);
    model.eval()
    img = Image.open(image_path)
    img_tensor = process_image(img)
    img_tensor.unsqueeze_(0)                    # Ensures the 1st argument of tensor is the batchsize
    img_tensor = img_tensor.to(device)

    logps = model.forward(img_tensor)           # Forward pass
    ps    = torch.exp(logps)                    # Convert log to get probabilities

    top_p, top_class = ps.topk(top_k, dim=1)    # Get the top K probabilities and their index
    return top_p, top_class

def get_image_paths(flower_number):
    """ Helper to find flower images in the workspace.
        Parameters:
        ===========
        flower_number: string
        outputs:       list of strings
    """

    list_images = os.listdir('flowers/test/' + flower_number)
    base        = 'flowers/test/'
    image_paths = [base + flower_number+'/'+ x for x in list_images]
    return image_paths

def class_to_name(classes, mapping, cat_to_name):
    """ Convert the classes to flower names.
        Parameters:
        ===========
        classes:     list of str - index of the top 5 classes
        mapping:     dict - maps index to flower numbers (the key)
        cat_to_name: dict - maps the flower numbers to names
        returns:     list str - names of flowers
        """

    class_values = classes.numpy().squeeze()                    # convert to numpy and remove extra []
    keys = []
    for value in class_values:                                  # Find the matching key for all the classes
        #print(value)
        tmp = [k for k,v in mapping.items() if v == value][0]   # Need the [0] to remove the list
        keys.append(tmp)

    names = [cat_to_name[key] for key in keys]                  # Convert into names
    return names

if __name__ == '__main__':

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")   # Use GPU if it's available
    print(f"Working on {device}")
    with open(args.category_names, 'r') as f:
        cat_to_name = json.load(f)

    """flower_number = str(args.image_no)
    print(f"Flower number: {flower_number}")
    image_paths = get_image_paths(flower_number)
    image_path = image_paths[0]    """
    image_path = args.image

    checkpoint_name = args.input
    print(f"Loading: {checkpoint_name}")
    model = load_checkpoint(checkpoint_name, 'vgg19')
    mapping = model.class_to_idx
    print(model)

    print("*** Starting Predict ***")
    probs, classes = predict(image_path, model, args.top_k)

    probs = probs.cpu()
    classes = classes.cpu()
    # print(f"Probs: {type(probs)} {len(probs)}")
    # print(f"Probs: {type(classes)} {len(classes)}")
    probs =  probs.detach().numpy().squeeze()                # Need to convert tensor to array and remove extra []
    #class_values = classes.numpy().squeeze()                # convert to numpy then take the 1st item of the 1st vector
    #print(probs, classes)

    """key = [k for k,v in mapping.items() if v == class_value][0]
    value = cat_to_name[key]"""

    flowers = class_to_name(classes, mapping, cat_to_name)
    for prob, flower in zip(probs, flowers):
        print(f"flower: {flower}, prop: {prob}")

