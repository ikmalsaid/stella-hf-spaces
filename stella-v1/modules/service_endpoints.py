import os

mode = {
    'generate'  : os.getenv('generate'),
    'upscale'   : os.getenv('upscale'),
    'fusion'    : os.getenv('fusion')
}

head = {
    'bearer'    : os.getenv('bearer')
}