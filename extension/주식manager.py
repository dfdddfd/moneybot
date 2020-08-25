from dbjson import Database
from asyncio import sleep
from random import choice

class Manager:
    db = Database('database/주식.json')

    async def update_loop(self, name: str, seconds: int = 60):
        while True:
            await sleep(seconds)
            self.db[name] += choice(range(-50, 51))
            self.db.commit()
    
    def get(self, name: str) -> int: return self.db[name]
