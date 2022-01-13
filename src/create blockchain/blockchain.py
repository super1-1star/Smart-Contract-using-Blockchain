

import datetime
import haslib
import json
import flask import Flask,jsonify


class Blockchain:

    def__init__(self):
        self.chain = []
        self.create.block(prof = 1,previous_hash='0')

    def create_block(self,proof,previous_hash):
        
