# Image Homography Transformation and Bounding Box Adjustment

This project demonstrates how to apply a homography transformation to an image and adjust the coordinates of a bounding box accordingly.

## Description

The code performs the following tasks:
1. Reads an image (`pic.png`).
2. Applies a homography transformation to the image using a given transformation matrix.
3. Transforms the coordinates of a specified bounding box according to the homography transformation.
4. Displays the original and transformed images with their respective bounding boxes.

## Requirements

- Python 3.x
- NumPy
- Pandas
- scikit-image
- Matplotlib

You can install the required packages using the following command:
```bash
pip install numpy pandas scikit-image matplotlib
```

## Usage

1. Save the code into a Python script (e.g., `homography_transformation.py`).
2. Ensure you have an image named `pic.png` in the same directory as the script.
3. Run the script.

The script will:
- Apply the homography transformation to the image.
- Transform the bounding box coordinates.
- Save the transformed image as `transformed_img.png`.
- Display the original and transformed images with their bounding boxes.

## Code Explanation

### Homography Transformation Matrix

The homography transformation matrix is defined as:
```python
tform_matrix = np.array([[3.41818141e+00,  6.69540689e-01, -4.56274360e+02],
                         [1.07093025e+00,  2.64093478e+00, -4.46848244e+02],
                         [1.57043311e-03,  1.29288901e-03,  1.00000000e+00]])
```

### Bounding Box Coordinates

The bounding box coordinates in the original image are:
```python
bb = [226, 222, 388, 417]
xmin, ymin, xmax, ymax = bb
```

### Functions Used

- `apply_homography(img, tform_matrix)`: Applies the homography transformation to the image.
- `transform_bounding_box(xmin, ymin, xmax, ymax, tform_matrix)`: Transforms the bounding box coordinates according to the homography transformation.

### Results

The script prints the original and transformed bounding box coordinates and displays the images with the bounding boxes.

## Results

### Original Image
![Original Image](pic.png)

### Transformed Image
![Transformed Image](transformed_img.png)

