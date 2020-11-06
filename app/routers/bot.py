from fastapi import APIRouter
from intelmq.bin import intelmqctl

router = APIRouter()
imqc = intelmqctl.IntelMQController()

@router.get('/status/')
async def status(bot_id: str):
    retval, status = imqc.bot_status(bot_id)
    return {'status': status}

@router.get('/start/')
async def start(bot_id: str):
    retval, status = imqc.bot_start(bot_id)
    return {'status': status}

@router.get('/stop/')
async def stop(bot_id: str):
    retval, status = imqc.bot_stop(bot_id)
    return {'status': status}

@router.get('/restart/')
async def restart(bot_id: str):
    retval, status = imqc.bot_restart(bot_id)
    return {'status': status}

@router.get('/reload/')
async def reload(bot_id: str):
    retval, status = imqc.bot_reload(bot_id)
    return {'status': status}

@router.get('/run/')
async def run(bot_id: str):
    retval, status = imqc.bot_run(bot_id)
    return {'status': status}

@router.get('/disable/')
async def disable(bot_id: str):
    retval, status = imqc.bot_disable(bot_id)
    return {'status': status}

@router.get('/enable/')
async def enable(bot_id: str):
    retval, status = imqc.bot_enable(bot_id)
    return {'status': status}
