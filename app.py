import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

# Define the video frame callback function
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # Check if the flip checkbox is checked
    if flip:
        # Flip vertically
        flipped = img[::-1,:,:]
    else:
        flipped = img

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

# Streamlit app title
st.title('WebRTC Example - Vertical Flip')

# Checkbox to control flipping
flip = st.checkbox("Flip vertically")

rtc_configuration = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},  # Example STUN server
        # Add your TURN server configuration if required
    ]
}

webrtc_ctx = webrtc_streamer(key="example", video_frame_callback=video_frame_callback, rtc_configuration=rtc_configuration)

# Display the video streamer
if webrtc_ctx.video_transformer:
    if not webrtc_ctx.state.playing:
        st.write('Waiting for webcam to start...')
