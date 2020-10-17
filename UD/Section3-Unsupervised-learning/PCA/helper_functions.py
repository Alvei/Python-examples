###########################################
# Udacity
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
###########################################

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

# Reload the data set and make it global. Not best practice...
train = pd.read_csv('./data/train.csv')
y = train['label']                       # save the labels to a Pandas series target
X = train.drop("label",axis=1)           # Drop the label feature

def show_images(num_images: int) -> None:
    ''' Plot the num_images provided of MNIST dataset. Images are 28x28 pixels

        INPUT:  Number of images you would like to view.
                Mod 10 of num_images should be 0 and it should be fewer than 101 images.
        OUTPUT: A figure with the images shown for the training data.
    '''
    if num_images % 10 == 0 and num_images <= 100:
        for digit_num in range(0, num_images):
            plt.subplot(num_images/10, 10, digit_num+1)            # create subplots
            mat_data = X.iloc[digit_num].values.reshape(28, 28)    # reshape images
            plt.imshow(mat_data) # plot the data
            plt.xticks([])       # removes numbered labels on x-axis
            plt.yticks([])       # removes numbered labels on y-axis
    else:
        print('That is not the right input, please read the docstring before continuing.')


def show_images_by_digit(digit_to_see: int) -> None:
    ''' This function plots 50 images all of the type digits_to_see of the MNIST dataset.

        INPUT:  digits_to_see - A number between 0 and 9 of what you want to see.
        OUTPUT: A figure with the images shown for the training data.
    '''
    if digit_to_see in list(range(10)):
        indices = np.where(y == digit_to_see) # pull indices for num of interest
        for digit_num in range(0, 50):
            plt.subplot(5,10, digit_num+1)                                   # create subplots
            mat_data = X.iloc[indices[0][digit_num]].values.reshape(28, 28)  # reshape images
            plt.imshow(mat_data) # plot the data
            plt.xticks([])       # removes numbered labels on x-axis
            plt.yticks([])       # removes numbered labels on y-axis
    else:
        print('That is not the right input, please read the docstring before continuing.')


def fit_random_forest_classifier(X, y) -> float:
    ''' INPUT:  names are pretty self explanatory
        OUTPUT: prints the confusion matrix and accuracy, returns accuracy
    '''
    # Create training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # We could grid search and tune, but let's just fit a simple model to see how it does
    clf = RandomForestClassifier(n_estimators=100, max_depth=None)
    clf.fit(X_train, y_train)
    y_preds = clf.predict(X_test)

    print(confusion_matrix(y_test, y_preds))
    acc = accuracy_score(y_test, y_preds)
    print(acc)

    return acc


def fit_random_forest_classifier2(X, y) -> float:
    '''
    INPUT:  X - the x-matrix of input features
            y - the response column
    OUTPUT: prints the confusion matrix and accuracy, returns accuracy
    '''
    # Create training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # We could grid search and tune, but let's just fit a simple model to see how it does

    clf = RandomForestClassifier(n_estimators=100, max_depth=None)
    clf.fit(X_train, y_train)
    y_preds = clf.predict(X_test)
    acc = accuracy_score(y_test, y_preds)

    return acc


def do_pca(n_components: int, data):
    ''' Transforms data using PCA to create n_components, and provides back
        the results of the transformation.

    INPUT: n_components - number of principal components to create
           data - data you would like to transform

    OUTPUT: pca   - pca object created after fitting the data
            X_pca - transformed X matrix with new number of components
    '''
    X = StandardScaler().fit_transform(data)
    pca = PCA(n_components)
    X_pca = pca.fit_transform(X)
    return pca, X_pca


def plot_components(X, y) -> None:
    ''' Plots the data in a 2 dimensional space to view separation
        INPUT: X - x-matrix of input features
               y - response column
        OUTPUT: none
    '''
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    plt.figure(figsize=(10, 6))
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(y[i]), color=plt.cm.Set1(y[i]), fontdict={'size': 15})

    plt.xticks([]), plt.yticks([]), plt.ylim([-0.1,1.1]), plt.xlim([-0.1,1.1])


def scree_plot(pca):
    ''' Creates a scree plot associated with the principal components.

        INPUT:  pca - result of instantian of PCA in scikit learn
        OUTPUT: None
    '''
    num_components=len(pca.explained_variance_ratio_)
    ind = np.arange(num_components)
    vals = pca.explained_variance_ratio_

    plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)
    cumvals = np.cumsum(vals)
    ax.bar(ind, vals)
    ax.plot(ind, cumvals)
    for i in range(num_components):
        ax.annotate(r"%s%%" % ((str(vals[i]*100)[:4])), (ind[i]+0.2, vals[i]), va="bottom", ha="center", fontsize=12)

    ax.xaxis.set_tick_params(width=0)
    ax.yaxis.set_tick_params(width=2, length=12)

    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Variance Explained (%)")
    plt.title('Explained Variance Per Principal Component')


def plot_component(pca, comp: int) -> None:
    '''
    Plots an image associated with each component to understand how the weighting
    of the components
    INPUT:
            pca  - pca object created from PCA in sklearn
            comp - component you want to see starting at 0
    OUTPUT: None
    '''
    if comp <= len(pca.components_):
        mat_data = np.asmatrix(pca.components_[comp]).reshape(28,28)  # reshape images
        plt.imshow(mat_data); # plot the data
        plt.xticks([])        # removes numbered labels on x-axis
        plt.yticks([])        # removes numbered labels on y-axis
    else:
        print('That is not the right input, please read the docstring before continuing.')


def pca_results(full_dataset, pca):
	''' Create a DataFrame of the PCA results
	    Includes dimension feature weights and explained variance
	    Visualizes the PCA results
	'''

	# Dimension indexing
	dimensions = dimensions = ['Dimension {}'.format(i) for i in range(1, len(pca.components_)+1)]

	# PCA components
	components = pd.DataFrame(np.round(pca.components_, 4), columns = full_dataset.keys())
	components.index = dimensions

	# PCA explained variance
	ratios = pca.explained_variance_ratio_.reshape(len(pca.components_), 1)
	variance_ratios = pd.DataFrame(np.round(ratios, 4), columns = ['Explained Variance'])
	variance_ratios.index = dimensions

	# Create a bar plot visualization
	fig, ax = plt.subplots(figsize = (14,8))

	# Plot the feature weights as a function of the components
	components.plot(ax = ax, kind = 'bar');
	ax.set_ylabel("Feature Weights")
	ax.set_xticklabels(dimensions, rotation=0)


	# Display the explained variance ratios
	for i, ev in enumerate(pca.explained_variance_ratio_):
		ax.text(i-0.40, ax.get_ylim()[1] + 0.05, "Explained Variance\n          %.4f"%(ev))

	# Return a concatenated DataFrame
	return pd.concat([variance_ratios, components], axis = 1)
