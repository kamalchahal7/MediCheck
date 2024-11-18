from tensor_imports import *
    
class Client:
    # m_path: str directory full path of the model file
    # l_path: str directory full path of the labels associated with the model file
    def __init__(self, m_path: str, l_path: str):
        # To-do: Better error handling
        if not os.path.exists(m_path) or not os.path.exists(l_path): raise Exception
        # Load model from .keras path
        self.model: Sequential = load_model(m_path)
        # Load labels from .txt path
        with open(l_path,"r") as f:
            self.labels = f.readline().split(",")

    def __preprocess_img(self, img_input):
        # Open as PIL image
        img = Image.open(img_input)
        # Resize to fit model
        img = img.resize((256,256))
        # Convert to 256x256x3
        img = img.convert('RGB')
        # Turn to numeric array with unit type tf.float32
        img_array = np.array(img)
        img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)
        # Add another singleton dimension to fit model input
        img_tensor = tf.expand_dims(img_tensor, axis=0)
        #Debug: print(img_tensor.shape)
        return img_tensor
        
    def predict(self, img_input):
        # Preprocess for formatting
        feed = self.__preprocess_img(img_input)
        # Get model output
        res = self.model.predict(feed)[0]
        #Debug: print(res)
        # Get index of maximum probability
        mx = max(res)
        idx = 0
        for i in range(len(res)):
            if res[i] == mx:
                idx = i
                break
        # Return prediction label
        return self.labels[idx]
       
'''
if __name__ == "__main__":
    # Sample image
    img_path = "./Model/data/brain/train/Pituitary/images/p (55).jpg"
    # Client testing
    client = Client("brain")
    y_pred = client.predict(img_path)
    print(y_pred)
'''
