import streamlit as st
from PIL import Image

st.title("PriDeb Image Resizer")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    # Resize options
    width = st.number_input("Enter new width", min_value=1, value=image.width)
    height = st.number_input("Enter new height", min_value=1, value=image.height)

    if st.button("Resize Image"):
        resized_image = image.resize((width, height))
        st.image(resized_image, caption="Resized Image", use_container_width=True)

        # Convert image to bytes for download
        img_format = uploaded_file.name.split(".")[-1].upper()
        if img_format not in ["JPG", "JPEG", "PNG"]:
            img_format = "PNG"

        resized_image_bytes = resized_image.tobytes()
        st.download_button(
            label="Download Resized Image",
            data=resized_image_bytes,
            file_name=f"resized_image.{img_format.lower()}",
            mime=f"image/{img_format.lower()}"
        )
