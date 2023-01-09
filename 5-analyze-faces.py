from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# Import namespaces


def main():

    global face_client

    try:
        # Get Configuration Settings
        # load_dotenv()
        # cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        # cog_key = os.getenv('COG_SERVICE_KEY')
        # Get Configuration Settings from environment variables instead of .env file
        cog_endpoint = os.environ['COG_SERVICE_ENDPOINT']
        cog_key = os.environ['COG_SERVICE_KEY']

        # Authenticate Face client


        # Menu for face functions
        print('1: Detect faces\nAny other key to quit')
        command = input('Enter a number:')
        if command == '1':
            DetectFaces(os.path.join('images/Exercise-5','people.jpg'))

    except Exception as ex:
        print(ex)

def DetectFaces(image_file):
    print('Detecting faces in', image_file)

    # Specify facial features to be retrieved
    

    # Get faces

#Test 6: test the main function
def test_main():
    
    # Act
    main()

    # Assert detected_faces.jpg is created
    assert os.path.exists('detected_faces.jpg') == True
    
if __name__ == "__main__":
    main()