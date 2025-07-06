import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import math

# Set page config
st.set_page_config(
    page_title="Happy 38th Birthdayn Alissa! 🎉",
    page_icon="🎂",
    layout="wide"
)

# Birthday information
BIRTH_DATE = date(1987, 8, 13)  # Adjust the year based on her actual birth year
BIRTHDAY_2024 = date(2024, 8, 13)
TODAY = date.today()

# Calculate time lived
def calculate_time_lived():
    """Calculate various time units lived"""
    days_lived = (TODAY - BIRTH_DATE).days
    months_lived = days_lived / 30.44  # Average days per month
    hours_lived = days_lived * 24
    minutes_lived = hours_lived * 60
    seconds_lived = minutes_lived * 60
    
    return {
        'days': days_lived,
        'months': months_lived,
        'hours': hours_lived,
        'minutes': minutes_lived,
        'seconds': seconds_lived
    }

time_data = calculate_time_lived()

# Main title
st.title("🎂 Happy 38th Birthday! 🎉")
st.markdown("### Celebrating the amazing time you've been alive!")

# Create a beautiful layout
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Days Lived",
        value=f"{time_data['days']:,}",
        delta="+1 today!"
    )

with col2:
    st.metric(
        label="Months Lived", 
        value=f"{time_data['months']:,.1f}",
        delta="Growing every day!"
    )

with col3:
    st.metric(
        label="Hours Lived",
        value=f"{time_data['hours']:,}",
        delta="+24 today!"
    )

with col4:
    st.metric(
        label="Minutes Lived",
        value=f"{time_data['minutes']:,}",
        delta="+1,440 today!"
    )

with col5:
    st.metric(
        label="Seconds Lived",
        value=f"{time_data['seconds']:,}",
        delta="+86,400 today!"
    )

st.markdown("---")



# Fun facts section
st.markdown("---")
st.subheader("🎉 Fun Facts About Your Time on Earth!")

col1, col2 = st.columns(2)

with col1:
    st.info(f"**You've lived through approximately {time_data['days'] // 365} birthdays!**")
    st.info(f"**You've experienced about {time_data['days'] // 4} seasons!**")
    st.info(f"**You've seen roughly {time_data['days'] // 7} weekends!**")

with col2:
    st.success(f"**You've lived through {time_data['days'] // 30} full moons!**")
    st.success(f"**You've experienced about {time_data['days'] // 365} New Years!**")
    st.success(f"**You've had approximately {time_data['days']} sunrises and sunsets!**")

# Countdown to next birthday
days_to_birthday = (BIRTHDAY_2024 - TODAY).days
if days_to_birthday > 0:
    st.warning(f"🎂 Only {days_to_birthday} days until your 38th birthday!")
elif days_to_birthday == 0:
    st.balloons()
    st.success("🎉 TODAY IS YOUR BIRTHDAY! 🎉")
else:
    st.info("🎂 Your birthday has passed this year! Here's to many more!")

# Footer
st.markdown("---")
st.markdown("*Made with ❤️ for your special day*") 