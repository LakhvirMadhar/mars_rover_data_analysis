# Mars Rover Exploratory Data Analysis

This exploratory data analysis project aims to provide insights into the Mars rover missions using data retrieved from the Mars Rover Photo API.

## Project Overview

The analysis covers:

- **Basic Rover Info**: Presents essential information about each rover, including launch and landing dates, status, total photos taken, and the duration of missions.

- **Mission Data Analysis**: Explores the time taken for each rover to reach Mars, mission lengths for completed missions, and identifies which rover had the longest mission.

- **Photos Data Analysis**: Analyzes the total number of photos taken by each rover, the sol/earth dates with the most photos, calculates the average and median photos taken, and provides visualizations of the top 25 frequencies at which photos were taken.

- **Dates Analysis**: Investigates the largest gaps between photo sessions and provides visualizations of the frequency of photo-taking sessions.

## Project Setup

There are two primary Python files for this project:

- **mars_rover_json_creation.py**: This script fetches each rover's manifest data from the NASA API and saves it as local JSON files.

- **mars_rover_eda.py**: The core script that conducts exploratory data analysis on the Mars rover data that we've stored in our local JSON files.

## Results

The following questions were addressed as part of the exploratory data analysis:

### *Basic Rover Info*

      Curiosity Rover:  
      Launch Date: 2011-11-26  
      Landing Date: 2012-08-06  
      Status: Active  
      Max Sol: 4102  
      Max Date: 2024-02-19  
      Total Photos: 695,670  

      Opportunity Rover:  
      Launch Date: 2003-07-07  
      Landing Date: 2004-01-25  
      Status: Complete  
      Max Sol: 5111  
      Max Date: 2018-06-11  
      Total Photos: 198,439  

      Spirit Rover:  
      Launch Date: 2003-06-10  
      Landing Date: 2004-01-04  
      Status: Complete  
      Max Sol: 2208  
      Max Date: 2010-03-21  
      Total Photos: 124,550  

## *Mission Data Analysis*

### How long did it take each rover to get to Mars?
      The Curiosity rover took 254 Earth days to land on Mars.  
      The Opportunity rover took 202 Earth days to land on Mars.  
      The Spirit rover took 208 Earth days to land on Mars.  

### If the status of a rover is complete, how long was their mission?   
      Opportunity Rover:  
      Landing Date: 2004-01-25  
      Final Mission Date: 2018-06-11  
      Mission Length: 5,251 Earth days (14.38 Earth years)  

      Spirit Rover: 
      Landing Date: 2004-01-04  
      Final Mission Date: 2010-03-21  
      Mission Length: 2,268 Earth days (6.21 Earth years)  

      The Opportunity rover had the longest mission of 5,251 Earth days!  

## *Photos Data Analysis*

### Which rover has taken the most photos? 
      The Curiosity rover has taken 695,670 photos.  
      The Opportunity rover has taken 198,439 photos.  
      The Spirit rover has taken 124,550 photos.  

      The Curiosity rover has taken the most photos, for a total of 695,670 photos!  

### For each rover, what sol(s)/earth date(s) had the most photos taken?  
      Curiosity Rover: 
      Max Total Photos: 3,702  
      Sol Date: 0  
      Earth Date: 2012-08-06  

      Opportunity Rover:  
      Max Total Photos: 346  
      Sol Date: 60  
      Earth Date: 2004-03-26  

      Spirit Rover:  
      Max Total Photos: 415  
      Sol Date: 433  
      Earth Date: 2005-03-23  

### On average, how many photos did each rover take per Sol?  
      The Curiosity rover took an average of 187.16 photos per Sol.  
      The Opportunity rover took an average of 41.25 photos per Sol.  
      The Spirit rover took an average of 58.89 photos per Sol.  

### What was the median amount of photos taken?  
      The Curiosity rover took a median of 138 photos per Sol.  
      The Opportunity rover took a median of 32 photos per Sol.  
      The Spirit rover took a median of 43 photos per Sol.  

### What are the top 25 photo frequencies for each rover?  
![Curiosity_Rover_Top_25_Photo_Frequencies](https://github.com/user-attachments/assets/20606f04-aeb9-4f10-aa18-0b6b60ddc7ed)
![Opportunity_Rover_Top_25_Photo_Frequencies](https://github.com/user-attachments/assets/6c24b788-1daf-4f30-8975-08b2ff22ecb3)
![Spirit_Rover_Top_25_Photo_Frequencies](https://github.com/user-attachments/assets/64ce0ab3-e1ae-4ef9-aa57-6e82d6f87440)


## *Dates Analysis*

### What's the longest time gap between photo sessions for each rover?  
      The Curiosity rover's longest sol gap time is 27 sols.  
      The Opportunity rover's longest sol gap time is 15 sols.  
      The Spirit rover's longest sol gap time is 12 sols.  

### What were the time gap frequencies for each rover?"  
![Curiosity_Rover_Time_Gap_Frequencies_2012-08-06_to_2024-02-19](https://github.com/user-attachments/assets/ab5fac30-2016-4e73-830e-5c8420632ae3)
![Opportunity_Rover_Time_Gap_Frequencies_2004-01-25_to_2018-06-11](https://github.com/user-attachments/assets/b43d15e8-247a-47a7-a742-45ee396017a5)
![Spirit_Rover_Time_Gap_Frequencies_2004-01-04_to_2010-03-21](https://github.com/user-attachments/assets/29c9c898-60e2-4a3a-b339-769fa0963aa1)

## Acknowledgements

- [NASA API](https://api.nasa.gov/) - For providing the API to access the Mars Rover Photo data.  
