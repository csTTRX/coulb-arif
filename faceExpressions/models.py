import cv2
from django.db import models
from authenticate.models import User
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
# Create your models here.


class Postes(models.Model):
    poste_type = models.CharField(max_length=200)
    poste_description = models.CharField(max_length=250)

    def __str__(self):
        return self.poste_type
    
class Candidats (models.Model):
    first_name = models.CharField(max_length=200, verbose_name="nom")
    last_name = models.CharField(max_length=200, verbose_name="prenom")
    adress = models.CharField(max_length=250)
    email = models.EmailField(verbose_name="email")
    photo_file_name = models.ImageField(verbose_name='photo')
    cv_file_name = models.FileField(upload_to='cv')
    video_file_name = models.FileField(upload_to='videos')
    poste = models.ForeignKey(Postes, on_delete=models.CASCADE, related_name='poste')
    selected = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    angry = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    disgust = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    fear = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    surprise = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    naturel = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    sad = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    happy = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    total_frame = 1

    IMAGE_MAX_SIZE = (172, 172)
    def resize_image(self):
        photo = Image.open(self.photo_file_name)
        photo.thumbnail(self.IMAGE_MAX_SIZE)
        photo.save(self.photo_file_name.path)
    
    
    def traitement(self):
        cap = cv2.VideoCapture(self.video_file_name.path)
        angry_count = 0
        disgust_count = 0
        fear_count = 0
        naturel_count = 0
        sad_count = 0
        happy_count = 0
        surprise_count = 0
        model = load_model("/home/cs/Projects/Dev/memoire/models/best_model.h5")
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            faces_roi = None
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 3)
            for x, y, w, h in faces:
                roi_gray = gray[y:y+h, x: x+w]
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0 ), 2)
                faces1 = faceCascade.detectMultiScale(roi_gray, 1.2, 3)
                if len(faces1) == 0:
                    print('Pas de visage')
                else:
                    for (ex, ey, ew, eh) in faces1:
                        faces_roi = roi_gray[ey:ey+eh, ex:ex+ew]
                    
            if faces_roi is not None :
                self.total_frame += 1
                final_img = cv2.resize(faces_roi, (48, 48),1)
                final_img = final_img.reshape(48, 48, 1)
                final_img = np.expand_dims(final_img, axis =0)
                final_img = final_img/255
                Predictions = model.predict(final_img)
                if (np.argmax(Predictions)==0):
                    angry_count += 1
                if (np.argmax(Predictions)==1):
                    disgust_count += 1
                if (np.argmax(Predictions)==2):
                    fear_count += 1
                if (np.argmax(Predictions)==3):
                    happy_count += 1
                if (np.argmax(Predictions)==4):
                    naturel_count += 1
                if (np.argmax(Predictions)==5):
                    sad_count += 1
                if (np.argmax(Predictions)==6):
                    surprise_count += 1
            else:
                pass
        cap.release()
        self.happy = happy_count/self.total_frame
        self.angry = angry_count/self.total_frame
        self.fear = fear_count/self.total_frame
        self.sad = sad_count/self.total_frame
        self.disgust = disgust_count/self.total_frame
        self.surprise = surprise_count/self.total_frame
        self.naturel = naturel_count/self.total_frame
        self.score = happy_count + naturel_count/self.total_frame
        print(self.happy)
        print(self.total_frame)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
        if self.total_frame == 1:
            self.traitement()
            self.save()

    def __str__(self):
        return self.first_name