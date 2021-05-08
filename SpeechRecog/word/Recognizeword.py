import os
import argparse
import warnings
import numpy as np
from scipy.io import wavfile
from hmmlearn import hmm
from features import mfcc

# define a function to prse the i/p arg. need to specify the i/p folder contain the audio files required to train our SRS

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Trains the HMM-based speech\recognition system')
    parser.add_argument("--input-folder", dest = "input_folder", required = True, help="Input folder containing the audio files for training")
    return parser

# define a class to train the HMMs.
class ModelHMM(object):
    def __init__(self, num_components=4, num_iter=1000):
        self.n_components = num_components
        self.n_iter = num_iter

# define the convariance type and the type of HMM:
        self.cov_type = 'diag'
        self.model_name = 'GaussianHMM'
        self.models =[]

# define the model using the specified parameters:
        self.model = hmm.Gaussian(n_components = self.n_components, covariance_type=self.cov_type, n_iter = self.n_iter)

# define a method to train the model
def train(self, training_data):
    np.seterr(all='ignore')
    cur_model = self.model.fit(training_data)
    self.models.append(cur_model)

# define a method to compute the scorre for i/p data
def compute_score(self, input_data):
    return self.model.score(input_data)

# define a fuction to build a model for each word
def build_models(input_folder):
    speech_models= []

# parse the input directory
    for dirname in os.listdir(input_folder):
        subfolder  = os.path.join(input_folder, dirname)
        if not os.path.join.isdir(subfolder):
            continue

# extract the lable
        label = subfolder[subfolder.rfind('/') + 1:]
        x = np.array([])
        training_files = [x for x in os.libdir(subfolder) if x.endswitch('.wav') [:-1]]
    for filename in training_files:
        filepath = os.path.join(subfolder, filename)
        sampling_freq, signal = wavfile.read(filepath)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            features_mfcc = mfcc(signal, sampling_freq)
        if len(x) == 0:
            x = features_mfcc
        else:
            x =np.append(x, features_mfcc, axis = 0) 
    model = ModelHMM()
    model.train(x)
    speech_models.append((model, label))
    model=None
    return speech_models  

#define a function to run the tests on the dataset
def run_tests(test_files):
    for test_file in test_files:
        sampling_freq, signal = wavfile.read(test_file)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore') 
            features_mfcc = mfcc(signal, sampling_freq)
        max_score = -float('inf')
        output_lable = None
        for item in speech_models:
            model, label = item
            score = model.compute_score(features_mfcc)
            if score > max_score:
                predicted_lable = label
        start_index = test_file.find('/') + 1
        end_index = test_file.rfind('/')
        original_lable = test_file[start_index:end_index]
        print('\n Original:', original_lable)
        print('Predicyed:', predicted_lable)

if __name__ == '__main__':
    args = build_arg_parser().parse_args()
    input_folder = args.input_folder
    speech_models = build_models(input_folder)
    test_files = []
    for root, dirs, files in os.walk(input_folder):
        for filename in (x for x in files if '15' in x):
            filepath = os.path.join(root, filename)
            test_files.append(filepath)
    run_tests(test_files)



    
