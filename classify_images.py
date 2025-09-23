#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Barbara Ortiz
# DATE CREATED: 17/09/25                                 
# REVISED DATE: 23/09/25  

# Imports classifier function for using CNN to classify images 
from classifier import classifier 
from os import path

def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images using a specified CNN model, compares the
    predicted labels with the true pet labels, and updates results_dic
    with the classifier label and a match indicator.

    Args:
        images_dir (str): Path to the folder of images.
        results_dic (dict): Dictionary with:
            key = image filename
            value[0] = pet image label
            value[1] = classifier label (added by this function)
            value[2] = match indicator (1 if labels match, 0 otherwise).
        model (str): CNN model architecture: 'resnet', 'alexnet', or 'vgg'.

    Returns:
        None: results_dic is modified in place.
    """
        # Iterate over each image in results_dic
    for filename in results_dic:

        # Create full path to the image
        image_path = path.join(images_dir, filename)

        # Get the classifier label
        classifier_label = classifier(image_path, model)

        # Normalize (lowercase and remove trailing spaces)
        classifier_label = classifier_label.lower().strip()

        # Add the classifier tag to that key's list
        # (the pet tag already exists in [0])
        results_dic[filename].append(classifier_label)

        # Determine if there is a match
        pet_label = results_dic[filename][0]

        # If pet_label is contained within classifier_label → match=1
        if pet_label in classifier_label:
            results_dic[filename].append(1)
        else:
            results_dic[filename].append(0)