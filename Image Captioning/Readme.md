# Image Captioning System Using ResNet-50 and LSTM

## Table of Contents
- [Introduction](#introduction)
- [System Overview](#system-overview)
- [Model Architecture](#model-architecture)
- [Datasets Used](#datasets-used)
- [Preprocessing](#preprocessing)
- [Training and Fine-Tuning](#training-and-fine-tuning)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [Future Scope](#future-scope)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This repository contains the implementation of an **Image Captioning System** that uses the **ResNet-50** architecture combined with a **Long Short-Term Memory (LSTM)** network. The system generates informative descriptions for photographs by automatically analyzing and understanding the content of the image.

### Key Features:
- Combines **ResNet-50** for feature extraction and **LSTM** for caption generation.
- Uses **Soft Attention** to focus on specific regions of an image while generating captions.
- Trained on **Flickr8k** and **COCO 2017** datasets.
- Supports metrics like **BLEU** to evaluate the quality of generated captions.

## System Overview

The image captioning system leverages a pre-trained **ResNet-50** model for extracting high-level image features. These features are then passed to an **LSTM** network, which generates human-like captions. Additionally, the system incorporates a **Soft Attention Mechanism** to dynamically focus on different parts of the image during caption generation.

## Model Architecture

### ResNet-50
- **ResNet-50** is a deep **Convolutional Neural Network (CNN)** that automatically learns a hierarchical representation of the image.
- This model extracts feature maps, which are used as input to the caption generation process.
  
### LSTM Network
- The **LSTM** is used as a decoder to generate captions.
- It processes the sequence of image features and generates the next word of the caption.
  
### Soft Attention Mechanism
- The **Soft Attention** mechanism highlights specific features of the image, allowing the model to focus on different areas while generating each word in the caption.

## Datasets Used

- **Flickr8k Dataset**: Contains 8,000 images, each with 5 different captions.
- **COCO 2017 Dataset**: Contains over 118,000 images with corresponding captions.

## Preprocessing

1. **Image Preprocessing**: 
   - Images are resized to **224x224 pixels** for uniformity.
   - Pixel values are normalized to fall within the range `[0, 1]`.
   
2. **Text Preprocessing**:
   - Captions are tokenized and converted into integer sequences for training.
   - A vocabulary is created based on the unique words in the captions.

## Training and Fine-Tuning

- The system uses a pre-trained **ResNet-50** model with frozen convolutional layers. The fully connected layers are modified to generate captions.
- Fine-tuning of hyperparameters:
  - **Batch size**: [32, 64, 128]
  - **Learning rate**: [0.001, 0.01, 0.1]
  - **Optimizers**: Adam, SGD
- Regularization techniques like **dropout** and **early stopping** were used to prevent overfitting.

## Evaluation Metrics

The performance of the model is evaluated using **BLEU** scores:
- **BLEU-1**: Measures unigram precision.
- **BLEU-2**: Measures bigram precision.
- **BLEU-3**: Measures trigram precision.
- **BLEU-4**: Measures 4-gram precision.

## Results

The system achieved the following BLEU scores on the **COCO 2017 dataset**:
| Metric   | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 |
|----------|--------|--------|--------|--------|
| **AICRL-ResNet50** | 0.672  | 0.511  | 0.421  | 0.330  |

On the **Flickr8k dataset**, using **beam search** with `k=3`, the BLEU-4 score was **0.493**.

## Future Scope

- **Integration with IoT Devices**: The captioning system can be integrated with IoT devices like smart glasses to help visually impaired individuals by providing real-time audio descriptions of their surroundings.
- **Automated Content Generation**: The system can be adapted for creating educational materials and improving accessibility in various fields.
- **Edge Device Optimization**: Further research is needed to optimize the model for deployment on edge devices with low computational power while maintaining high performance.

## Conclusion

This research demonstrates the effectiveness of combining **ResNet-50** and **LSTM** models for automatic image captioning. By leveraging a deep CNN for feature extraction and an LSTM network for sequential caption generation, the system produces captions that are not only grammatically correct but also semantically meaningful. Future work will focus on enhancing real-world applications and improving the overall efficiency of the model.

## References

1. Chu, Y., et al. (2020). "Automatic image captioning based on ResNet50 and LSTM with soft attention." Wireless Communications and Mobile Computing.
2. Shuster, K., et al. (2019). "Engaging image captioning via personality." IEEE/CVF Conference on Computer Vision and Pattern Recognition.
3. Charu, S., et al. (2020). "Vision to Language: Captioning Images using Deep Learning." 2020 International Conference on Artificial Intelligence and Signal Processing (AISP). IEEE.
4. Dharsini, S. V., et al. (2022). "Captioning based image using Euclidean distance and ResNet-50." 2022 International Conference on Data Science, Agents & Artificial Intelligence (ICDSAAI).
5. Alam, M. S., et al. (2021). "Comparison of different CNN models used as encoders for image captioning." 2021 International Conference on Data Analytics for Business and Industry (ICDABI).

