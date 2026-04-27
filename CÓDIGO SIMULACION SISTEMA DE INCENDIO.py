class SistemaIncendio:
    def __init__(self):
        self.central_activa = True
        self.alarma_sonando = False

    def recibir_señal(self, dispositivo):
        print(f"\n--- [CENTRAL DE INCENDIO] ---")
        print(f"[INFO] Señal de emergencia recibida de: {dispositivo}")
        self.activar_alarma()

    def activar_alarma(self):
        self.alarma_sonando = True
        print("!!! ALERTA GENERAL !!!")
        print(">> Sirena activada en todo el edificio.")
        print(">> Mensaje en Repetidores: PROCEDER A LA EVACUACIÓN.")
        print("-----------------------------\n")

# --- Simulación Interactiva ---
central = SistemaIncendio()

print("Panel de Control del Espacio Común")
print("1. Activar Detector de Humo (Automático)")
print("2. Accionar Pulsador Manual (Manual)")
print("3. Salir de la simulación")

opcion = input("\nSeleccione qué evento ocurre (1/2/3): ")

if opcion == "1":
    dispositivo = "Detector de Humo - Sector A"
    central.recibir_señal(dispositivo)
elif opcion == "2":
    dispositivo = "Pulsador Manual de Emergencia - Pasillo Central"
    central.recibir_señal(dispositivo)
elif opcion == "3":
    print("Simulación finalizada.")
else:
    print("Opción no válida. El sistema sigue en modo vigilancia.")