# Game Analytics: Unlocking Tennis Data with SportRadar API

## Project Overview
The **SportRadar Event Explorer** project aims to create a comprehensive solution for managing, visualizing, and analyzing tennis competition data extracted from the Sportradar API. This application will parse JSON data, store structured information in a relational database, and provide interactive insights into tournaments, competition hierarchies, and event details. It is tailored for sports enthusiasts, analysts, and organizations to understand competition structures and trends while exploring detailed event-specific information.

## Skills Acquired
- **Python Scripting**: Automating data extraction and transformation.
- **Data Collection via API Integration**: Interfacing with the Sportradar API.
- **Data Management Using SQL**: Designing and managing relational databases.
- **Streamlit**: Building intuitive dashboards and interactive visualizations.

## Domain
**Sports / Data Analytics**

## Problem Statement
The Sportradar Event Explorer project addresses the need for an intuitive system to manage and analyze sports data. By leveraging the Sportradar API, the solution will:
- Parse and transform complex JSON data.
- Store the information in a structured relational database.
- Provide tools for interactive visualization and trend analysis of sports events.

## Business Use Cases
1. **Event Exploration**: Enable users to navigate competition hierarchies (e.g., ATP Vienna events).
2. **Trend Analysis**: Visualize the distribution of events by type, gender, and competition level.
3. **Performance Insights**: Analyze player participation across singles and doubles events.
4. **Decision Support**: Deliver data-driven insights to event organizers or sports bodies for resource allocation.

## Approach
### 1. Data Extraction
- Connect to the Sportradar API to retrieve competition data.
- Parse and extract relevant information from JSON responses.
- Transform nested JSON structures into flat, relational data suitable for analysis.

### 2. Data Storage
- Design a SQL database schema tailored to sports data.
  - Define appropriate data types and relationships.
  - Implement primary and foreign keys to maintain data integrity.
- Store parsed data for easy querying and analysis.

### 3. Data Analysis & Visualization
- Use Python libraries (e.g., Pandas, Matplotlib) to analyze stored data.
- Develop an interactive dashboard using Streamlit to:
  - Visualize competition trends.
  - Explore player participation and event distributions.

### 4. Insights Delivery
- Generate insights into competition structures and participation trends.
- Provide actionable recommendations for event organizers and sports analysts.

## Technologies Used
- **Python**: For scripting and data processing.
- **Sportradar API**: Data source for tennis event information.
- **SQL**: Relational database for structured data storage.
- **Streamlit**: Dashboard creation and data visualization.

## Expected Outcomes
- A robust system for parsing and storing sports data.
- Intuitive dashboards for exploring competition hierarchies and trends.
- Actionable insights to aid sports decision-making processes.

---

### Repository Structure
```
/README.md       # Project documentation
/data            # Raw and processed data files
/scripts         # Python scripts for API integration and data processing
/database        # SQL schema and database files
/dashboard       # Streamlit application files
```

### Getting Started
1. Clone this repository.
2. Install the required Python libraries from `requirements.txt`.
3. Obtain API access credentials from Sportradar.
4. Run the data extraction script to populate the database.
5. Launch the Streamlit dashboard to explore insights interactively.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with detailed explanations of changes.

---
**Author**: RAJ KUMAR
**Contact**: raju2992000@gmai.com
