from fastapi import APIRouter

router = APIRouter()

@router.get('/defaults/')
async def read_defaults():
    pass

@router.put('/defaults/')
async def update_defaults():
    pass

@router.get('/pipeline/')
async def read_pipeline():
    pass

@router.put('/pipeline/')
async def update_pipeline():
    pass

@router.get('/runtime/')
async def read_runtime():
    pass

@router.put('/runtime/')
async def update_runtime():
    pass

@router.get('/harmonization/')
async def harmonization():
    pass
