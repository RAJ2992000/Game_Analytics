import streamlit as st
import mysql.connector
import pandas as pd

# Set page layout to wide
st.set_page_config(layout="wide")

def get_data():
   
    db_connection = mysql.connector.connect(
        host="localhost",     
        user="root",           
        password="Neethiuma@123",  
        database="sportsanalytics"     
    )
    
    cursor = db_connection.cursor(dictionary=True)  
    cursor.execute("""
        SELECT a.name, b.ranks, a.country, b.points, b.movement, b.competitions_played 
        FROM competitors_table a 
        JOIN competitor_ranking_table b 
        ON a.competitor_id = b.competitor_id
    """)
    data = cursor.fetchall()
    
    db_connection.close()
    return data

def display_dashboard(data):
    df = pd.DataFrame(data)

    # Summary statistics
    total_competitors = df.shape[0]
    total_countries = df['country'].nunique()
    highest_points = df['points'].max()

    # Create a three-column layout: Left for filters, Center for title, summary, and image, Right for leaderboards
    left_column, center_column, right_column = st.columns([1, 2, 1])

    with center_column:
        # Add CSS for styling and animations
        st.markdown("""
        <style>
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes slideInFromLeft {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(0); }
        }
        @keyframes scaleUp {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes bounceIn {
            0% { transform: scale(0.8); opacity: 0; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(1); }
        }

        .fade-in {
            animation: fadeIn 2s ease-out forwards;
        }
        .slide-in-left {
            animation: slideInFromLeft 1.5s ease-out forwards;
        }
        .scale-up {
            animation: scaleUp 2s ease-out forwards;
        }
        .bounce-in {
            animation: bounceIn 2s ease-out forwards;
        }

        .content {
            position: relative;
            z-index: 1;
            padding: 20px;
        }

        .large-title {
            font-size: 4em; /* Increase the size of the title */
            font-weight: bold;
            text-align: center;
            color: #FFD700;
        }
        </style>
        """, unsafe_allow_html=True)

        # Add the animated title with scaling and bouncing effects
        st.markdown('<div class="content"><div class="large-title bounce-in">🏆 Sports Analytics Dashboard 🏅</div></div>', unsafe_allow_html=True)

        # Add the image directly below the title
        st.markdown('<div class="content"><img src="https://img.freepik.com/free-photo/sports-tools_53876-138077.jpg?t=st=1734848390~exp=1734851990~hmac=d34cfa5d5bc8d93ff7d7271522593edd66842e33e778d229dc65eb2a77aac83d&w=996" width="100%" alt="Sports Tools Image"></div>', unsafe_allow_html=True)

        # Add a nice header for the summary
        st.markdown('<div class="content"><h2>🏆 Dashboard Summary 🏅</h2></div>', unsafe_allow_html=True)

        # Add fade-in animation for Total Competitors
        st.markdown(f'<div class="content fade-in"><div class="typing-stat">📊 **Total Competitors:** {total_competitors} 🏅</div></div>', unsafe_allow_html=True)

        # Add slide-in animation for Countries Represented
        st.markdown(f'<div class="content slide-in-left"><div class="typing-stat">🌍 **Countries Represented:** {total_countries} 🌏</div></div>', unsafe_allow_html=True)

        # Add scale-up animation for Highest Points Scored
        st.markdown(f'<div class="content scale-up"><div class="typing-stat">🎯 **Highest Points Scored by a Competitor:** {highest_points} 🥇</div></div>', unsafe_allow_html=True)

    with right_column:
        # Leaderboards Section: Display Top-Ranked Competitors
        st.markdown("### 🥇 Top-Ranked Competitors 🥇")
        top_ranked = df.sort_values(by="ranks").head(10)  # Top 10 competitors by rank
        st.dataframe(top_ranked[['name', 'ranks', 'country', 'points']])

        # Leaderboards Section: Display Competitors with Highest Points
        st.markdown("### 🎯 Competitors with the Highest Points 🎯")
        highest_points_competitors = df.sort_values(by="points", ascending=False).head(10)  # Top 10 competitors by points
        st.dataframe(highest_points_competitors[['name', 'points', 'ranks', 'country']])

    with left_column:
        # Search Box to search for competitors by name
        search_query = st.text_input("Search Competitor by Name:", "")
        
        # Rank Range Filter
        rank_range = st.slider("Filter by Rank Range", min_value=int(df['ranks'].min()), max_value=int(df['ranks'].max()), 
                               value=(int(df['ranks'].min()), int(df['ranks'].max())))

        # Filter by Country
        country = st.selectbox("Filter by Country", ['All'] + list(df['country'].unique()))

        # Filter by Points Threshold
        points_threshold = st.slider("Filter by Points Threshold", min_value=int(df['points'].min()), max_value=int(df['points'].max()), 
                                     value=int(df['points'].min()))

        # Reset Button to clear all filters
        reset_button = st.button("Reset Filters")
        
        # Reset all filters if the button is clicked
        if reset_button:
            search_query = ""
            rank_range = (int(df['ranks'].min()), int(df['ranks'].max()))
            country = 'All'
            points_threshold = int(df['points'].min())

        # Apply filters if the values are set
        if search_query:
            # Trim whitespace and handle missing data properly
            search_query = search_query.strip()
            df = df[df['name'].str.contains(search_query, case=False, na=False)]
        
        df = df[(df['ranks'] >= rank_range[0]) & (df['ranks'] <= rank_range[1])]
        if country != 'All':
            df = df[df['country'] == country]
        df = df[df['points'] >= points_threshold]

        # Displaying the filtered data in a table (only the rows that match the search query and other filters)
        st.subheader('📊 Filtered Competitor Data:')
        st.dataframe(df)

        # Competitor Details Viewer (Displayed when a search query is entered)
        if search_query:
            if not df.empty:
                # Assume the first match for now, or you can modify this to allow multiple results
                competitor_details = df.iloc[0]
                st.subheader(f"🏅 Details for {competitor_details['name']} 🏆")
                st.write(f"**Rank**: {competitor_details['ranks']}")
                st.write(f"**Rank Movement**: {competitor_details['movement']}")
                st.write(f"**Competitions Played**: {competitor_details['competitions_played']}")
                st.write(f"**Country**: {competitor_details['country']}")
                st.write(f"**Points**: {competitor_details['points']}")
            else:
                st.write("No competitor found with the given name.")

data = get_data()

display_dashboard(data)
