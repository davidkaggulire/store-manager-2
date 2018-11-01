"""
module run
"""
import os
from api import create_app


app = create_app(os.environ.get('environment_variable')or 'testing')
if __name__ == '__main__':
    app.run()
