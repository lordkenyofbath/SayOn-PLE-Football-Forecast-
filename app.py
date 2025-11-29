import streamlit as st
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="SayOn Football Forecast",
    page_icon="⚽",
    layout="wide"
)

# Title
st.title("⚽ SayOn Premier League Forecast")
st.markdown("### 2025-26 Season | Ken's Prediction Game")

# Premier League 2025-26 Season - Matchweek 13 (Nov 29-30, 2025)
fixtures = [
    {"id": 1, "home": "Brentford", "away": "Burnley"},
    {"id": 2, "home": "Manchester City", "away": "Leeds United"},
    {"id": 3, "home": "Sunderland", "away": "Bournemouth"},
    {"id": 4, "home": "Everton", "away": "Newcastle United"},
    {"id": 5, "home": "Tottenham", "away": "Fulham"},
    {"id": 6, "home": "Crystal Palace", "away": "Manchester United"},
    {"id": 7, "home": "Aston Villa", "away": "Wolves"},
    {"id": 8, "home": "Nottingham Forest", "away": "Brighton"},
    {"id": 9, "home": "West Ham", "away": "Liverpool"},
    {"id": 10, "home": "Chelsea", "away": "Arsenal"}
]

# Deadline info
st.info(f"📅 **Matchweek 13** - Deadline: Friday 28 Nov 2025 at 20:00 GMT")

# Initialize session state for predictions
if 'predictions' not in st.session_state:
    st.session_state.predictions = {}
    st.session_state.submitted = False

# Display fixtures and collect predictions
st.markdown("---")
st.subheader("Enter Your Predictions")

for fixture in fixtures:
    col1, col2, col3, col4, col5 = st.columns([3, 1, 0.5, 1, 3])
    
    with col1:
        st.markdown(f"**{fixture['home']}**")
    
    with col2:
        home_score = st.number_input(
            f"home_{fixture['id']}", 
            min_value=0, 
            max_value=15, 
            value=st.session_state.predictions.get(fixture['id'], {}).get('home', 0),
            key=f"home_{fixture['id']}",
            label_visibility="collapsed"
        )
    
    with col3:
        st.markdown("<div style='text-align: center; padding-top: 8px;'><b>-</b></div>", unsafe_allow_html=True)
    
    with col4:
        away_score = st.number_input(
            f"away_{fixture['id']}",
            min_value=0,
            max_value=15,
            value=st.session_state.predictions.get(fixture['id'], {}).get('away', 0),
            key=f"away_{fixture['id']}",
            label_visibility="collapsed"
        )
    
    with col5:
        st.markdown(f"**{fixture['away']}**")
    
    # Store predictions
    st.session_state.predictions[fixture['id']] = {
        'home': home_score,
        'away': away_score,
        'match': f"{fixture['home']} vs {fixture['away']}"
    }
    
    st.markdown("<br>", unsafe_allow_html=True)

# Submit button
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Submit All Predictions", type="primary", use_container_width=True):
        st.session_state.submitted = True
        st.balloons()

# Show submitted predictions
if st.session_state.submitted:
    st.success("🎉 Predictions submitted successfully!")
    
    st.markdown("---")
    st.subheader("Your Predictions for Matchweek 13:")
    
    for fixture_id, prediction in st.session_state.predictions.items():
        st.markdown(f"**{prediction['match']}:** `{prediction['home']} - {prediction['away']}`")
    
    # Reset button
    st.markdown("---")
    if st.button("Edit Predictions"):
        st.session_state.submitted = False
        st.rerun()

# Footer
st.markdown("---")
st.caption("SayOn Football Forecast v1.0 | Built for Ken")
