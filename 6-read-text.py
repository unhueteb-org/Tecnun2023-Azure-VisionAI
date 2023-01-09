from dotenv import load_dotenv
import os
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# Import namespaces


def main():

    global cv_client

    try:
        # Get Configuration Settings
        # load_dotenv()
        # cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        # cog_key = os.getenv('COG_SERVICE_KEY')

        # Get Configuration Settings from environment variables instead of .env file
        cog_endpoint = os.environ['COG_SERVICE_ENDPOINT']
        cog_key = os.environ['COG_SERVICE_KEY']

        # Authenticate Computer Vision client
        
        


        # Menu for text reading functions
        print('1: Use Read API for image\n2: Use Read API for document\n3: Read handwriting\nAny other key to quit')
        command = input('Enter a number:')
        if command == '1':
            image_file = os.path.join('images/Exercise-6','Lincoln.jpg')
            GetTextRead(image_file)
        elif command =='2':
            image_file = os.path.join('images/Exercise-6','Rome.pdf')
            GetTextRead(image_file)
        elif command =='3':
            image_file = os.path.join('images/Exercise-6','Note.jpg')
            GetTextRead(image_file)
        

    except Exception as ex:
        print(ex)
        return 0

def GetTextRead(image_file):
    print('Reading text in {}\n'.format(image_file))




#Test 7: test the main function
def test_GetTextRead():
        
        # Arrange
        global cv_client
        expected = 1
        # Get Configuration Settings from environment variables instead of .env file
        cog_endpoint = os.environ['COG_SERVICE_ENDPOINT']
        cog_key = os.environ['COG_SERVICE_KEY']

        # Authenticate Computer Vision client
        # Authenticate Computer Vision client
        credential = CognitiveServicesCredentials(cog_key) 
        cv_client = ComputerVisionClient(cog_endpoint, credential)
        image_file = os.path.join('images/Exercise-6','Note.jpg')
        

        # Act
        actual=GetTextRead(image_file)

        # Assert
        assert actual == expected


if __name__ == "__main__":
    main()