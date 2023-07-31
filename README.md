# Fish Species Prediction Web App

This is a simple web-based application that predicts the species of a fish based on its Weight, Length1, Length2, Length3, Height, and Width. The prediction is made using a pre-trained machine learning model deployed with Flask.

## Getting Started

To use the web app, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure you have the pre-trained machine learning model file (`fish_species_model.pkl`) in the root directory.
4. Run the Flask app using `python fish_species_app.py`.
5. Access the app in your web browser at `http://localhost:5000/`.
6. Enter the fish parameters and click "Predict Species" to see the prediction.

## Dependencies

The web app uses Flask for serving the application, scikit-learn for the machine learning model, and joblib for model serialization.

## Data

The machine learning model was trained on a fish species dataset. The data used for training is not included in this repository.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to fork and modify the code to suit your needs!

