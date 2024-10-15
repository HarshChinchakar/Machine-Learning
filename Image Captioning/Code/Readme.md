# Image Captioning System Using ResNet-50 and LSTM

## Overview
This project implements an image captioning system that uses a combination of ResNet-50 for image feature extraction and LSTM for generating natural language captions. The goal is to automatically generate descriptive captions for images by leveraging deep learning techniques. 

## Objective
The objective of this project is to create a robust image captioning system that can interpret images and generate accurate and contextually relevant captions, providing a seamless way to bridge the gap between visual content and descriptive text.

## Key Features
- Uses ResNet-50, a powerful convolutional neural network, for extracting visual features from images.
- Employs an LSTM model to generate captions based on extracted image features.
- Supports the COCO 2017 and Flickr8k datasets for training and evaluation.
- Incorporates a soft attention mechanism for improved focus on different parts of an image.
- Achieves high BLEU scores for evaluation, indicating the quality of generated captions.

## Model Architecture
The image captioning model is designed as follows:
1. **Encoder**: Uses ResNet-50 (pre-trained on ImageNet) as an encoder to extract deep visual features from the input images.
2. **Decoder**: An LSTM model is used as a decoder, taking the extracted features as input and generating a sequence of words to form a caption.
3. **Attention Mechanism**: A soft attention mechanism is applied to focus on specific parts of the image during caption generation, enhancing the relevance of generated text.

## Preprocessing
1. **Image Processing**: Images are resized to 224x224 pixels using OpenCV (`cv2`) and normalized to have values between 0 and 1.
2. **Text Tokenization**: Captions are tokenized into words and mapped to integer indices to build a vocabulary.
3. **Caption Encoding**: The tokenized words are converted into integer sequences for input into the LSTM model.
4. **Hyperparameter Tuning**: Learning rate, batch size, and optimizers (Adam and SGD) are fine-tuned for optimal model performance.

## Training
- **Dataset**: The model is trained on the COCO 2017 and Flickr8k datasets.
- **Feature Extraction**: ResNet-50 extracts features from the images, which are used by the LSTM for sequence generation.
- **Training Strategy**: Includes regularization techniques such as dropout and early stopping to prevent overfitting.
- **Fine-Tuning**: The pre-trained ResNet-50 is fine-tuned, with adjustments made to the fully connected layers for caption generation.

## Code Overview
Here is a step-by-step breakdown of the core code:

### 1. Feature Extraction using ResNet-50
The ResNet-50 model is used to extract features from images. The model is pre-trained and modified to output a rich representation of image features.

```python
# Feature extraction using ResNet-50
from keras.applications.resnet50 import ResNet50
from keras.models import Model

# Load ResNet50 model pre-trained on ImageNet
base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)
