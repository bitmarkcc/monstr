import asyncio
import logging
import sys
from monstr.client.client import Client, ClientPool
from monstr.encrypt import Keys
from monstr.event.event import Event

urls = ['ws://localhost:8090','wss://nos.lol','wss://relay.primal.net','wss://relay.snort.social','wss://relay.damus.io','wss://wot.utxo.one','wss://nostrelites.org','wss://wot.nostr.party','wss://wot.girino.org']

async def do_post(text):
    """
        Example showing how to post a text note (Kind 1) to relay
    """

    # Xmark bridge key
    n_keys = Keys.get_key("nsecmyprivatekey")
    n_msg = Event(kind=Event.KIND_TEXT_NOTE,
                  content=text,
                  pub_key=n_keys.public_key_hex())
    n_msg.sign(n_keys.private_key_hex())

    for url in urls:
        async with Client(url) as c:
            c.publish(n_msg)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    text = sys.argv[1]
    asyncio.run(do_post(text))
