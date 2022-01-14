import numpy             as np
from flask               import Flask, request, jsonify
from keras.models        import load_model
from keras.preprocessing import image


app = Flask(__name__)

path = 'api\saved_model'
def load_model1(path):
    model = load_model('{}'.format(path))
    return model


model = load_model1(path)

@app.route('/<string:img_name>',methods = ["POST"])
def classify_image(img_name):
    path = r'api\save_img/'
    img = image.load_img(path + img_name, target_size = (64, 64))
    img = image.img_to_array(img)
    img /= 255
    img = np.expand_dims(img, axis = 0)
    pred = model.predict(img)
    if pred >= 0.5:
        return jsonify({'Object_identified': 'Cat'})
    return jsonify({'Object_identified':'Dog'})



app.run(debug= False)