""" Train a new network on a data set with train.py
    Basic usage: python train.py data_directory
    Prints out training loss, validation loss, and validation accuracy as the network trains

Options:
Set directory to save checkpoints: python train.py data_dir --save_dir save_directory
Choose architecture: python train.py data_dir --arch "vgg13"
Set hyperparameters: python train.py data_dir --learning_rate 0.01 --hidden_units 512 --epochs 20
Use GPU for training: python train.py data_dir --gpu
"""
# Importing all the modules
import torch
from torch import nn
from torch import optim
from torchvision import datasets, transforms, models

import json
import sys

import numpy as np
import argparse

# Create object
parser = argparse.ArgumentParser(description='Predict Flower Name')

parser.add_argument('-s', '--save_dir',     type=str,    metavar='', required=False, default='checkpoint.pth',
                    help='Save_directory')
parser.add_argument('-a', '--arch',         type=str,    metavar='', required=False, default='vgg19',
                    help='Choose model architecture vgg19 or vgg16')
parser.add_argument('-l', '--learning_rate', type=float, metavar='', required=False, default= 0.002,
                    help='Learning rate')
parser.add_argument('-H', '--hidden_units', type=int,    metavar='', required=False, default= 4096,
                    help='Number of hiddent Units')
parser.add_argument('-e', '--epochs',       type=int,    metavar='', required=False, default= 5,
                    help='Number of epochs')
parser.add_argument('--gpu', action='store_true', help='Boolean flag to use GPU for inference')
args = parser.parse_args()

print(f"save_dir:      {args.save_dir}")
print(f"arch:          {args.arch}")
print(f"learning_rate: {args.learning_rate}")
print(f"hidden_units:  {args.hidden_units}")
print(f"epochs:        {args.epochs}")

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

if __name__ == "__main__":

    checkpoint_name = args.save_dir
    learning_rate   = args.learning_rate
    hidden_units    = args.hidden_units
    arch            = args.arch
    epochs          = args.epochs

    # device    = torch.device("cuda" if torch.cuda.is_available() else "cpu")   # Use GPU if it's available
    device = "cpu"
    if args.gpu:
        device = "cuda"

    data_dir  = 'flowers'
    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'
    test_dir  = data_dir + '/test'

    mean = np.array([0.485, 0.456, 0.406])
    std  = np.array([0.229, 0.224, 0.225])
    train_transforms = transforms.Compose([transforms.RandomRotation(30),
                                          transforms.RandomResizedCrop(224),
                                          transforms.RandomHorizontalFlip(),
                                          transforms.CenterCrop(224),
                                          transforms.ToTensor(),
                                          transforms.Normalize(mean, std)])

    valid_transforms = transforms.Compose([transforms.Resize(256),
                                           transforms.CenterCrop(224),
                                           transforms.ToTensor(),
                                           transforms.Normalize(mean, std)])
    test_transforms  = transforms.Compose([transforms.Resize(256),
                                           transforms.CenterCrop(224),
                                           transforms.ToTensor(),
                                           transforms.Normalize(mean, std)])

    # Load the datasets with ImageFolder
    trainset = datasets.ImageFolder(train_dir, transform=train_transforms)
    validset = datasets.ImageFolder(valid_dir, transform=valid_transforms)
    testset  = datasets.ImageFolder(test_dir,  transform=test_transforms)

    # Using the image datasets and the trainforms, define the dataloaders
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
    validloader = torch.utils.data.DataLoader(validset, batch_size=32, shuffle=False)
    testloader  = torch.utils.data.DataLoader(testset,  batch_size=32, shuffle=False)

    with open('cat_to_name.json', 'r') as f:
        cat_to_name = json.load(f)

    # Setup the model
    print(f"Loading the model: {arch}")
    if arch == 'vgg19':
        model = models.vgg19(pretrained=True)
    elif arch == 'vgg16':
        model = models.vgg16(pretrained=True)
    else:
        print(f"*** ERROR *** model architecture is {arch} => should be vgg19 or vgg16")
        sys.exit(1)

    for param in model.features.parameters():    # freeze convolution weights
        param.requires_grad = False

    # Setup the calssifier
    input_size   = 25088
    output_size  = 102
    model.classifier = nn.Sequential(nn.Linear(input_size, hidden_units),
                                     nn.ReLU(),
                                     nn.Linear(hidden_units, output_size),
                                     nn.LogSoftmax(dim=1))
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), lr=learning_rate)
    model.to(device)

    # Key parameters
    steps  = 0
    running_loss = 0       # Loss for a group of steps defined by print every
    print_every  = 100
    train_lost_history = []
    model.train()          # Turn the training mode

    for epoch in range(epochs):
        print(f"Starting epoch:{epoch+1} with {len(trainloader)} steps")
        for inputs, labels in trainloader:
            steps += 1

            # Move input and label tensors to the default device
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            logps = model.forward(inputs)
            loss = criterion(logps, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            train_lost_history.append(loss.item())

            # Check testing accuracy from time to time
            if steps % print_every == 0:
                valid_loss, accuracy = valid_model(model, validloader, criterion, optimizer)
                print(f"Epoch {epoch+1}/{epochs}, Step {steps}.. "
                      f"Train loss: {running_loss/print_every:.3f}.. "
                      f"Valid loss: {valid_loss/len(validloader):.3f}.. "
                      f"Valid accuracy: {100*accuracy/len(validloader):.2f}%")
                model.train()      # Turn model back into learning mode
                running_loss = 0

    # Save the checkpoint
    model.class_to_idx = trainset.class_to_idx
    print("Our model: \n\n", model, '\n')
    print("The state dict keys: \n\n", model.state_dict().keys())

    state = {'arch': arch,
             'hidden_units': hidden_units,
             'epochs': epochs,
             'l_rate': learning_rate,
             'class_to_idx': model.class_to_idx,
             'state_dict': model.state_dict(),
             'optimizer':  optimizer.state_dict()}

    torch.save(state, checkpoint_name)



