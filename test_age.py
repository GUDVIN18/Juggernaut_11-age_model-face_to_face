import requests
from PIL import Image
from io import BytesIO
from transformers import ViTFeatureExtractor, ViTForImageClassification
import time



def source_age(image_path):
    a = time.time()
    im = Image.open((image_path))

    # Init model, transforms
    model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
    transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')

    # Transform our image and pass it through the model
    inputs = transforms(im, return_tensors='pt')
    output = model(**inputs)

    # Predicted Class probabilities
    proba = output.logits.softmax(1)

    # Predicted Classes
    preds = proba.argmax(1)
    # Список возрастных категорий
    age_categories = [
        '2', '8', '19', '27', 
        '36', '46', '56', '66', '80'
    ]

    # Вывод результатов
    predicted_age_index = preds.item()
    predicted_age_category = age_categories[predicted_age_index]

    b = time.time()
    c = b - a 
    print(predicted_age_category, f'time: {c}')
    return predicted_age_category