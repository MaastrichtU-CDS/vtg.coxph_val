# cox_validation

## Repo Description

This repo contains the validation scripts for the Federated Cox Regression Algorithm https://github.com/IKNL/vtg.coxph. 

Input -- Beta Values Obtained from Training the Cox Regression Algorithm.
Output -- Concordance Index

## Dockerizing the algorithm
    1. Clone the repository to your local machine 
    2. cd vtg.coxph_val/
    3. The repo contains a [Dockerfile](https://github.com/MaastrichtU-CDS/vtg.coxph_val/blob/main/Dockerfile) which can be used to build the docker image. Follow the commands below 
               - docker build -t <docker_image_name> . 
               - docker tag <docker_image_name> <docker_repository_name/docker_image_name>
               - docker push <docker_repository_name/docker_image_name> 

## Adapting the code for your project 
The code supplied in the repository comes with a data filtering script that is custom-built for the project Atomcat2. If you want to adapt it for your project, make changes to the file [here](https://github.com/MaastrichtU-CDS/vtg.coxph_val/blob/main/coxph_validate/apply_filters.py)


## Using the code with Vantage6 Infrastructure

An example Jupyter Notebook can be found [here](https://github.com/MaastrichtU-CDS/vtg.coxph_val/blob/main/atomCAT2validation.ipynb)


  



