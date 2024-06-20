import os

mode = {
    'generate'  : os.getenv('generate'),
    'upscale'   : os.getenv('upscale'),
    'fusion'    : os.getenv('fusion'),
    'expander'  : os.getenv('expander')
}

head = {
    'bearer'    : os.getenv('bearer')
}