# Canadian Elections

## Description:
This project uses Python to draw Canada and all of its official ridings in an election, then colours them based on which party won in that riding. It also displays voting data for all parties in a riding, just hover over or click the riding!

The election maps of Canada are highly detailed, and you can zoom into any part of the country seamlessly.

Will add previous and future elections to this project.

### How to run this project:
1. Find the latest canadianelections Docker image from the official Dockerhub:
[matthewshirazi/canadianelections](https://hub.docker.com/repository/docker/matthewshirazi/canadianelections/tags)

2. Create a simple deployment using the latest canadianelections image:

    `kubectl create deployment local-canadiannelections -n test --image=matthewshirazi/canadianelections:0.0.xx`

    NOTE: Replace `xx` in the above command to the latest version

3. Create a simple NodePort service which targets the pod's port 8080:

    `kubectl create service nodeport local-canadianelections -n test --tcp=80:8080`

4. Get the assigned NodePort:

    `kubectl get services local-canadianelections -n test`

    You'll see NodePort listed after the service port (so if it looks like 80:31125, 31125 is the NodePort)

5. Get the Internal-IP of the node that the local-elections pod is running on

    `kubectl get pods -n test -o wide`

    Then:

    `kubectl get nodes -o wide | grep <node_name>`

    You'll find the Internal-IP for the node there.

6. In your browser, head to `http://<Internal-IP>:<NodePort>/elections/1867.html`

    You'll now be able to view the entire project locally!

### January 2026 UPDATE:
* Added the 1965, 1968, and 1972 elections to the project!
* Added a GitHub Action that scans for vulnerabilites in the Dockerfile.
* Added a GitHub Action that builds the Dockerfile and pushes it to Dockerhub after merging a Pull Request to main

### December 2025 UPDATE:
* Optimized the website for search engines; every election now has its own individual web page.
* Added the 1962 and 1963 elections to the project!

### November 2025 UPDATE:
* Added the 1935, 1940, 1945, 1949, 1953, 1957 and 1958 elections to the project!
* Fully automated pull_voting_data.py, archived the old version of the script.

### October 2025 UPDATE:
* Added parliament charts for each currently available election! Just click the `>` button to see 
the seat makeup in parliament.
* Added the 1900, 1904, 1908, 1911, 1917, 1921, 1925, 1926, and 1930 elections to the project!
* Added favicons, so a maple leaf will appear for this tab in all browsers.

### September 2025 UPDATE:
* Added the 1872, 1874, 1878, 1882, 1887, 1891 AND 1896 elections to the project! You can view them under the NEW dropdown menu. Just hover your mouse over the "More" button and select an election.
* Minified elections_style.css in the Dockerfile to decrease loading times (improve performance).

### August 2025 UPDATE:
* [canadianelections.net](https://canadianelections.net/elections/1867.html) is now **LIVE**! Head over to canadianelections.net to view this entire project!
* Made the elections.html page mobile friendly. The webpage now looks great on both PC and mobile.
* Updated Dockerfile and python scripts. They now function better.

### July 2025 UPDATE:
* Performance has been significantly improved. Loading times have decreased by **98%**
* The 1867 election has been added to the project. Huge thanks to [Dr. Jack Lucas, Dr. Zach Taylor,](https://borealisdata.ca/file.xhtml?fileId=449029&version=2.0) and their team for creating and publishing the shapefiles for every federal district of every election in Canadian history.
* A landing page was created, so now you can click a button to view any of the elections available
* The Dockerfile was redone, so now you can host this entire project inside of a conatiner
