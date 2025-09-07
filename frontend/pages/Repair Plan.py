import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

# ————— Load data and map full state names —————
df = pd.read_csv(r"C:\Users\SHREY\Desktop\gnctd\Area of Damage Results\Final List.csv")
df["Traffic Severity Score"] = pd.to_numeric(df["Traffic Severity Score"], errors="coerce").fillna(0)
df["Total_Damage_Area"] = pd.to_numeric(df["Total_Damage_Area"], errors="coerce").fillna(0)

state_name_map = {
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "RS": "Rio Grande do Sul"
}
df["State"] = df["State"].map(state_name_map).fillna(df["State"])

# ————— Filters —————
st.subheader("📍 Select States and Highways to Analyze")
all_states = df["State"].unique().tolist()
selected_states = st.multiselect("States", all_states, default=all_states)

filtered_df = df[df["State"].isin(selected_states)]

all_highways = sorted(filtered_df["Highway Name"].unique().tolist())
selected_highways = st.multiselect("Highways", all_highways, default=all_highways)

filtered_df = filtered_df[filtered_df["Highway Name"].isin(selected_highways)]

st.markdown("---")

# ————— Priority selectors —————
st.subheader("🎯 Choose Your Priority Levels")
col1, col2 = st.columns(2)

with col1:
    traffic_choice = st.radio(
        "⚡ Traffic Severity Priority",
        ("Low", "Normal", "High"),
        index=1,
        help="How important is traffic severity in ordering repairs?"
    )
with col2:
    area_choice = st.radio(
        "🛣️ Area of Damage Priority",
        ("Low", "Normal", "High"),
        index=1,
        help="How important is total damage area in ordering repairs?"
    )

st.markdown("---")

# ————— Generate button —————
if st.button("▶️ Generate Repair Priority List"):

    if filtered_df.empty:
        st.warning("No segments found for the selected state/highway filters.")
    else:
        # Apply priority weights
        weight_map = {"Low": 5, "Normal": 10, "High": 20}
        w_traffic = weight_map[traffic_choice]
        w_area = weight_map[area_choice]

        # Compute weighted score
        filtered_df["Raw Priority Score"] = (
            filtered_df["Traffic Severity Score"] * w_traffic *
            filtered_df["Total_Damage_Area"] * w_area
        )

        # Normalize score into [1, 10]
        min_s, max_s = filtered_df["Raw Priority Score"].min(), filtered_df["Raw Priority Score"].max()
        if max_s > min_s:
            filtered_df["Repair Priority Score"] = 1 + 9 * (filtered_df["Raw Priority Score"] - min_s) / (max_s - min_s)
        else:
            filtered_df["Repair Priority Score"] = 1.0

        # Sort results
        filtered_df = filtered_df.sort_values("Repair Priority Score", ascending=False).reset_index(drop=True)

        # Prepare final display
        df_display = filtered_df[["State", "Highway Name", "Repair Priority Score"]].copy()
        df_display.index += 1
        df_display.index.name = "S. No."

        st.subheader("🔧 Repair Priority List")
        st.dataframe(df_display.style.format({"Repair Priority Score": "{:.2f}"}))

        # ————— Show Images by Segment —————
        st.markdown("---")
        st.subheader("🖼️ View Damage Images by Segment")

        img_folder = r"C:\Users\SHREY\Desktop\gnctd\frontend\Visualization"

        for _, row in filtered_df.head(10).iterrows():
            state_code_full = row["State"]
            orig_state_code = [k for k, v in state_name_map.items() if v == state_code_full][0]

            highway_name = row["Highway Name"]
            identifier = f"{orig_state_code}_{highway_name.replace('-', '')}"

            with st.expander(f"📍 {state_code_full} — {highway_name}"):
                matched_imgs = [
                    f for f in os.listdir(img_folder)
                    if f.startswith(f"{orig_state_code}_{highway_name}") and f.lower().endswith(('.jpg', '.jpeg', '.png'))
                ][:5]

                if matched_imgs:
                    cols = st.columns(len(matched_imgs))
                    for i, img_file in enumerate(matched_imgs):
                        img_path = os.path.join(img_folder, img_file)
                        image = Image.open(img_path)
                        cols[i].image(image, caption=img_file, use_container_width=True)
                else:
                    st.info("No images found for this segment.")

        # ————— CSV Download Button —————
        csv = df_display.to_csv().encode("utf-8")
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="RAPID_repair_priority_list.csv",
            mime="text/csv"
        )