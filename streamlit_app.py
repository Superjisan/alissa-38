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

# Chinese Zodiac information for 1987
CHINESE_ZODIAC_1987 = "Rabbit"  # 1987 was the Year of the Rabbit
ZODIAC_ELEMENT = "Fire"  # Fire Rabbit
ZODIAC_DESCRIPTION = "Fire Rabbit - Creative, intelligent, and compassionate"

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

# Chinese Zodiac section
st.subheader("🐰 Your Chinese Zodiac Sign")

# Create zodiac info cards
col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"**Zodiac Animal:** {CHINESE_ZODIAC_1987}")

with col2:
    st.success(f"**Element:** {ZODIAC_ELEMENT}")

with col3:
    st.warning(f"**Year:** 1987")

# Zodiac characteristics
st.markdown(f"**{ZODIAC_DESCRIPTION}**")

# Create a chart showing Chinese Zodiac cycle
st.subheader("📊 Chinese Zodiac Cycle")

# Chinese Zodiac animals in order
zodiac_animals = [
    "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
    "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
]

# Create data for the chart
zodiac_data = pd.DataFrame({
    'Animal': zodiac_animals,
    'Position': range(1, 13),
    'Is_Your_Year': [animal == CHINESE_ZODIAC_1987 for animal in zodiac_animals]
})

# Create a bar chart highlighting the Rabbit year
fig = px.bar(
    zodiac_data,
    x='Animal',
    y='Position',
    color='Is_Your_Year',
    title="Chinese Zodiac Animals (Highlighting Your Year - Rabbit)",
    color_discrete_map={True: '#FF6B6B', False: '#4ECDC4'},
    labels={'Position': 'Zodiac Position', 'Is_Your_Year': 'Your Year'}
)

fig.update_layout(
    title_font_size=20,
    height=400,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

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