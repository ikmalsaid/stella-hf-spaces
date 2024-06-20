import os

mode = {
    'describe'  : os.getenv('describe'),
    'upscale'   : os.getenv('upscale'),
    'variate'   : os.getenv('variate'),
    'fusion'    : os.getenv('fusion')
}

head = {
    'bearer'    : os.getenv('bearer')
}