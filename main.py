from fastapi import FastAPI
import platform, datetime, psutil

app = FastAPI(title='HomeOps API')

@app.get('/')
def root():
    return {'status': 'ok', 'project': 'HomeOps', 'host': platform.node(), 'time': datetime.datetime.utcnow().isoformat()}

@app.get('/health')
def health():
    return {'healthy': True}

@app.get('/metrics')
def metrics():
    disk = psutil.disk_usage('/')
    return {'cpu_percent': psutil.cpu_percent(interval=1), 'ram_percent': psutil.virtual_memory().percent, 'disk_percent': disk.percent, 'uptime_seconds': int(datetime.datetime.now().timestamp() - psutil.boot_time())}

