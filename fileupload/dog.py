from keras.preprocessing import image
from keras.applications.inception_v3 import *
import numpy as np
from PIL import Image
from keras import backend as K
# from keras.models import Sequential
# from keras.models import Model
# from keras import backend as K
# sess = tf.Session()
# K.set_session(sess)

#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
#just to remove warnings

def executeUpload(path):
    K.set_image_dim_ordering('tf')
    model= InceptionV3(weights = 'imagenet')

    # model = Model(model,model)
    # model._make_predict_function()
    # graph = tf.get_default_graph()
    # graph = K.get_session().graph
    # graph = tf.get_default_graph()

    # sess=tf.Session()
    # hello = tf.constant('Hello, TensorFlow!')
    # sess.run(hello)

    img = image.load_img(path,target_size=(299,299))
    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    x=preprocess_input(x)
    
    preds = model.predict(x)

    mylist=[]
    mylist=decode_predictions(preds,top=1)[0]
    conf = mylist[0][2] * 100
    str=mylist[0][1]
    str=str.replace('_', ' ')
    breedList=['Afghan_hound','affenpinscher','Lakeland_terrier','Norwegian_elkhound','Samoyed','English_foxhound','American_Staffordshire_terrier','Irish_water_spaniel',
           'Labrador_retriever','Appenzeller','kelpie','Border_collie','Australian_terrier','Ibizan_hound','Irish_water_spaniel','basenji','basset','beagle','Tibetan_terrier',
           'Bedlington_terrier','groenendael','Norwich_terrier','Bernese_mountain_dog','toy_poodle','black-and-tan_coonhound','Bouvier_des_Flandres','bloodhound','bluetick',
           'Maltese_dog','Border_terrier','borzoi','Boston_bull','boxer','Sussex_spaniel','German_short-haired_pointer','briard','Brittany_spaniel','Brabancon_griffon',
           'French_bulldog','bull_mastiff','cairn','German_shepherd','Staffordshire_bullterrier','Cardigan','Scottish_deerhound','Blenheim_spaniel','standard_schnauzer',
           'curly-coated_retriever','Chihuahua','Mexican_hairless','malinois','chow','clumber','miniature_poodle','cocker_spaniel','collie','Tibetan_terrier','curly-coated_retriever',
           'redbone','Doberman','English_setter','EntleBucher','keeshond','flat-coated_retriever','wire-haired_fox_terrier','giant_schnauzer','golden_retriever','standard_poodle',
           'Gordon_setter','Great_Dane','Great_Pyrenees','Greater_Swiss_Mountain_dog','whippet','Pomeranian','Welsh_springer_spaniel','Irish_setter','Italian_greyhound',
           'toy_terrier','Japanese_spaniel','Kerry_blue_terrier','komondor','Eskimo_dog','kuvasz','Leonberg','Lhasa','Shih-Tzu','Newfoundland','Norfolk_terrier','West_Highland_white_terrier',
           'Old_English_sheepdog','otterhound','papillon','Pekinese','Pembroke','pug','Shetland_sheepdog','Rhodesian_ridgeback','Rottweiler','Saluki','Scotch_terrier','Sealyham_terrier',
           'English_springer','soft-coated_wheaten_terrier','Saint_Bernard','Tibetan_mastiff','Great_Dane','vizsla','Airedale','Yorkshire_terrier']

    if mylist[0][1] in breedList:
        if conf>80.0:
            print('I am sure that its a ',mylist[0][1])
        elif conf>30.0 and conf<80.0:
            print('I think its a ',mylist[0][1])
        else:
            print('I am not sure about that, its look like a ',mylist[0][1])
    
    if mylist[0][1] not in breedList:
        print (mylist[0][1] +" Not in the list")
    K.clear_session()    
    return str


        
    
