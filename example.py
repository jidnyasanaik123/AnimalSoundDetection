import streamlit as st
from PIL import Image
from gtts import gTTS
import base64
import os

# Title of the app
st.title("Text to Audio")

# Display an image
cow_image = Image.open(r"C:\Users\lenovo\Documents\Animal_App\cow.jpg")
st.image(cow_image, caption="Click the button to hear")

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

# Button to hear the sound
if st.button("Click here to hear the sound", key="sound_button"):
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

# Characteristics Section
st.header("Animal Characteristics")

# Dropdown to select the number of characteristics
num_characteristics = st.selectbox("Select number of characteristics", [2, 5, 10], key="num_characteristics")

# Initialize session state for characteristics display
if "show_characteristics" not in st.session_state:
    st.session_state["show_characteristics"] = False

# Button to display characteristics
if st.button("Show Characteristics", key="show_characteristics_button"):
    st.session_state["show_characteristics"] = True  # Set session state to True

# Display characteristics based on selection
if st.session_state["show_characteristics"]:
    characteristics = {
        2: ["Cows are gentle animals.", "They give us milk."],
        5: [
            "Cows are gentle animals.",
            "They give us milk.",
            "Cows eat grass.",
            "Cows can sleep while standing.",
            "Baby cows are called calves."
        ],
        10: [
            "Cows are gentle animals.",
            "They give us milk.",
            "Cows eat grass.",
            "Cows can sleep while standing.",
            "Baby cows are called calves.",
            "Cows have four stomach compartments.",
            "Cows like to be in groups.",
            "They have a good sense of smell.",
            "Cows can recognize human faces.",
            "They can live up to 20 years."
        ]
    }
    selected_characteristics = characteristics.get(num_characteristics, [])
    st.write("Characteristics:")
    for char in selected_characteristics:
        st.write(f"- {char}")

