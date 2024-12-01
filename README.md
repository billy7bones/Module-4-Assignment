# Module-4-Assignment
# Netflix Data Visualization

## Overview
This project analyses Netflix's dataset to gain insights into genres and ratings distribution. Both Python and R are used for data preparation, cleaning, exploration, and visualization. A key part of this analysis involved splitting the `listed_in` column, which lists multiple genres for a single show, into individual genres for more accurate insights.

## Files
- `analysis.py`: Python script for data analysis and visualizations.
- `netflix_visualization.R`: R script for creating visualizations.
- `Netflix_shows_movies.csv`: The dataset.
- Images:
  - `Figure_1_Ratings_Distribution_Histogram.png`: Histogram of ratings distribution (Python).
  - `Figure_2_Most_Watched_Genres_Bar_Chart.png`: Bar chart of most watched genres (Python).
  - `Rplot01_Most_Watched_Genres.png`: Bar chart of most watched genres (R).

## Data Preparation
- The dataset was loaded and cleaned in both Python and R.
- The `listed_in` column, which contains genres, was split into individual genres in both Python and R to ensure proper analysis and visualization.

## How to Run
### Python:
1. Open `analysis.py` in Visual Studio.
2. Run the script using **F5** or `Debug > Start Debugging`.

### R:
1. Open `netflix_visualization.R` in RStudio.
2. Run the script to generate the R visualization.

## Output
- **Python**:
  - Bar plot of most watched genres (saved as `Figure_2_Most_Watched_Genres_Bar_Chart.png`).
  - Histogram of ratings distribution (saved as `Figure_1_Ratings_Distribution_Histogram.png`).
- **R**:
  - Bar plot of most watched genres (saved as `Rplot01_Most_Watched_Genres.png`).

## Key Insights
1. **Drama** emerged as the most popular genre, with a significant lead over other genres like **Comedy** and **Action**.
2. The majority of Netflix content is rated **TV-MA**, indicating a strong focus on adult-oriented programming.

## Key Insights from Data Preparation
- Splitting the `listed_in` column provided a detailed breakdown of genres, ensuring accurate visualization of the most watched genres.
- The ratings distribution visualization offered insights into the distribution of content ratings across the dataset.
