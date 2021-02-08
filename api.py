
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from utilities import get_uptime




# --- Welcome to your Emily API! --- #

# See the README for guides on how to test it.

# Your API endpoints under http://yourdomain/api/...
# are accessible from any origin by default.
# Make sure to restrict access below to origins you
# trust before deploying your API to production.

config_file = 'config.json'
config = json.load(open(config_file))

app = FastAPI()


@app.get('/api/health')
def healthcheck():
    return {
        'uptime': get_uptime(),
        'status': 'UP',
        'host': config['connection']['host'],
        'port': config['connection']['port'],
    }


@app.get('/api')
def hello():
    import os
    files = os.listdir('paralenz-image-classifier')
    s = (f'The {config["project_name"]} API is running (uptime: {get_uptime()}) files at mounted drive: {[str(f) for f in files]}')
    return s

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # When deploying, remember to change this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(
        'api:app',
        host=config['connection']['host'],
        port=config['connection']['port']
    )

