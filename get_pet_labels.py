#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Barbara Ortiz
# DATE CREATED: 17/09/25                                 
# REVISED DATE: 23/09/25  

# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
Creates a dictionary of pet labels based on image filenames.

Parameters:
  image_dir (str): Path to the folder containing pet images.

Returns:
  results_dic (dict): Dictionary with:
      key = image filename
      value = list containing:
          index 0 = pet image label (string, lowercase, stripped of whitespace)
"""

    filename_list = listdir(image_dir)
    results_dic = dict()

    # Iterate over each file name
    for filename in filename_list:
        
        if filename.startswith('.'):
            continue

        # Convert to lowercase
        lower_filename = filename.lower()

        # Separate by "_"
        word_list = lower_filename.split("_")

        # Create label with only alphabetical words
        pet_name = ""
        for word in word_list:
            if word.isalpha():
                pet_name += word + " "

        # Remove leading/trailing spaces
        pet_name = pet_name.strip()

        # Add to dictionary if it doesn't exist yet
        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print("** Warning: The key=", filename, "already exists in results_dic")
    return results_dic
