import os
from pathlib import Path # this librabry actually helps in getting the path format from any OS becuase windows uses '/' where as mac uses '\' so to be compatablie use this librbary


project_name = 'us_visa'

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",#this is used to create as an constructor file.Inside that folder the below files which are presetn under components are created
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",#configuration is an a folder so we kept an __init__.py files
    f"{project_name}/constants/__init__.py",#constant is an a folder so we kept an __init__.py files
    f"{project_name}/entity/__init__.py",#entity is an a folder so we kept an __init__.py files
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
    else:
        print(f"File is already present at:{filepath}")
 