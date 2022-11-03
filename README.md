# Twitter Data Pipeline using Airflow

In this project, we are testing [Airflow](https://github.com/apache/airflow/) which allows to programmatically author, schedule, and monitor workflows. The goal is to create an End-To-End Data Engineering application by extracting data using Twitter API and save it.



## Steps

- Create a twitter account and create a new application in the [Developer Platform](https://developer.twitter.com/). Then, generate and save keys and tokens.

- Create a python project to collect data from twitter, extract text, hashtags, links, mentions and emojis from tweets, and save the results to a csv file.

- Create the DAG file by defining the default arguments, instantiating a DAG object and using an operator which define a unit of work for Airflow to complete.

- Trigger DAG using Airflow web interface and check the generated output file.

## Installation 

- Install the requirements
```bash
pip install -r requirements.txt
```

- Copy python scripts to airflow/dags folder

- Configure secrets.json file with your twitter project credentials and the output folder
```bash 
{
    "API_KEY": "",
    "API_KEY_SECRET": "",
    "BEARER_TOKEN": "",
    "ACCESS_TOKEN": "",
    "ACCESS_TOKEN_SECRET": "",
    "OUTPUT_PATH": ""
}
```

- Starting Airflow Standalone 
```bash 
airflow standalone
```




 
