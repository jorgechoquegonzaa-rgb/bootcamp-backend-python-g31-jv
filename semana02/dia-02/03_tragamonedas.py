import random

# PARTE 3 Y 5: CLASE BASE 

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        
        self._creditos = creditos 
        self._total_jugado = 0
        self._total_ganado = 0

    def mostrar(self):
        
        estado = f"S/ {self._creditos}" if self._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"🎰 {self.nombre} — Créditos: {estado}")

    def girar(self):
        
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return

        self._creditos -= apuesta
        self._total_jugado += apuesta
        
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")

    def mostrar_estadisticas(self):
        print(f"   {self.nombre}")
        print(f"   Apostado: S/ {self._total_jugado} | Ganado: S/ {self._total_ganado}")
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   Balance: S/ {signo}{balance} | Créditos actuales: S/ {self._creditos}")
        print()

# PARTE 4: HERENCIA (Máquinas con temas propios)
class TragamonedasFrutas(Tragamonedas):
    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []
        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

class TragamonedasClasico(Tragamonedas):
    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []
        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

# Esta es la máquina personalizada que pide el reto 4B (Mundial)
class TragamonedasMundial(Tragamonedas):
    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]
        resultado = []
        for i in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


    def jugar(self, apuesta):
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()
        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15 # <-- Regla especial: paga x15
            print(f"🏆 ¡TRIPLETE! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif tiene_peru:
            print(f"🇵🇪 ¡Perú apareció! Recuperas tu apuesta de S/ {apuesta}")
            self._creditos += apuesta
        else:
            print(f"😢 Perdiste S/ {apuesta}")

# PARTE 5B: SISTEMA MULTI-MÁQUINA (Menú Principal)

# 1. Creamos las 3 máquinas (Frutas, Clásica y Mundial)
maquinas = [
    TragamonedasFrutas("La Frutal", 200),
    TragamonedasClasico("La Clásica", 300),
    TragamonedasMundial("Mundial 2026", 150)
]


def jugar_en_maquina(maquina):
    while maquina._creditos > 0:
        maquina.mostrar()
        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver al casino): "))
        except ValueError:
            print("❌ Ingresa un número válido.")
            continue

        if apuesta == 0:
            break

        maquina.jugar(apuesta)
        print() 
while True:
    print("\n" + "=" * 35)
    print("      🎰 CASINO ROYALE 🎰")
    print("=" * 35)

    
    for i in range(len(maquinas)):
        m = maquinas[i]
        estado = f"S/ {m._creditos}" if m._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"  {i + 1}. {m.nombre} ({estado})")

    
    print(f"  {len(maquinas) + 1}. Mostrar estadísticas de todas")
    print(f"  {len(maquinas) + 2}. Salir")

    try:
        opcion = int(input("\nElige una opción: "))
    except ValueError:
        print("❌ Opción inválida.")
        continue

    
    if 1 <= opcion <= len(maquinas):
        maquina = maquinas[opcion - 1]
        if maquina._creditos == 0:
            print("💀 Esta maquina está sin creditos. Elige otra.")
        else:
            jugar_en_maquina(maquina)

    
    elif opcion == len(maquinas) + 1:
        print("\n📊 ESTADISTICAS DEL CASINO")
        print("-" * 35)
        for m in maquinas:
            m.mostrar_estadisticas()


    elif opcion == len(maquinas) + 2:
        print("\n💰 Gracias por visitar el Casino Royale. ¡Vuelve pronto!")
        break
    else:
        print("❌ Opción inválida.")

