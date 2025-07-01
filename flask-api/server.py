from flask import Flask, request, jsonify  # Import Flask and necessary modules
from flask_cors import CORS  # Import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained TFLite model
TFLITE_MODEL_PATH = "TrainedModelRecyclable.tflite"

# Load model into interpreter
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL_PATH)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = Image.open(BytesIO(file.read()))

    # Resize and preprocess
    img = img.resize((224, 224))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Run prediction
    interpreter.set_tensor(input_details[0]["index"], img_array)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]["index"])

    # Get result
    predicted_class = int(predictions[0][0] > 0.5)
    labels = ["Non-Recyclable", "Recyclable"]
    result = labels[predicted_class]

    return jsonify({"prediction": result})


@app.route('/')
def home():
    return "Flask API is running!"


if __name__ == "__main__":
    app.run(debug=True)
