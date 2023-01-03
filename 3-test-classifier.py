from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

def main():
    from dotenv import load_dotenv

    try:
        # Get Configuration Settings
        #load_dotenv()

        # Get Configuration Settings from environment variables instead of .env file
        prediction_endpoint = os.environ['PREDICTIONENDPOINT']
        prediction_key = os.environ['PREDICTIONKEY']
        project_id = os.environ['PROJECTID']
        model_name = os.environ['MODELNAME']

        # Authenticate a client for the training API
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        prediction_client = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=credentials)

        # Classify test images
        for image in os.listdir('images/Exercise-3/test-images'):
            image_data = open(os.path.join('images/Exercise-3/test-images',image), "rb").read()
            results = prediction_client.classify_image(project_id, model_name, image_data)

            # Loop over each label prediction and print any with probability > 50%
            for prediction in results.predictions:
                if prediction.probability > 0.5:
                    print(image, ': {} ({:.0%})'.format(prediction.tag_name, prediction.probability))

        #it worked
        return 1
    
    except Exception as ex:
        print(ex)
        return 0

# Test 4: unit testing main def calling classification model
def test_main():

    #Arrange
    expected = 1
    
    #Act
    actual=main()

    #Assert
    assert actual == expected
    

if __name__ == "__main__":
    main()

