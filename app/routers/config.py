from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config import settings

import json

router = APIRouter()

@router.get('/defaults/')
async def read_defaults():
    data = json.load(open(settings.defaults_conf))
    return data

@router.put('/defaults/')
async def update_defaults(defaults: str):
    data = json.loads(defaults)
    with open(settings.defaults_conf, 'w') as outfile:
        json.dump(data, outfile)
    return data

@router.get('/pipeline/')
async def read_pipeline():
    data = json.load(open(settings.pipeline_conf))
    return data

@router.put('/pipeline/')
async def update_pipeline(pipeline: str):
    data = json.loads(pipeline)
    with open(settings.pipeline_conf, 'w') as outfile:
        json.dump(data, outfile)
    return data

@router.get('/runtime/')
async def read_runtime():
    data = json.load(open(settings.runtime_conf))
    return data

@router.put('/runtime/')
async def update_runtime(runtime: str):
    data = json.loads(runtime)
    with open(settings.runtime_conf, 'w') as outfile:
        json.dump(data, outfile)
    return data

@router.get('/harmonization/')
async def harmonization():
    data = json.load(open(settings.harmonization_conf))
    return data
