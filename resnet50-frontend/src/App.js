import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
    const [file, setFile] = useState(null);
    const [imagePreview, setImagePreview] = useState(null);
    const [prediction, setPrediction] = useState("");

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        setFile(selectedFile);
        setImagePreview(URL.createObjectURL(selectedFile));
    };

    const handleSubmit = async () => {
        if (!file) {
            alert("Please upload a file!");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post(
                "http://127.0.0.1:5000/predict",
                formData,
                {
                    headers: { "Content-Type": "multipart/form-data" },
                }
            );
            setPrediction(response.data.prediction);
        } catch (error) {
            console.error("Error:", error);
            setPrediction("Error occurred while predicting");
        }
    };

    return (
        <div className="app">
            <header className="header">
                <h1>Flower Color Prediction Using ResNet50</h1>
                <p>Upload a flower image and predict its color!</p>
            </header>
            <main className="main">
                <div className="upload-section">
                    <input type="file" onChange={handleFileChange} />
                    <button className="predict-button" onClick={handleSubmit}>
                        Predict
                    </button>
                </div>
                {imagePreview && (
                    <div className="image-preview">
                        <img src={imagePreview} alt="Selected" />
                    </div>
                )}
                {prediction && (
                    <div className="prediction-result">
                        <h2>Prediction: {prediction}</h2>
                    </div>
                )}
            </main>
        </div>
    );
}

export default App;
