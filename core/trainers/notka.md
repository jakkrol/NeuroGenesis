# Architektura Projektu: Trenerzy i Cykl Życia Symulacji

## 1. Hierarchia Czasu (Kto kogo wywołuje?)

Łańcuch wywołań w każdej klatce symulacji wygląda następująco:
**`SimWindow`** ➔ **`Trainer.step()`** ➔ **`World.step()`**

*   **`SimWindow` (UI)**: Zna tylko Trenera (przez interfejs `BaseTrainer`). W głównej pętli wywołuje `trainer.step()` i rysuje planszę. Kompletnie ignoruje fizykę i zasady ewolucji.
*   **`Trainer` (Zarządca)**: Odpowiada za makro-skalę (eksperyment). Woła `world.step()`, a następnie nasłuchuje zdarzeń ze Świata (np. koniec pokolenia, zdobycie jedzenia), żeby wywołać mutację lub dać nagrodę.
*   **`World` (Fizyka)**: Sterylna piaskownica. W `step()` zarządza mikro-skalą: wiekiem organizmów, widzeniem (`get_orientation`), wywoływaniem u nich `decide()` i fizycznym ruchem (`act()`).

## 2. Komunikacja Zdarzeniowa (Event-Driven)

Świat (`World`) nie sprawdza, kiedy włączyć ewolucję i nie ma warunków typu `if ewolucja: ...`. 
Zamiast tego Świat ma callbacki i rzuca zdarzenia w void:

```python
# W World:
if len(self.organisms) == 0:
    for listener in self.on_all_dead_listeners:
        listener()

# W GeneticTrainer (w __init__):
self.world.on_all_dead_listeners.append(self.ewoluuj)