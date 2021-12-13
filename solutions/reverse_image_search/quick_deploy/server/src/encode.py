from numpy import linalg as LA
from towhee import pipeline
from PIL import Image

class Resnet50:
    def __init__(self):
        self.embedding_pipeline = pipeline('image-embedding')

    def resnet50_extract_feat(self, img_path):
        # Return the normalized embedding([[vec]]) of image
        img = Image.open(img_path)
        feat = self.embedding_pipeline(img)
        norm_feat = feat / LA.norm(feat)
        return norm_feat.tolist()[0][0]
