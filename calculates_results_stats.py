#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Barbara Ortiz
# DATE CREATED: 17/09/25                                 
# REVISED DATE: 23/09/25 

def calculates_results_stats(results_dic):
    """
Calculates summary statistics from the classification results.

Parameters:
  results_dic - Dictionary with key = image filename and value = list:
      idx 0 = pet image label (string)
      idx 1 = classifier label (string)
      idx 2 = 1/0 match flag (int)
      idx 3 = 1/0 pet image 'is-a-dog' flag (int)
      idx 4 = 1/0 classifier 'is-a-dog' flag (int)

Returns:
  results_stats_dic - Dictionary with counts and percentages:
      keys start with 'n' for counts and 'pct' for percentages.
"""
        

    # Initialize statistics dictionary
    results_stats_dic = dict()

    # Initialize counters
    n_images = len(results_dic)
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0

    # Loop through the results dictionary
    for key in results_dic:

        # Labels
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        match = results_dic[key][2]
        is_dog = results_dic[key][3]
        classifier_is_dog = results_dic[key][4]

        # Total matches 
        if match == 1:
            n_match += 1

        # Image is a dog
        if is_dog == 1:
            n_dogs_img += 1

            # Correctly classified as a dog
            if classifier_is_dog == 1:
                n_correct_dogs += 1

                # Also the race matches
                if match == 1:
                    n_correct_breed += 1

        # Image is not a dog
        else:
            n_notdogs_img += 1

            # Correctly classified as not a dog
            if classifier_is_dog == 0:
                n_correct_notdogs += 1

    # Save counts
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed

    # Calculate percentages
    results_stats_dic['pct_match'] = (n_match / n_images) * 100.0
    results_stats_dic['pct_correct_dogs'] = (n_correct_dogs / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    results_stats_dic['pct_correct_breed'] = (n_correct_breed / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    results_stats_dic['pct_correct_notdogs'] = (n_correct_notdogs / n_notdogs_img) * 100.0 if n_notdogs_img > 0 else 0.0

    return results_stats_dic
   
