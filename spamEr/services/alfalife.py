from service import Service


class AlfaLife(Service):
    async def run(self):
        await self.post(
            "https://alfalife.cc/auth.php", data={"phone": self.phone},
        )
