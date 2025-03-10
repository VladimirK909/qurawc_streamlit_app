import streamlit as st
import os
from PIL import Image

def get_image_files(folder_path):
    """Retrieve all image files from the specified folder."""
    supported_formats = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff")
    return [f for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]

def main():
    st.title("QuRAWC Visualizer App")

    st.write("Use the slider below to cycle through the firefighting steps and observe how the fire spreads and is controlled.")

    folder_path = "gif1"  # Change this to the path of your images folder

    if not os.path.exists(folder_path):
        st.error(f"The folder '{folder_path}' does not exist.")
        return

    image_files = get_image_files(folder_path)

    if not image_files:
        st.error("No image files found in the specified folder.")
        return

    image_files.sort()  # Sort files alphabetically

    index = st.slider("Visualize the firefighting animation shown in the presentation:", 0, len(image_files) - 1, 0)

    image_path = os.path.join(folder_path, image_files[index])
    image = Image.open(image_path)

    st.image(image, caption=image_files[index], use_container_width=True)

if __name__ == "__main__":
    main()
