import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

# ————— Page config —————
st.set_page_config(page_title="RAPID", page_icon="🚧", layout="wide")

# ————— Centered Title —————
st.markdown("<h1 style='text-align: center; font-size: 3em;'>🚧 RAPID</h1>", unsafe_allow_html=True)

# ————— Styles —————
st.markdown(
    """
    <style>
    .section-box {
        background-color: #5A5A5A;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        color: #FF5F4D;
        margin-bottom: 10px;
    }
    .section-text {
        font-size: 16px;
        line-height: 1.7;
    }
    .reference {
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 8px;
    }
    a {
        color: #1f77b4;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ————— About Section —————
st.markdown("""
<div class="section-box">
  <div class="section-title">🛣️ About RAPID</div>
  <div class="section-text">
    <b>RAPID</b> — <em>Road Assessment & Prioritized Intervention for Damage</em> — is an intelligent road damage evaluation and repair prioritization system developed by 
    <a href="https://www.linkedin.com/in/shrey-jaiswal-1a7724272/" target="_blank"><b>Shrey Jaiswal</b></a> during his internship under 
    <a href="https://www.linkedin.com/in/dr-arjun-ghosh-2005321a5/" target="_blank">Dr. Arjun Ghosh</a> (Data Processing Assistant) and 
    <a href="https://www.linkedin.com/in/murugan-k-9259084/?originalSubdomain=in" target="_blank">Mr. K Murugan</a> (Joint Director, IT Department), GNCTD.
    <br><br>
    It identifies and quantifies road damage, integrates usage and structural indicators, and outputs a ranked intervention plan — ensuring optimal use of limited maintenance budgets.
  </div>
</div>
""", unsafe_allow_html=True)

# ————— Workflow Section —————
st.markdown("""
<div class="section-box">
  <div class="section-title">🧠 System Workflow</div>
  <div class="section-text">
    1. <b>Computer Vision Stage</b>:  
    Semantic segmentation models detect cracks and potholes in images and calculate total damaged area per segment using model ensembles.
    <br><br>
    2. <b>Traffic Weighting Stage</b>:  
    A traffic severity score is computed using:
    <ul>
      <li><b>Road-specific metrics</b>: average lanes, speed limit</li>
      <li><b>State-specific metrics</b>: population, urbanization</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

# ————— Frontend Utility Section —————
st.markdown("""
<div class="section-box">
  <div class="section-title">⚙️ Frontend Utility</div>
  <div class="section-text">
    This tool helps maintenance officers:
    <ul>
      <li>Filter by <b>states</b> and <b>highways</b></li>
      <li>Adjust the <b>weight of damage area</b> and <b>traffic severity</b></li>
      <li>Generate a <b>ranked repair plan</b></li>
      <li>View <b>segment-specific road images</b></li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

# ————— Dataset Section —————
st.markdown("""
<div class="section-box">
  <div class="section-title">📂 Dataset</div>
  <div class="section-text">
    Source:  
    <a href="https://data.mendeley.com/datasets/t576ydh9v8/4" target="_blank">
    Passos, Bianka T. <i>et al.</i> (2020), “Cracks and Potholes in Road Images”, Mendeley Data, V4</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ————— References Section —————
st.markdown("""
<div class="section-box">
  <div class="section-title">📚 References</div>
  <div class="reference">[1] <a href="https://escholarship.org/uc/item/3q21f88p" target="_blank">Volker, Jamey & Handy, Susan. <i>Increasing Highway Capacity Induces More Auto Travel</i> (2023)</a></div>
  <div class="reference">[2] <a href="https://www.sciencedirect.com/science/article/pii/S096585642200026X" target="_blank">Bucsky, Péter & Juhász, Mattias. <i>Long-term evidence on induced traffic: Budapest bridges</i>. Transp. Research Part A, 157 (2022): 244–257</a></div>
  <div class="reference">[3] <a href="https://www.sciencedirect.com/science/article/pii/S1877042813045308" target="_blank">Bains, Manraj Singh <i>et al.</i> <i>Effect of speed limit compliance on Indian expressways</i>. Procedia – Social & Behavioral Sciences, 104 (2013): 458–467</a></div>
  <div class="reference">[4] <a href="https://www.tandfonline.com/doi/full/10.1080/19427867.2017.1374007" target="_blank">Arkatkar, Shriniwas S. <i>Traffic operations & capacity analysis in India</i>. Transportation Letters 10.2 (2018): 65–67</a></div>
  <div class="reference">[5] <a href="https://mednexus.org/doi/full/10.1016/j.cjtee.2019.07.004" target="_blank">Sun, Li-Lu <i>et al.</i> <i>Road traffic safety: Cross-effects of economic, road, and population factors</i>. Chinese Journal of Traumatology, 22.05 (2019): 290–295</a></div>
</div>
""", unsafe_allow_html=True)

# ————— Call to Action —————
st.markdown("---")
st.info("Go to the **Repair Plan** page using the sidebar to generate and visualize road repair priorities.")
