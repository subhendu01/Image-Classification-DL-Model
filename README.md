# Image_Classification_DL-Model
It's a deep learning model for image classification.

#### model_creation.py
##### First we create a image classifier model using ResNet50

#### app.py
##### By using the model we predict the classification of image.

### Heroku Deployment
Heroku server has only 500MB of RAM. And this can be a problem for stable running of some Tensorflow tasks. For this project Heroku server is not fit. Because of RAM, but if you run some more basic Tensorflow operations, Heroku can by ok.