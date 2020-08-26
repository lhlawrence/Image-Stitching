'''
@brief: 
@author: Vijendra Singh
'''

import os
import cv2

import parameters as params


def read_images(dir_name='data'):
    '''
    @brief: read images and store it along with unique ID representing its position
    @args[in]: directory containing images
    @args[out]: list of images and its corresping assigned ID
    '''
    images = []
    image_names = os.listdir(dir_name)
    image_names.sort()
    for cam_num, image_name in enumerate(image_names):
        print(image_name, 'loaded')
        image = cv2.imread(os.path.join(dir_name, image_name), 0)
        width = image.shape[1]//params.DOWN_FACTOR
        height = image.shape[0]//params.DOWN_FACTOR
        image = cv2.resize(image, (width, height))
        row = cam_num//params.VIEW_ROWS
        col = cam_num % params.VIEW_COLS
        images.append([(row, col), image])
        if params.TEST_BOOL:
            cv2.imshow(image_name, image)
            cv2.moveWindow(image_name, 100, 50)
            cv2.waitKey(0)
            cv2.destroyWindow(image_name)
    return images