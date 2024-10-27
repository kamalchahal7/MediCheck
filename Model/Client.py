try:
    from tensor_imports import *
except:
    from Model.tensor_imports import *

from PIL import Image
from tensor_imports import *

class Client:

    def __init__(self, name: str):
        
        m_path = f"./Model/models/{name}.keras"
        l_path = f"./Model/labels/{name}.txt"

        if not os.path.exists(m_path) or not os.path.exists(l_path): raise Exception

        self.model: Sequential = load_model(m_path)

        with open(l_path,"r") as f:
            self.labels = f.readline().split(",")
        
    def predict(self, img):
        res = self.model.predict(img)
        print(res)

if __name__ == "__main__":
    # Sample image
    img_path = "./Model/data/brain/train/Glioma/images/gg (2).jpg"
    img = Image.open(img_path)
    img = img.resize((256,256))
    img = img.convert('RGB')
    img_array = np.array(img)
    img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)
    img_tensor = tf.expand_dims(img_tensor, axis=0)
    print(img_tensor.shape)
    # Client testing
    client = Client("brain")
    client.predict(img=img_tensor)
