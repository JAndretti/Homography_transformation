import numpy as np

# Function to apply homography transformation
def apply_homography(image, H):
    """
    Apply a homography transformation to an image.

    Parameters:
        image (ndarray): Input image.
        H (ndarray): Homography transformation matrix.

    Returns:
        ndarray: Transformed image.
    """
    h, w = image.shape[:2]
    transformed_image = np.zeros_like(image)
    i, j = np.indices((h, w))
    ji_homogeneous = np.stack((j.ravel(), i.ravel(), np.ones_like(j).ravel()))
    transformed_ji = H @ ji_homogeneous
    transformed_ji /= transformed_ji[2, :]
    j_transformed = np.clip(transformed_ji[0], 0, w-1).astype(int)
    i_transformed = np.clip(transformed_ji[1], 0, h-1).astype(int)
    transformed_image[i.ravel(), j.ravel()] = image[i_transformed, j_transformed]
    return transformed_image

# Function to transform bounding box coordinates
def transform_bounding_box(xmin, ymin, xmax, ymax, H):
    """
    Transform bounding box coordinates using a homography matrix.

    Parameters:
        xmin, ymin, xmax, ymax (int): Original bounding box coordinates.
        H (ndarray): Homography transformation matrix.

    Returns:
        tuple: Transformed bounding box coordinates.
    """
    H = np.linalg.inv(H)
    corners = np.array([
        [xmin, ymin, 1],  # Top-left corner
        [xmax, ymin, 1],  # Top-right corner
        [xmax, ymax, 1],  # Bottom-right corner
        [xmin, ymax, 1]   # Bottom-left corner
    ]).T  # Transpose to shape (3, 4)
    transformed_corners = H @ corners
    transformed_corners /= transformed_corners[2, :]
    transformed_xmin = min(transformed_corners[0])
    transformed_ymin = min(transformed_corners[1])
    transformed_xmax = max(transformed_corners[0])
    transformed_ymax = max(transformed_corners[1])
    return transformed_xmin, transformed_ymin, transformed_xmax, transformed_ymax