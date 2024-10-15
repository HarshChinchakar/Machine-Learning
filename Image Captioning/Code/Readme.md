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

```python
# Feature extraction using ResNet-50
from keras.applications.resnet50 import ResNet50
from keras.models import Model

# Load ResNet50 model pre-trained on ImageNet
base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)

from keras.layers import Input, LSTM, Embedding, Dense

# Define the LSTM model architecture
input_image_features = Input(shape=(2048,))
input_text = Input(shape=(max_length,))
embedding_layer = Embedding(vocab_size, embedding_dim)(input_text)
lstm_layer = LSTM(256)(embedding_layer)
output_layer = Dense(vocab_size, activation='softmax')(lstm_layer)

# Combine image features and LSTM output
caption_model = Model(inputs=[input_image_features, input_text], outputs=output_layer)
caption_model.compile(loss='categorical_crossentropy', optimizer='adam')

from keras.layers import Add, Activation, RepeatVector

# Attention mechanism for focusing on parts of the image
attention = Add()([image_features, lstm_output])
attention = Activation('softmax')(attention)
context = RepeatVector(max_length)(attention)

# Train the model with training images and their captions
caption_model.fit([train_image_features, train_captions], train_targets, epochs=20, batch_size=64, validation_split=0.2)

# Generate caption for a given image
def generate_caption(image):
    features = extract_features(image)
    input_sequence = [start_token]
    for _ in range(max_length):
        prediction = caption_model.predict([features, input_sequence])
        next_word = decode_prediction(prediction)
        input_sequence.append(next_word)
        if next_word == end_token:
            break
    return ' '.join(input_sequence)
