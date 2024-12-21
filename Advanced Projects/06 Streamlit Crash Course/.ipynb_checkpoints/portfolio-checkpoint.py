import streamlit as st

# Configure the layout of the page to use the full page width
st.set_page_config(layout="wide")

# Set the title of the web app
st.title('Welcome to My Portfolio')

st.image('images/DataScientist Sheema Masood.GIF', caption='Sheema Masood - Business Card')

# Enhanced professional title and description
st.header('🌟 Data Scientist | Certified Agentic and Robotic AI Engineer | Aspiring Innovator')
st.subheader('Bridging data-driven insights and cutting-edge AI innovation 🚀 ')

st.markdown("""
As a passionate technologist, I specialize in leveraging **machine learning**, **data analysis**, and **AI engineering** to craft impactful solutions.
""")

st.write("""
Passionate Data Scientist with expertise in machine learning, Generative AI, and data visualization. I excel at transforming complex data into actionable insights and building scalable, AI-driven solutions. My recent work focuses on leveraging advanced AI techniques like LangChain and API integrations to automate workflows and enhance efficiency. Dedicated to pushing technological boundaries, I aim to create innovative solutions that drive value for businesses and society
""")

# Create columns for the main content and the simulated right sidebar
col1, col2 = st.columns([3, 1])

with col1:
    # Main content with project listings
    st.header('Projects')
    st.write("""
    1. **Virtual Navigation Assistant**: An assistive program combining object detection, depth analysis, and audio instructions for visually impaired individuals.
    2. **Streamlit Portfolio Website**: This very website showcasing my projects and skills.
    3. **AI Agent Development (Ongoing)**: Built an AI agent using LangChain and APIs, automating client workflows by integrating various systems for streamlined operations.
    4. **BrisT1D Blood Glucose Levels Prediction (Kaggle)**: Achieved RMSE of 0.09 and ranked 51st on the leaderboard.
    5. **Problematic Internet Use Prediction (Kaggle)**: Top 10% ranking with a 0.49 accuracy score.
    6. **RSNA Spine Disease Classification (Kaggle)**: Achieved 70% accuracy in medical image classification, securing a top 10% leaderboard position.
    7. **Digit Recognition (Kaggle)**: Achieved 100% accuracy using a CNN.
    8. **Object Detection (Kaggle)**: Designed an advanced CNN achieving 92% test accuracy, paired with a user-friendly web interface for intuitive image uploads and instant classification results.
    """)

with col2:
    # Simulated right sidebar for Professional Highlights and Let's Connect
    st.header('Professional Highlights')
    st.markdown("""
    - 💡 Certified in **Agentic and Robotics AI Engineering** with expertise in advanced technologies.
    - 💻 Proficient in developing AI agents using **LangChain**, competing in **Kaggle challenges**, and building scalable, data-driven solutions.
    - 🌱 Continuously exploring emerging technologies and working on **transformative projects**.
    """)
    
    st.header("Let's Connect")
    st.write("""
    - 🌐 [LinkedIn](https://www.linkedin.com/in/sheema-masood/)
    - ✉️ [Email Me](mailto:sheemamasood381@gmail.com)
    - 📊 [Kaggle](https://www.kaggle.com/sheemamasood) 
    - 🖥️ [GitHub](https://github.com/sheemamasood381/)
    """)

# Footer
st.markdown("""
---
#### Powered by Streamlit | Developed by SHEEMA MASOOD
""", unsafe_allow_html=True)
