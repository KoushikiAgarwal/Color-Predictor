from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from flask_cors import CORS  # Add this line
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load your trained model
model = load_model('resnet50.h5')  # Make sure this file is in the same folder

# Define class names
class_names = ['white', 'pink', 'orange']

def preprocess_image(image):
    image = image.resize((224, 224))  # Resize image
    img_array = img_to_array(image) / 255.0  # Normalize pixel values
    return np.expand_dims(img_array, axis=0)  # Add batch dimension

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    try:
        image = Image.open(file)
        preprocessed_image = preprocess_image(image)

        predictions = model.predict(preprocessed_image)
        class_id = np.argmax(predictions, axis=1)[0]
        confidence = predictions[0][class_id]

        return jsonify({
            'prediction': class_names[class_id],
            'confidence': float(confidence)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
