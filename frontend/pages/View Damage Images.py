import streamlit as st
import os
from PIL import Image

# ------------------- Config -------------------
st.set_page_config(page_title="Damage Viewer", page_icon="🖼️", layout="wide")
st.title("🖼️ View Damage Images by State & Highway")

# ------------------- Inputs -------------------
state_code_map = {
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "RS": "Rio Grande do Sul"
}

highways_per_state = {
    "DF": ["BR-020", "BR-060", "BR-070", "BR-251"],
    "ES": ["BR-101", "BR-259", "BR-482"],
    "RS": ["BR-290", "BR-386"]
}

# State selection
selected_state = st.selectbox("Select State", list(state_code_map.keys()), format_func=lambda x: state_code_map[x])

# Highway selection
selected_highway = st.selectbox("Select Highway", highways_per_state[selected_state])

# ------------------- Image Display -------------------
img_folder = r"C:\Users\SHREY\Desktop\gnctd\frontend\Visualization"
search_prefix = f"{selected_state}_{selected_highway.replace('-', '')}"

matched_imgs = sorted([
    f for f in os.listdir(img_folder)
    if f.startswith(f"{selected_state}_{selected_highway}") and f.lower().endswith(('.jpg', '.jpeg', '.png'))
])

st.markdown(f"### Showing {len(matched_imgs)} images for `{selected_state} — {selected_highway}`")

if matched_imgs:
    num_cols = 3
    cols = st.columns(num_cols)

    for idx, img_file in enumerate(matched_imgs):
        img_path = os.path.join(img_folder, img_file)
        image = Image.open(img_path)
        with cols[idx % num_cols]:
            st.image(image, caption=img_file, use_container_width=True)
else:
    st.warning("No images found for this selection.")