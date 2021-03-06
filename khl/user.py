from typing import Any, Mapping, Sequence, TYPE_CHECKING

from .hardcoded import API_URL

if TYPE_CHECKING:
    from khl.bot import Bot


class User:
    __slots__ = 'id', 'roles', 'bot'
    """
    presents a User in chat/group

    including other bots
    """
    id: str
    roles: Sequence[str]

    def __init__(self, data: Mapping[str, Any]):
        self.id = data['id']
        self.roles = data['roles'] if data.get('roles') else []
        pass

    @property
    def mention(self):
        return f'(met){self.id}(met)'

    async def grant_role(self, bot: 'Bot', guild_id: str,
                         role_id: int) -> bool:
        return await bot.post(f'{API_URL}/guild-role/grant?compress=0',
                              json={
                                  'user_id': self.id,
                                  'guild_id': guild_id,
                                  'role_id': role_id
                              })

    async def revoke_role(self, bot: 'Bot', guild_id: str,
                          role_id: int) -> bool:
        return await bot.post(f'{API_URL}/guild-role/revoke?compress=0',
                              json={
                                  'user_id': self.id,
                                  'guild_id': guild_id,
                                  'role_id': role_id
                              })
