import os
import cv2

# params
viz_bool = True
down_factor = 6


def stitch_images(images):
    '''
    @brief: Stich all the given images and save the stitched image
    @arg[in]: Array of images to be stitched
    '''
    stitcher = cv2.Stitcher_create()
    status, stitched = stitcher.stitch(images)
    if status == 0:
        cv2.imwrite('stitched.png', stitched)
        if viz_bool:
            cv2.imshow("Stitched", stitched)
            cv2.waitKey(0)
    else:
        print("Stitching failed, retake images")


def main():
    images = []
    for image_name in os.listdir('data'):
        image = cv2.imread('data/{}'.format(image_name))
        width = image.shape[1]//down_factor
        height = image.shape[0]//down_factor
        image = cv2.resize(image, (width, height))
        if viz_bool:
            cv2.imshow(image_name, image)
            cv2.waitKey(0)
        images.append(image)
    stitch_images(images)


if __name__ == '__main__':
    main()