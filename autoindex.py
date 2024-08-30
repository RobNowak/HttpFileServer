#!/bin/python
import argparse
import os
import socket

from flask import Flask
from flask_autoindex import AutoIndex

def http_file_server(directory: str | None = None):
    
    if directory == None:
        dir_env = os.getenv("HFS_DIRECTORY")
        if dir_env != None:
                directory = dir_env
        else:
                directory = os.getcwd()

    app = Flask(__name__)
    app.config.from_prefixed_env()

    AutoIndex(app, browse_root=directory, template_context = dict(SITENAME = socket.gethostname()))
    return app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Http Server with flask auto index to serve a list of files')
    parser.add_argument('-i', '--ip', default='0.0.0.0', type=str,
            help='the hostname to listen to.')
    parser.add_argument('-p', '--port', default=8888, type=int,
            help='the port of the webserver.')
    parser.add_argument('-d', '--directory', default=None, type=str,
            help='the directory to serve.')

    args = parser.parse_args()
    app = http_file_server(args.directory)

    app.run(host=args.ip, port=args.port)
