# -*- coding: utf-8 -*-
from app import create_app

tasksCX = create_app()

# cc:main function
if __name__ == '__main__':
    tasksCX.run(host="127.0.0.1", port=5000)
