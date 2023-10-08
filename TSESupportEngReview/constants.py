endpoint = 'https://getcolor.atlassian.net/rest/api/2/search?'

jql = (
    'jql=resolved%20>%3D%202023-08-01%20' + 'AND' +
    '%20resolved%20<%3D%202023-09-01%20' + 'AND' +
    '%20project%20%3D%20SUPPORT%20' + 'AND' +
    '%20status%20in%20(DONE%2C%20Done)%20' + 'AND' +
    '%20priority%20in%20("P2%20(Medium)"%2C%20"P3%20(Low)"%2C%20"P4%20(Lowest)")' +
    '%20order%20by%20created%20DESC'
)

url = endpoint + jql

