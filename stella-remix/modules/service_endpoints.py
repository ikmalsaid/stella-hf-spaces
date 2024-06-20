import os

mode = {
    'remix'     : os.getenv('remix'),
    'describe'  : os.getenv('describe'),
    'upscale'   : os.getenv('upscale'),
    'fusion'    : os.getenv('fusion')
}

head = {
    'bearer'    : os.getenv('bearer')
}