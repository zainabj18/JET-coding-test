# Restaurant Data Finder

Using the **Just Eat API**, this program fetches restaurant data based on a given postcode and displays the following details of 10 relevant restaurants:
- Name
- Cuisines
- Rating
- Address

## How to Run the Script

### Prerequisites
- Python 3.10 
- Internet connection to fetch API data

### Installation
1. Clone the repository:

   git clone https://github.com/zainabj18/JET-coding-test.git 

2. Install required dependencies. 
This script uses the built-in `requests` module. If it's not installed, run:
   
   pip install requests
   

### Running the Script

1. Open a terminal and navigate to the script directory.
2. Run the script:

   python restaurants.py

3. Enter a UK postcode when prompted.
4. Choose sorting option:
   - Enter `1` to sort by rating (Highest rated first)
   - Enter `2` for a random order
   - Inavlid input defaults to random order
5. The top 10 relevant restaurants will be displayed.

## Assumptions
- **Keyword Filtering**: The API sometimes returns non-restaurant businesses (e.g., CEX). To filter out irrelevant results, only restaurants with relevant cuisine-related keywords (e.g., "Pizza", "Grill", "Sushi") are included.
- **Sorting**: Users can choose to sort results by rating (descending order) or in a random order.
- **Error Handling**: Prevents crashes by defaulting to random sorting if invalid input is given.


## Possible Improvements
- **Better Filtering**: A more advanced approach (e.g., checking multiple fields instead of just cuisine keywords) could improve accuracy.
- **GUI/Web Interface**: A graphical user interface or web app would make the output more user-friendly.
- **More Sorting Options**: Allow users to sort by distance, popularity, or other factors.
- **Even more and advanved error handling**

## Author
- **Zainab Jaffar**


