from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..world import World
    from ..organism import Organism

class WorldRule:
    name = "rule"

    def on_attach(self, world: "World") -> None:
        """Po dodaniu do świata (tu np. zarejestruj przechodnie typy komórek)."""
 
    def on_detach(self, world: "World") -> None:
        """Przy usuwaniu ze świata (tu posprzątaj po sobie)."""
 
    def on_step_start(self, world: "World") -> None:
        """Początek tury (np. odrastanie jedzenia)."""
 
    def on_organism_tick(self, world: "World", organism: "Organism") -> None:
        """Dla każdego żywego organizmu, po jego ruchu (np. metabolizm)."""
 
    def on_enter(self, world: "World", organism: "Organism", x: int, y: int, previous: int) -> None:
        """Organizm wszedł na pole (x, y); `previous` to kod, który tam był (np. FOOD)."""
 
    def on_blocked(self, world: "World", organism: "Organism", x: int, y: int, content: int) -> None:
        """Organizm próbował wejść na nieprzechodnie pole (np. walka z innym organizmem)."""
 
    def on_step_end(self, world: "World") -> None:
        """Koniec tury."""


