import glob
import json
from fastapi import FastAPI
from typing import List, Union
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    path: str = None
    type: str = None
    magnification: int = None
    datetime: str = None


class Component(BaseModel):
    name: str = None
    amount: float = None
    unit: str = None


class Cycle(BaseModel):
    repeat: int = None
    temperature: float = None
    timedelta: int = None
    images: List[Image] = None


class DNA(BaseModel):
    name: str = None
    components: List[Component] = None
    cycles: List[Cycle] = None
    start_date: str = None
    end_date: str = None


class RNA(BaseModel):
    yields: float = None
    start_date: str = None
    end_date: str = None


class State(BaseModel):
    type: str = None
    coating: str = None
    init_cell_number: int = None
    components: List[Component] = None
    images: List[Image] = None
    start_date: str = None
    end_date: str = None


class Condition(BaseModel):
    dna: List[DNA] = None
    rna: List[RNA] = None
    states: List[State] = None
    start_date: str = None
    end_date: str = None
    

class Experiment(BaseModel):
    conditions: List[Condition] = None
    start_date: str = None
    end_date: str = None


@app.get('/experiments')
async def get_experiments():

    experiments = []
    for path in glob.iglob('experiments/*'):
        with open(path) as f:
            experiment = json.load(f)
            experiments.append(experiment)
    
    return experiments


@app.post('/experiments')
async def update_experiment(experiment: Experiment):

    experiment = experiment.dict()

    paths = glob.iglob('experiments/*')
    paths = [int(path[12:-5]) for path in paths]
    id = max(paths) + 1 if len(paths) else 0

    with open(f'experiments/{id}.json', 'x') as f:
        json.dump(experiment, f, indent=2)

    return experiment


@app.get('/experiments/{id}')
async def get_experiments(id: int):

    with open(f'experiments/{id}.json') as f:
        experiment = json.load(f)
    
    return experiment


@app.put('/experiments/{id}')
async def get_experiments(id: int, experiment: Experiment):

    experiment = experiment.dict()

    with open(f'experiments/{id}.json', 'w') as f:
        json.dump(experiment, f, indent=2)

    return experiment


@app.post('/experiments')
async def update_experiment(experiment: Experiment):

    experiment = experiment.dict()

    paths = glob.iglob('experiments/*')
    paths = [int(path[12:-5]) for path in paths]
    id = max(paths) + 1 if len(paths) else 0

    with open(f'experiments/{id}.json', 'x') as f:
        json.dump(experiment, f, indent=2)

    return experiment


@app.get('/experiments/{id}')
async def get_experiments(id: int):

    with open(f'experiments/{id}.json') as f:
        experiment = json.load(f)
    
    return experiment


@app.put('/experiments/{id}')
async def get_experiments(id: int, experiment: Experiment):

    experiment = experiment.dict()

    with open(f'experiments/{id}.json', 'w') as f:
        json.dump(experiment, f, indent=2)

    return experiment
