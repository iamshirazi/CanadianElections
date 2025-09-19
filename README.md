# Canadian Elections

## Description:
This project uses Python to draw Canada and all of its official ridings, then colours them based on which party won in that riding.

The map of Canada is highly detailed, and allows you to zoom into any part of the country seamlessly.

Will add previous and future elections to this project.

### September 2025 UPDATE:
* Added the 1872, 1874, 1878, 1882 AND 1887 elections to the project! You can view them under the NEW dropdown menu. Just hover your mouse over the "More" button and select an election.
* Minified elections_style.css in the Dockerfile to decrease loading times (improve performance).

### August 2025 UPDATE:
* [canadianelections.net](https://canadianelections.net) is now **LIVE**! Head over to canadianelections.net to view this entire project!
* Made the elections.html page mobile friendly. The webpage now looks great on both PC and mobile.
* Updated Dockerfile and python scripts. They now function better.

### July 2025 UPDATE:
* Performance has been significantly improved. Loading times have decreased by **98%**
* The 1867 election has been added to the project. Huge thanks to [Dr. Jack Lucas, Dr. Zach Taylor,](https://borealisdata.ca/file.xhtml?fileId=449029&version=2.0) and their team for creating and publishing the shapefiles for every federal district of every election in Canadian history.
* A landing page was created, so now you can click a button to view any of the elections available
* The Dockerfile was redone, so now you can host this entire project inside of a conatiner

## How to run this project:
1. Clone this repository
2. Run: `pip install -r requirements.txt` to install all necessary libraries
3. Run CanadianElection1867.py, CanadianElection2019.py and CanadianElection2021.py
4. Copy the path of the /pages/main/elections.html file
5. Paste the path into your browser to view all of the current electoral maps available
