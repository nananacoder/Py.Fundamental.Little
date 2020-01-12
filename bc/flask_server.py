#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

import json
import hashlib
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, request
from flask.json import jsonify

from blockchain import BlockChain

# our node
app = Flask(__name__)
# generate a globally unique address for this node
node_idetifier = str(uuid4()).replace('-', '')

# instantiate
blockchain = BlockChain()


# to tell our server to mine a new lock
@app.route('/mine', methods=['GET'])
def mine():
    """
    1.calculate the Proof of Work;
    2. Reward the miiner(us) by adding a transaction granting us 1 coin;
    3. Forge the new Block by adding it to the chain.
    :return:
    """
    # run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # must receive a reward for finding the proof
    # sender is '0' to signify that this node has mined a new coin
    blockchain.new_transaction(
        sender="0",
        recipient=node_idetifier,
        amount=1)

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']}
    return jsonify(response), 200


# to create a new transaction to a block
# we'll sending date to it
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


# to return the full Blockchain
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


# adding transactions to a block
@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    """
    check that the required fields are in the POST'ed data
    create a new transaction
    :return:
    """
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': "New nodes have been added",
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', method=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    response = {
        'message': 'Our chain was replaced',
        'new_chain': blockchain.chain
    } if replaced else {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
    pass
