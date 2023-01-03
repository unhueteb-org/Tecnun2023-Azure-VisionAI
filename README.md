# Tecnun2023-Azure-VisionAI

# Prerequisites

Your teacher will onboard you into the process of opening the repository for the session.

You will receive a GitHub Classroom link that will provide:
- The repository for the labs/exercises
- **README.md** file with instructions to follow
- Lab files for each exercise
- GitHub Codespace -> a cloud development environment to test/try your code. 

# Exercise 1: Get Started with Cognitive Services

In this exercise, you'll get started with Cognitive Services by creating a **Cognitive Services** resource in your Azure subscription and using it from a client application. The goal of the exercise is not to gain expertise in any particular service, but rather to become familiar with a general pattern for provisioning and working with cognitive services as a developer.

## Provision a Cognitive Services resource

Azure Cognitive Services are cloud-based services that encapsulate artificial intelligence capabilities you can incorporate into your applications. You can provision individual cognitive services resources for specific APIs (for example, **Language** or **Computer Vision**), or you can provision a general **Cognitive Services** resource that provides access to multiple cognitive services APIs through a single endpoint and key. In this case, you'll use a single multi **Cognitive Services** resource, a single endpoint for multiple AI cognitive services.

1. Open the Azure portal at `https://portal.azure.com`, and sign in using the account associated with your Azure subscription.
2. Select the **Create a resource** button, search for *cognitive services*, and create a **Cognitive Services** resource with the following settings:
    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)*
    - **Region**: *Choose any available region*
    - **Name**: *Enter a unique name*
    - **Pricing tier**: Standard S0
3. **Select the required checkboxes** and create the resource.
4. Wait for deployment to complete, and then view the deployment details.
5. Go to the resource and view its **Keys and Endpoint** page. **This page contains the information that you will need to connect to your resource** and use it from applications you develop. Specifically:
    - An HTTP *endpoint* to which client applications can send requests.
    - Two *keys* that can be used for authentication (client applications can use either key to authenticate).
    - The *location* where the resource is hosted. This is required for requests to some (but not all) APIs.

1. We need to keep this sensitive information (anyone with the data collected before could use your resource!) on a safe place to be able to use it on our GitHub environment. On your GitHub repository website, go to **Settings>Secrets>Actions**.

    ![GitHub Action Secrets](images/github-secrets-actions.jpg)

    - Create 2 **New repository secrets**.
        - Name: **COG_SERVICE_ENDPOINT** Secret: **The endpoint from your Cognitive Service resource**.
        - Name: **COG_SERVICE_KEY** Secret: **1 of the keys provided**

1. Repeat same process and same 2 keys below **Settings>Secrets>Codespaces** section.

1. Your code during this labs will get the neccesary sensitive information from GitHub Secrets, instead of hard coding it (risk of exposing it!).

## Use a REST Interface

The cognitive services APIs are REST-based, so you can consume them by submitting JSON requests over HTTP. In this example, you'll explore a console application that uses the **Language** REST API to perform language detection; but the basic principle is the same for all of the APIs supported by the Cognitive Services resource.


1. In GitHub Codespace, open the following file:

    - **Python**: 1-rest-client.py

    Open the code file and review the code it contains, noting the following details:
    - Various namespaces are imported to enable HTTP communication

    - The program accepts user input, and uses the **GetLanguage** function to call the Text Analytics language detection REST API for your cognitive services endpoint to detect the language of the text that was entered.
    - The request sent to the API consists of a JSON object containing the input data - in this case, a collection of **document** objects, each of which has an **id** and **text**.
    - The key and endpoint for your service is included in the request header to authenticate your client application. These information is read from **GitHub Secrets** (environment variables).

    - The response from the service is a JSON object, which the client application can parse.

4. Open the Terminal. Then enter the following language-specific command to run the program:

    **Python**

    ```
    python 1-rest-client.py
    ```

5. When prompted, enter some text and review the language that is detected by the service, which is returned in the JSON response. For example, try entering "Hello", "Bonjour", and "Gracias".
6. When you have finished testing the application, enter "quit" to stop the program.

## Use an SDK

You can write code that consumes cognitive services REST APIs directly, but there are **software development kits (SDKs) for many popular programming languages**, including Microsoft C#, Python, and Node.js. Using an SDK can greatly simplify development of applications that consume cognitive services.

1. In the terminal, run the following command to install neccesary libraries:

   
    **Python**

    ```
    pip install azure-ai-textanalytics==5.1.0
    ```

3. View the contents of the **1-sdk-client.py** (Python) file:
    

    Open the code file and review the code it contains, noting the following details:
    - The namespace for the SDK you installed is imported
    - The **GetLanguage** function uses the SDK to create a client for the service (using your secret endpoint and key) and then uses the client to detect the language of the text that was entered.
