import streamlit as st
import langchain_helper

# Set page configuration
st.set_page_config(page_title="Cuisine Explorer", layout="wide")
st.title("🍽️ Cuisine Explorer")

# Sidebar for user inputs
with st.sidebar:
    st.header("Customize Your Experience")
    cuisine = st.selectbox("Pick a Cuisine", ["Select a Cuisine", "Indian", "Italian", "Mexican", "Arabic", "American", "Japanese", "Korean"], index=0)
    generate_button = st.button("Generate Restaurant Name and Menu")

# Check for the need to generate new restaurant info
if generate_button and (cuisine != "Select a Cuisine"):
    if 'last_cuisine' not in st.session_state or cuisine != st.session_state['last_cuisine']:
        # Generate and store new restaurant information
        restaurant_info = langchain_helper.generate_restaurant_name_and_items(cuisine)
        st.session_state['restaurant_info'] = restaurant_info
        st.session_state['last_cuisine'] = cuisine
    else:
        # Reuse existing restaurant information if cuisine hasn't changed
        restaurant_info = st.session_state['restaurant_info']
else:
    # Initialize with empty data to avoid errors
    restaurant_info = {'restaurant_name': '', 'menu_items': ''}

# Display logic for restaurant name and menu items
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("✨ Restaurant Name")
    if restaurant_info['restaurant_name']:  # Check if there's a restaurant name to display
        st.markdown(f"### {restaurant_info['restaurant_name']}")

with col2:
    st.subheader("📜 Menu Items")
    if restaurant_info['menu_items']:
        # Split and strip menu items, ensure uniqueness
        menu_items = list(set([item.strip() for item in restaurant_info['menu_items'].split(",")]))
        # Display each menu item
        for item in menu_items:
            st.markdown(f"- {item}")

# Information message for user guidance
if cuisine == "Select a Cuisine":
    st.info("Please select a cuisine to get started.")

