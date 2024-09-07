import streamlit as st
from utils import get_venue_recommendations, create_schedule, process_user_input

def main():
    st.title('Dynamic Event Planning Assistant')

    st.sidebar.header('User Preferences')
    event_type = st.sidebar.selectbox('Event Type', ['Wedding', 'Conference'])
    location = st.sidebar.text_input('Location')
    max_price = st.sidebar.number_input('Max Budget (in INR)', min_value=0)
    
    if st.sidebar.button('Get Recommendations'):
        st.subheader('Venue Recommendations')
        df = get_venue_recommendations(location, max_price, event_type.lower())
        st.dataframe(df)
    
    st.sidebar.header('Create Schedule')
    duration_hours = st.sidebar.number_input('Event Duration (in hours)', min_value=1)
    
    if st.sidebar.button('Generate Schedule'):
        schedule = create_schedule(event_type.lower(), duration_hours)
        st.subheader('Event Schedule')
        st.write(schedule)
    
    st.sidebar.header('User Input')
    user_input = st.sidebar.text_area('Describe your event:')
    
    if st.sidebar.button('Process Input'):
        response = process_user_input(user_input)
        st.subheader('Processed Information')
        st.write(response)

if __name__ == "__main__":
    main()
