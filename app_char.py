import streamlit as st
from PIL import Image
from gtts import gTTS
import base64
import os

# Title of the app
st.title("Text to Audio and Animal Characteristics")

# Display an image
cow_image = Image.open(r"C:\Users\lenovo\Documents\Animal_App\cow.jpg")
st.image(cow_image, caption="Click the button to hear or see characteristics")

# Function to generate audio and return base64 string
def generate_audio(text):
    tts = gTTS(text, lang='en')
    audio_file_path = "cow.mp3"
    tts.save(audio_file_path)

    # Read and encode the audio file to base64
    with open(audio_file_path, "rb") as f:
        audio_bytes = f.read()
        b64_audio = base64.b64encode(audio_bytes).decode()

    return b64_audio

# Button to play sound
if st.button("Click here to hear the sound"):
    # Generate audio and get base64 string
    b64_audio = generate_audio("Cow")

    # Create an HTML string for autoplaying audio without controls
    html_string = f"""
    <audio autoplay style="display:none;">
        <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
    </audio>
    """

    # Display the HTML in Streamlit
    st.markdown(html_string, unsafe_allow_html=True)

# Characteristics of a Cow
cow_characteristics = {
    "Color": "Cows typically have white, black, brown, or mixed-color coats.",
    "Size": "Cows can weigh between 1,000 to 1,800 pounds, depending on the breed.",
    "Habitat": "Cows are typically found in farms, grassy fields, and pastures.",
    "Diet": "Cows are herbivores and primarily eat grass, hay, and other plants.",
    "Behavior": "Cows are social animals, often forming close bonds with other cows in the herd."
}

# Button for Characteristics
if st.button("Click here for Cow Characteristics"):
    # Display the characteristics of the cow when the button is clicked
    st.subheader("Cow Characteristics:")
    for characteristic, description in cow_characteristics.items():
        st.write(f"**{characteristic}:** {description}")

# Optionally, remove the generated audio file after use (if needed)
# if os.path.exists("cow.mp3"):
#     os.remove("cow.mp3")
