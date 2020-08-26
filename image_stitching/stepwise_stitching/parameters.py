'''
@brief: Paramters
@author: Vijendra Singh
'''

# if true, enable additional print and visulaization
TEST_BOOL = True
TEST_ID = 'l2r'
# factor by image should be downscaled before use
DOWN_FACTOR = 6
# row and column of images in complete view
VIEW_ROWS = 2
VIEW_COLS = 2

# ---Feature matching---
# feature matching algorithm, choose between 'sift' and 'surf'
FEATURE_MATCHING_ALGORITHM = 'surf'
# -matching-
# FLANN matcher parameters
FLANN_INDEX_PARAMS = dict(algorithm=1, trees=5)
FLANN_SEARCH_PARAMS = dict(checks=50)
FLANN_K = 2
# minimum number of feature matching in two image
MIN_MATCH_COUNT = 4