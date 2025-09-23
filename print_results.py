#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Barbara Ortiz
# DATE CREATED: 17/09/25                                 
# REVISED DATE: 23/09/25 

# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
Prints summary results of the image classification and optionally
lists incorrectly classified dogs and dog breeds.

Parameters:
  results_dic (dict): Dictionary with key = image filename and value = list:
      idx 0 = pet image label (string)
      idx 1 = classifier label (string)
      idx 2 = match flag (1/0)
      idx 3 = pet 'is-a-dog' flag (1/0)
      idx 4 = classifier 'is-a-dog' flag (1/0)
  results_stats_dic (dict): Dictionary containing counts and percentages
      of classification results (keys start with 'n' for counts and 'pct' for percentages)
  model (str): CNN model used for classification ('resnet', 'alexnet', 'vgg')
  print_incorrect_dogs (bool): If True, prints incorrectly classified dog images
  print_incorrect_breed (bool): If True, prints incorrectly classified dog breeds

Returns:
  None
"""
    
    # Template Header 
    print("\n\n*** Results with the CNN model=", model.upper(), "***")

    # Totals
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dogs', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N No Dogs', results_stats_dic['n_notdogs_img']))

    # Percentages
    print("\n Percentages")
    for key in results_stats_dic:
        if key.startswith("pct_"):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))

    #  Misclassified dogs 
    if (print_incorrect_dogs and
        ( (results_stats_dic['n_correct_dogs'] +
            results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images'] )):
        print("\nMisclassifications of dogs:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Archive: {:>25} | Label: {:>15} | Sorter: {:>15}"
                      .format(key, results_dic[key][0], results_dic[key][1]))

    # Misclassified races 
    if (print_incorrect_breed and
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nMisclassifications of races:")
        for key in results_dic:
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):
                print("Archive: {:>25} | Label: {:>15} | Sorter: {:>15}"
                      .format(key, results_dic[key][0], results_dic[key][1]))
    
                
