from fastapi import APIRouter
from intelmq.bin import intelmqctl

router = APIRouter()
imqc = intelmqctl.IntelMQController()

@router.get('/status/')
async def status():
    retval, botnet_status = imqc.botnet_status()
    return botnet_status

@router.get('/start/')
async def start():
    retval, botnet_status = imqc.botnet_start()
    return botnet_status

@router.get('/stop/')
async def stop():
    retval, botnet_status = imqc.botnet_stop()
    return botnet_status

@router.get('/restart/')
async def restart():
    retval, botnet_status = imqc.botnet_restart()
    return botnet_status

@router.get('/reload/')
async def reload():
    retval, botnet_status = imqc.botnet_reload()
    return botnet_status
