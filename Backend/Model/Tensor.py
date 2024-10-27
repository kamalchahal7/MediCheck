try:
    from tensor_imports import *
    from helpers import *
except:
    from Model.tensor_imports import *
    from Model.helpers import *

SEED = 12345

class Tensor:

    # MARK: Properties & Initializer

    conv_parameters = {
        'filter_1': 3,
        'filter_2': 9,
        'kernel_shape_1': (1,1),
        'kernel_shape_2': (1,1),
        'dilation_rate_1': (1,1),
        'dilation_rate_2': (1,1),
        'padding': 'valid'
    }
    hyper_parameters = {
        'units_1': 256,
        'units_2': 256,
        'units_3': 128,
        'units_4': 64,
        'reg': 0.005
    }

    def __init__(self, name: str):
        np.random.seed(SEED)
        tf.random.set_seed(SEED)
        os.environ['PYTHONHASHSEED'] = str(SEED)
        self.model = None
        train_ = get_data(type=name ,dtype='train')
        val_ = get_data(type=name ,dtype='val')
        self.train = tune(train_)
        self.val = tune(val_)
        self.name = name
        self.labels = get_labels(name)

    # MARK: MODEL

    def build_model(self):
        model = Sequential()
        model.add(InputLayer(shape=[256,256,3]))
        # Convolution Block One
        model.add(BatchNormalization())
        model.add(Conv2D(filters=self.conv_parameters['filter_1'],kernel_size=self.conv_parameters['kernel_shape_1'],dilation_rate=self.conv_parameters['dilation_rate_1'],padding=self.conv_parameters['padding'],activation='relu'))
        model.add(MaxPool2D())
        # Convolutional Block Two
        model.add(Conv2D(filters=self.conv_parameters['filter_2'],kernel_size=self.conv_parameters['kernel_shape_2'],dilation_rate=self.conv_parameters['dilation_rate_2'],padding=self.conv_parameters['padding'],activation='relu'))
        model.add(MaxPool2D())
        # Inference Layer
        model.add(Flatten())
        model.add(Dense(units=self.hyper_parameters['units_1'],activation='relu'))
        model.add(Dense(units=self.hyper_parameters['units_2'],activation='relu'))
        model.add(Dense(units=self.hyper_parameters['units_3'],activation='relu'))
        model.add(Dense(units=self.hyper_parameters['units_4'],activation='relu'))
        model.add(Dense(units=4,activation='softmax',kernel_regularizer=L2(self.hyper_parameters['reg'])))
        self.model = model
    
    def train_model(self, epochs=15, verbose=1):
        if self.model == None:
            return

        self.model.compile(optimizer='adam',loss=CategoricalCrossentropy(from_logits=False),metrics=['accuracy'])
        history = self.model.fit(
            self.train,
            validation_data=self.val,
            batch_size=32,
            epochs=epochs,
            verbose=verbose
        )

        return history
    
    # Tune Hyper-parameters

    def hyper_model(self):
        return
    
    def tune_hyper(self):
        return

    def evaluate_model(self):
        if self.model == None or not self.model.compiled:
            return []
        
        return self.model.evaluate(self.val, verbose=0)

    # MARK: Save Model

    def save_model(self):
        self.model.save(f"./Model/models/{self.name}.keras")

        f = open(f"./Model/labels/{self.name}.txt", "w")
        f.write(self.labels)
        f.close()
    
if __name__ == "__main__":
    tensor = Tensor(name="brain")
    tensor.build_model()
    tensor.train_model(epochs=20)   
    res = tensor.evaluate_model()     
    print(f"Loss: {res[0]}, Accuracy: {res[1]}")
    tensor.save_model()
    