5. Return to the terminal and enter the following command to run the program:

    **Python**

    ```
    python 1-sdk-client.py
    ```

6. When prompted, enter some text and review the language that is detected by the service. For example, try entering "Goodbye", "Au revoir", and "Hasta la vista".
7. When you have finished testing the application, enter "quit" to stop the program.

> **Note**: Some languages that require Unicode character sets may not be recognized in this simple console application.



# Exercise 2: Analyze Images with Computer Vision

Computer vision is an artificial intelligence capability that enables software systems to interpret visual input by analyzing images. In Microsoft Azure, the **Computer Vision** cognitive service provides **pre-built models** for common computer vision tasks, including analysis of images to suggest captions and tags, detection of common objects, landmarks, celebrities, brands, and the presence of adult content. You can also use the Computer Vision service to analyze image color and formats, and to generate "smart-cropped" thumbnail images.

## Prepare to use the Computer Vision SDK

In this exercise, you'll complete a partially implemented client application that uses the **Computer Vision SDK** to analyze images.

1. In the **GitHub Codespace**, open the **Terminal**,  install the Computer Vision SDK package by running the appropriate command for your language preference:

**Python**

```
pip install azure-cognitiveservices-vision-computervision==0.7.0
```
    
4. File **2-image-analysis.py**(Python) contains a code file for the client application:


    Open the code file and at the top, under the existing namespace references, find the comment **Import namespaces**. Then, under this comment, add the following language-specific code to import the namespaces you will need to use the Computer Vision SDK:

**Python**

```Python
# import namespaces
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
```
    
## View the images you will analyze

In this exercise, you will use the Computer Vision service to analyze multiple images.

1. In the **Explorer** tab, expand the **images>Exercise-2** folder and the **images** folder it contains.

2. Select each of the image files in turn to view them.

## Analyze an image to suggest a caption

Now you're ready to use the SDK to call the Computer Vision service and analyze an image.

1. In the code file for your client application (**2-image-analysis.py**), in the **Main** function, note that the code to load the configuration settings has been provided. Then find the comment **Authenticate Computer Vision client**. Then, under this comment, **add the following language-specific code** to create and authenticate a Computer Vision client object:


**Python**

```Python
# Authenticate Computer Vision client
credential = CognitiveServicesCredentials(cog_key) 
cv_client = ComputerVisionClient(cog_endpoint, credential)
```

2. In the **Main** function, under the code you just added, note that the code specifies the path to an image file and then passes the image path to two other functions (**AnalyzeImage** and **GetThumbnail**). These functions **are not yet fully implemented**.

3. In the **AnalyzeImage** function, under the comment **Specify features to be retrieved**, add the following code:

**Python**

```Python
# Specify features to be retrieved
features = [VisualFeatureTypes.description,
            VisualFeatureTypes.tags,
            VisualFeatureTypes.categories,
            VisualFeatureTypes.brands,
            VisualFeatureTypes.objects,
            VisualFeatureTypes.adult]
```
    
4. In the **AnalyzeImage** function, under the comment **Get image analysis**, add the following code (including the comments indicating where **you will add more code later.**):


**Python**

```Python
# Get image analysis
with open(image_file, mode="rb") as image_data:
    analysis = cv_client.analyze_image_in_stream(image_data , features)

# Get image description
for caption in analysis.description.captions:
    print("Description: '{}' (confidence: {:.2f}%)".format(caption.text, caption.confidence * 100))

# Get image tags


# Get image categories 


# Get brands in the image


# Get objects in the image


# Get moderation ratings

```
    
5. Save your changes and return to the **Terminal** for the **image-analysis** folder, and enter the following command to run the program with the argument **images/Exercise-2/street.jpg**:


**Python**

```
python 2-image-analysis.py images/Exercise-2/street.jpg
```
    
6. Observe the output, which should include a suggested caption for the **street.jpg** image.
7. Run the program again, this time with the argument **images/building.jpg** to see the caption that gets generated for the **building.jpg** image.
8. Repeat the previous step to generate a caption for the **images/person.jpg** file.

## Get suggested tags for an image

It can sometimes be useful to identify relevant *tags* that provide clues about the contents of an image.

1. In the **AnalyzeImage** function, under the comment **Get image tags**, add the following code:

**Python**

```Python
# Get image tags
if (len(analysis.tags) > 0):
    print("Tags: ")
    for tag in analysis.tags:
        print(" -'{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))
```

2. Save your changes and run the program once for each of the image files in the **images** folder, observing that in addition to the image caption, a list of suggested tags is displayed.

## Get image categories

The Computer Vision service can suggest *categories* for images, and within each category it can identify well-known landmarks.

1. In the **AnalyzeImage** function, under the comment **Get image categories**, add the following code:


**Python**

