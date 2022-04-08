# Image Extraction from pdf files

Look `image_extraction.ipynb` for more details

**Run `image_extraction.ipynb` to extract images from unzipped `data_preprocess/PDFS`.**
- Requires PyMuPDF: `pip install PyMuPDF Pillow`
- Run `data_preprocess/data_preprocess.ipynb` to import `bik_df` dataframe into this Notebook

Method 1: Save images to individual folders (by paper).
- Saved to `images/extracted_images`

Method 2: Save all images to one folder.
- Saved to `images/extracted_images_new`

`extracted_images_cleaned.zip` has bad images manually removed, i.e. all-white images, all-black images, color gradients, logos, watermarks, etc.

NOTE: EXTRACTED IMAGES NOT UPLOADED TO GITHUB. SEE GOOGLE DRIVE LINK: https://drive.google.com/drive/folders/1finogOVevkTtMn0uYajDjDd2BVtabXuk?usp=sharing

# Facee Generation

Look `FaceGeneratorDCGAN.ipynb` for more details

**Run `FaceGeneratorDCGAN.ipynb` to generate faces.**
- Recommended to run on Google Colab
- Requires Kaggle API key to directly import 100k celebrity images dataset
- If running on your own images, export image file names as `extracted_images.txt`
- Update filepaths as needed
- Output: `generated_images.zip` contains 500 images generated on epoch 16
- Note: Original `FaceGeneratorDCGAN.ipynb` was updated to directly import Kaggle dataset with Kaggle API key and to generate TXT file for new input images
