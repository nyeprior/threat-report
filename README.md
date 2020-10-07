## Threat Roundup Newsletter
### ✨Prereqs:
1. `docker`
2. `docker-compose`

### ✨Running the application:
`git clone https://github.com/nyeprior/threat-roundup.git`
`cd threat-roundup`
`docker-compose up`

Then in your browser navigate to http://localhost


### ✨Using the Application:
Categories are in the navigation bar, simply navigate to any category and see the articles submitted. The number next to each category represents how many articles have been submitted.
To submit a new article, simply enter the URL and the headline of the article and click Submit

### ✨TODO:
- Add functionality to queue submissions for review.
- Add email functionality.
- Adjust HTML output of `/generate` function to be more email-friendly.
