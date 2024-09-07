import pandas as pd
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_venue_recommendations(location, max_price, type=None):
    from database import get_venues
    venues = get_venues(location, max_price, type)
    df = pd.DataFrame(venues, columns=['id', 'name', 'location', 'type', 'price'])
    return df

def create_schedule(event_type, duration_hours):
    # Basic schedule logic
    activities = {
        'wedding': ['Arrival', 'Ceremony', 'Reception', 'Dinner', 'Dancing'],
        'conference': ['Opening Speech', 'Keynote', 'Breakout Sessions', 'Lunch', 'Networking']
    }
    if event_type not in activities:
        return "Event type not supported."
    
    schedule = activities[event_type]
    return {f"{i+1} Hour(s)": activity for i, activity in enumerate(schedule)}

def process_user_input(user_input):
    # Using LLMChain to process user input with OpenAI
    llm = OpenAI(model="text-davinci-003")
    prompt = PromptTemplate(input_variables=["user_input"], template="Extract the event details from the following input: {user_input}")
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(user_input)
    return response

