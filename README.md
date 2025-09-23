# 🐾 Pet Image Classification with Convolutional Neural Networks (CNN)

This project is part of the AWS AI & ML Scholarship Program — Future AWS AI Scientist track.
The goal of the project is to build an image classification pipeline using pre-trained Convolutional Neural Networks (CNNs) (ResNet, AlexNet, VGG) to identify whether images contain dogs, and if so, classify their breed. It was developed step by step by implementing functions, building a complete image classification pipeline.

-----

## 📋 Key Features

* Classifies pet images using pretrained CNN models.
* Compares predictions against ground truth labels derived from filenames.
* Adjusts results to determine whether an image is of a dog or not using a reference file (dognames.txt).
* Computes performance statistics: accuracy on dogs, non-dogs, and dog breeds.
* Runs with different CNN architectures (resnet, alexnet, vgg) and compares performance.
* Classifies user-uploaded images stored in the uploaded_images folder.

-----

## 🗂️ Project Structure 

AWS-Proy1/
│
├── check_images.py               # Main program
├── get_input_args.py              # TODO 1 - Command line argument parser
├── get_pet_labels.py              # TODO 2 - Extract labels from filenames
├── classify_images.py             # TODO 3 - Run classification with CNN
├── adjust_results4_isadog.py      # TODO 4 - Mark results as dog/not dog
├── calculates_results_stats.py    # TODO 5 - Compute statistics
├── print_results.py               # TODO 6 - Print summary
│
├── dognames.txt                   # List of valid dog breeds
├── imagenet1000_clsid_to_human.txt # ImageNet labels
│
├── pet_images/                    # Test dataset (40 images)
├── uploaded_images/               # User-uploaded images
│
├── resnet_pet-images.txt          # Results using ResNet
├── alexnet_pet-images.txt         # Results using AlexNet
├── vgg_pet-images.txt             # Results using VGG

-----

## ⚙️ Installation

1. Clone the repository:

````
git clone https://github.com/yourusername/pet-image-classification.git
cd pet-image-classification
````
2.(Optional but recommended) Create a virtual environment:
````
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
````
3. Install dependencies:
```` 
pip install torch torchvision pillow
````

-----

## ▶️ Usage

* Run with the default test images:
```` 
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
````
* Run with uploaded images: 
```` 
python check_images.py --dir uploaded_images/ --arch resnet --dogfile dognames.txt
````
* Batch execution (Windows example): 
Create and run run_models_batch.bat:
```` 
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg     --dogfile dognames.txt > vgg_pet-images.txt
````
-----

## 📊 Expected Results

The program prints:

* Total number of images
* Number of dog images
* Number of non-dog images
* Correct classification percentages:
    - Dogs
    - Breeds
    - Not-a-dog
* (Optional) Incorrect classifications

Example output:
```` 
*** Results Summary for CNN Model Architecture VGG ***
N Images: 40
N Dog Images: 30
N Not-Dog Images: 10

% Correct Dogs: 100.0
% Correct Breed: 90.0
% Correct 'Not-a' Dog: 100.0
````
-----

## 🖼️ Uploaded Images Classification

Four images were tested in uploaded_images/:

* Dog_01.jpg
* Dog_02.jpg (mirrored version of Dog_01)
* Cat_01.jpg
* Coffee_mug_01.jpg

Each model (resnet, alexnet, vgg) was executed, and results were saved in:

* resnet_uploaded-images.txt
* alexnet_uploaded-images.txt
* vgg_uploaded-images.txt

-----

## ✅ Rubric Criteria Met

This project fulfills all rubric criteria:

* Runtime measurement included.
* Command line arguments implemented (--dir, --arch, --dogfile).
* Pet labels correctly extracted from filenames.
* Classification with pretrained CNNs.
* Identification of dogs vs non-dogs.
* Statistics and accuracy percentages calculated.
* Results printing and optional misclassification reporting.
* Support for classifying uploaded images.

-----
