This Python script, leveraging the **Pillow** ($\text{PIL}$) library, serves as an automated **batch image resizer and converter**. Its primary function is to efficiently process multiple image files stored in a designated **input folder** ($\text{images\_to\_resize}$), adjust their dimensions to a specified maximum width (in this case, $\text{800}$ pixels) while meticulously **maintaining their aspect ratio**, and then save the results as compressed **JPEG** files into an **output folder** ($\text{resized\_images}$).

---

## **Code Breakdown**

The script operates in three main stages: configuration, preparation/validation, and core processing.

### **1. Configuration and Setup**
The code begins by defining several global variables, or **constants**, that make the script highly customizable. These include the $\text{INPUT\_FOLDER}$, $\text{OUTPUT\_FOLDER}$, the $\text{TARGET\_WIDTH}$ for resizing, the $\text{JPEG\_QUALITY}$ setting, and a list of $\text{SUPPORTED\_EXTENSIONS}$ (e.g., .jpg, .png) to ensure only valid image files are processed.

### **2. Core Processing Function ($\text{resize\_and\_convert\_image}$)**
This is the heart of the script. It takes the file paths, target width, and quality as arguments. It first uses $\text{Image.open()}$ to load the image. It then checks if the $\text{original\_width}$ is greater than the $\text{target\_width}$. If it is, it calculates the necessary $\text{ratio}$ to find the $\text{new\_height}$ that prevents the image from being stretched or distorted. The $\text{img.resize()}$ method then performs the actual scaling, using $\text{Image.Resampling.LANCZOS}$ for high-quality downscaling. Finally, $\text{img.save()}$ writes the newly sized image to the output location, explicitly setting the format to $\text{JPEG}$ and applying the desired quality setting. A robust $\text{try...except}$ block wraps this function to gracefully handle errors like corrupted files or missing paths.

### **3. Batch Orchestration Function ($\text{batch\_resize\_images}$)**
This function manages the overall workflow. It first uses the $\text{os}$ module to **validate** the input folder's existence and **create** the output folder if it doesn't already exist. It then iterates through every file name in the $\text{INPUT\_FOLDER}$ using $\text{os.listdir()}$. For each file, it performs two critical checks: confirming it's a file (not a folder) and verifying that its extension is one of the $\text{SUPPORTED\_EXTENSIONS}$. If both checks pass, it constructs the new output filename (always with a $\text{.jpg}$ extension), joins it with the $\text{OUTPUT\_FOLDER}$ path, and calls the $\text{resize\_and\_convert\_image}$ function to do the heavy lifting. The script concludes by printing a summary of how many images were successfully processed.
