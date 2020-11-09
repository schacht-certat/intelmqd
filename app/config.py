from pydantic import BaseSettings


class Settings(BaseSettings):
    host = '127.0.0.1'
    port = 42432
    base_path = '/opt/intelmq/etc/'
    defaults_conf = base_path + '/defaults.conf'
    runtime_conf = base_path + '/runtime.conf'
    pipeline_conf = base_path + '/pipeline.conf'
    harmonization_conf = base_path + '/harmonization.conf'

settings = Settings()
