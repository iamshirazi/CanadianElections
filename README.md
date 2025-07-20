# Canadian Elections

## Description:
This project uses Python to draw Canada and all of its official ridings, then colours them based on which party won in that riding.

The map of Canada is highly detailed, and allows you to zoom into any part of the country seamlessly.

Will add previous and future elections to this project.

### July 2025 UPDATE:
* Performance has been significantly improved. Loading times have decreased by **98%**
* The 1867 election has been added to the project. Huge thanks to [Dr. Jack Lucas, Dr. Zach Taylor, and Dr. Dave Armstrong](https://borealisdata.ca/file.xhtml?fileId=449029&version=2.0) and their team for creating and publishing the shapefiles for every federal district of every election in Canadian history.
* A landing page was created, so now you can click a button to view any of the elections available
* The Dockerfile was redone, so now you can host this entire project inside of a conatiner

## How to run this project:
1. Clone this repository
2. Run: `pip install -r requirements.txt` to install all necessary libraries
3. Run CanadianElection1867.py, CanadianElection2019.py and CanadianElection2021.py
4. Copy the path of the landing_page.html file
5. Paste the path into your browser to view all of the current electoral maps available
