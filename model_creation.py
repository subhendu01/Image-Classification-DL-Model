# You can also use pretrained model from Keras
# Check https://keras.io/applications/
from keras.applications.resnet50 import ResNet50
model = ResNet50(weights='imagenet')
model.save('models/model_resnet.h5')