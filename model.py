from __future__ import annotations

from typing import List, TYPE_CHECKING

import states

if TYPE_CHECKING:
    from actor import Actor
    from gamemap import GameMap


class Model:
    """The model contains everything from a session which should be saved."""

    active_map: GameMap

    def __init__(self) -> None:
        self.log: List[str] = []

    @property
    def player(self) -> Actor:
        return self.active_map.player

    def report(self, text: str) -> None:
        print(text)
        self.log.append(text)

    def is_player_dead(self) -> bool:
        """True if the player had died."""
        return not self.player.fighter or self.player.fighter.hp <= 0

    def loop(self) -> None:
        while True:
            if self.is_player_dead():
                states.GameOver(self).loop()
                continue
            self.active_map.scheduler.invoke_next()
