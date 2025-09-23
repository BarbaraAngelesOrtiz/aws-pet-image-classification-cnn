#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Barbara Ortiz
# DATE CREATED: 17/09/25                                 
# REVISED DATE: 23/09/25  

# Imports python modules
import argparse

def get_input_args():
    """
Parses command line arguments for the program using argparse.

Arguments:
  --dir     Path to the image folder (default: 'pet_images')
  --arch    CNN model architecture: resnet, alexnet, vgg (default: 'vgg')
  --dogfile Text file with dog names (default: 'dognames.txt')

Returns:
  argparse.Namespace object with the parsed arguments.
"""

    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # command line arguments using add_argument() from ArguementParser method
    parser.add_argument('--dir', 
                        type=str, 
                        default='pet_images',
                        help='Path to the folder with the images')

    parser.add_argument('--arch', 
                        type=str, 
                        default='vgg',
                        help='CNN model to use (e.g. vgg, resnet, alexnet)')

    parser.add_argument('--dogfile', 
                        type=str, 
                        default='dognames.txt',
                        help='Text file with dog breed names')
    
    
    return parser.parse_args()
