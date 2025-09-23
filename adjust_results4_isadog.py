#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Barbara Ortiz
# DATE CREATED: 17/09/25                                 
# REVISED DATE: 23/09/25  

def adjust_results4_isadog(results_dic, dogfile):
    """
    Updates the results dictionary to indicate whether the classifier
    and the pet image label correspond to a dog or not.

    Args:
        results_dic (dict): Dictionary with:
            key (str): image filename
            value (list):
                index 0 (str): pet image label
                index 1 (str): classifier label
                index 2 (int): 1/0 match indicator (1 = match, 0 = no match)
                index 3 (int): added by this function, 1/0 indicating if
                               pet image 'is-a' dog (1) or 'is-NOT-a' dog (0)
                index 4 (int): added by this function, 1/0 indicating if
                               classifier labels image 'as-a' dog (1) or
                               'as-NOT-a' dog (0)
        dogfile (str): Path to a text file containing dog names (lowercase).
                       One dog name per line. Classifier labels may contain
                       multiple names separated by commas.

    Returns:
        None: results_dic is updated in place.
    """

    # Read dognames.txt in a dictionary
    dognames_dic = dict()
    with open(dogfile, "r") as f:
        for line in f:
            name = line.strip().lower()
            if name not in dognames_dic:
                dognames_dic[name] = 1
            else:
                print(f"**Warning: duplicate name in dognames.txt: {name}")

    # Loop through results_dic 
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        pet_isdog = 1 if pet_label in dognames_dic else 0

        # The classifier can return multiple labels separated by commas
        classifier_labels = [lab.strip().lower() for lab in classifier_label.split(",")]
        classifier_isdog = 0
        for lab in classifier_labels:
            if lab in dognames_dic:
                classifier_isdog = 1
                break

        # Add both values ​​to the results list
        results_dic[key].extend([pet_isdog, classifier_isdog])         
 