```Python
# Get image categories
if (len(analysis.categories) > 0):
    print("Categories:")
    landmarks = []
    for category in analysis.categories:
        # Print the category
        print(" -'{}' (confidence: {:.2f}%)".format(category.name, category.score * 100))
        if category.detail:
            # Get landmarks in this category
            if category.detail.landmarks:
                for landmark in category.detail.landmarks:
                    if landmark not in landmarks:
                        landmarks.append(landmark)

    # If there were landmarks, list them
    if len(landmarks) > 0:
        print("Landmarks:")
        for landmark in landmarks:
            print(" -'{}' (confidence: {:.2f}%)".format(landmark.name, landmark.confidence * 100))

```
    
2. Save your changes and run the program once for each of the image files in the **images** folder, observing that in addition to the image caption and tags, a list of suggested categories is displayed along with any recognized landmarks (in particular in the **building.jpg** image).

## Get brands in an image

Some brands are visually recognizable from logo's, even when the name of the brand is not displayed. The Computer Vision service is trained to identify thousands of well-known brands.

1. In the **AnalyzeImage** function, under the comment **Get brands in the image**, add the following code:

**Python**

```Python
# Get brands in the image
if (len(analysis.brands) > 0):
    print("Brands: ")
    for brand in analysis.brands:
        print(" -'{}' (confidence: {:.2f}%)".format(brand.name, brand.confidence * 100))
```
    
2. Save your changes and run the program once for each of the image files in the **images** folder, observing any brands that are identified (specifically, in the **person.jpg** image).

## Detect and locate objects in an image

*Object detection* is a specific form of computer vision in which individual objects within an image are identified and their location indicated by a bounding box..

1. In the **AnalyzeImage** function, under the comment **Get objects in the image**, add the following code:


**Python**

```Python
# Get objects in the image
if len(analysis.objects) > 0:
    print("Objects in image:")

    # Prepare image for drawing
    fig = plt.figure(figsize=(8, 8))
    plt.axis('off')
    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)
    color = 'cyan'
    for detected_object in analysis.objects:
        # Print object name
        print(" -{} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))
        
        # Draw object bounding box
        r = detected_object.rectangle
        bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
        draw.rectangle(bounding_box, outline=color, width=3)
        plt.annotate(detected_object.object_property,(r.x, r.y), backgroundcolor=color)
    # Save annotated image
    plt.imshow(image)
    outputfile = 'objects.jpg'
    fig.savefig(outputfile)
    print('  Results saved in', outputfile)
```
    
2. Save your changes and run the program once for each of the image files in the **images** folder, observing any objects that are detected. After each run, view the **objects.jpg** file that is generated in the same folder as your code file to **see the annotated objects**.

## Get moderation ratings for an image

Some images may not be suitable for all audiences, and you may need to apply some moderation to identify images that are adult or violent in nature.

1. In the **AnalyzeImage** function, under the comment **Get moderation ratings**, add the following code:

**Python**

```Python
# Get moderation ratings
ratings = 'Ratings:\n -Adult: {}\n -Racy: {}\n -Gore: {}'.format(analysis.adult.is_adult_content,
                                                                    analysis.adult.is_racy_content,
                                                                    analysis.adult.is_gory_content)
print(ratings)
```
    
2. Save your changes and run the program once for each of the image files in the **images** folder, observing the ratings for each image.

> **Note**: In the preceding tasks, you used a single method to analyze the image, and then incrementally added code to parse and display the results. **The SDK also provides individual methods** for suggesting captions, identifying tags, detecting objects, and so on - meaning that you can use the most appropriate method to return only the information you need, reducing the size of the data payload that needs to be returned. See the [.NET SDK documentation](https://docs.microsoft.com/dotnet/api/overview/azure/cognitiveservices/client/computervision?view=azure-dotnet) or [Python SDK documentation](https://docs.microsoft.com/python/api/overview/azure/cognitiveservices/computervision?view=azure-python) for more details.

## Generate a thumbnail image

In some cases, you may need to create a smaller version of an image named a *thumbnail*, cropping it to include the main visual subject within new image dimensions.

1. In your code file, find the **GetThumbnail** function; and under the comment **Generate a thumbnail**, add the following code:


**Python**

```Python
# Generate a thumbnail
with open(image_file, mode="rb") as image_data:
    # Get thumbnail data
    thumbnail_stream = cv_client.generate_thumbnail_in_stream(100, 100, image_data, True)

# Save thumbnail image
thumbnail_file_name = 'thumbnail.png'
with open(thumbnail_file_name, "wb") as thumbnail_file:
    for chunk in thumbnail_stream:
        thumbnail_file.write(chunk)

print('Thumbnail saved in.', thumbnail_file_name)
```
    
2. Save your changes and run the program once for each of the image files in the **images** folder, opening the **thumbnail.jpg** file that is generated in the same folder as your code file for each image.

