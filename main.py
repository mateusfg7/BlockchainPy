# main blockchain
blockchain = []


def get_sha256(string) -> str:
    import hashlib

    if type(string) != str:
        string = str(string)

    return hashlib.sha256(string.encode()).hexdigest()


def addBlockToBlockchain(block):
    if len(blockchain) == 0:
        # make genesis block (first block of blockchain)
        block['hash'] = get_sha256(block)
    else:
        # get last block in blockchain
        last_block = blockchain[len(blockchain) - 1]

        # vinculate the hash block with last hash block
        block['hash'] = last_block['hash']

        # get hash of block
        block['hash'] = get_sha256(block)

    blockchain.append(block)


# block
block_1 = {
    'transations': [
        {
            'sender': 'Mateus',
            'recipient': 'Felipe',
            'value': 5
        },
        {
            'sender': 'jack',
            'recipient': 'Chan',
            'value': 1
        },
        {
            'sender': 'Daniel',
            'recipient': 'Fraga',
            'value': 500
        },
        {
            'sender': 'Satoshi',
            'recipient': 'Nakamoto',
            'value': 900
        },
    ]
}

# block
block_2 = {
    'transations': [
        {
            'sender': 'Tony',
            'recipient': 'Stark',
            'value': 456
        },
        {
            'sender': 'Goku',
            'recipient': 'Vegeta',
            'value': 36
        },
    ]
}

# block
block_3 = {
    'transations': [
        {
            'sender': 'Fulano1',
            'recipient': 'Fulano2',
            'value': 789
        },
        {
            'sender': 'Ze',
            'recipient': 'Orlickas',
            'value': 15
        },
        {
            'sender': 'Ubiratan',
            'recipient': 'Taki',
            'value': 2
        },
    ]
}


addBlockToBlockchain(block_1)
addBlockToBlockchain(block_2)
addBlockToBlockchain(block_3)


# SHOW THE BLOCKS
position = 1
for block in blockchain:
    print(f'\nBlock #{position}: {block["hash"]}')
    for transaction in block['transations']:
        print('')
        print(f'sender: {transaction["sender"]}')
        print(f'recipient: {transaction["recipient"]}')
        print(f'value: {transaction["value"]}')
    position += 1
