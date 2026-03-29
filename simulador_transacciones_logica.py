# PROYECTO: SISTEMA DE GESTIÓN Y VALIDACIÓN DE TRANSACCIONES FINANCIERAS
# Objetivo: Implementar protocolos de seguridad y reportes estadísticos de sesión.

pin_seguridad = 1234
saldo_disponible = 500
intentos_fallidos = 0
historial_transacciones = []

print("--- BIENVENIDO AL SISTEMA DE GESTIÓN FINANCIERA ---")

# Fase 1: Validación de Seguridad
while True:
    acceso = int(input("Ingrese su PIN de seguridad: "))
    if acceso == pin_seguridad:
        print("\nAUTENTICACIÓN EXITOSA. Acceso concedido.")
        break
    
    intentos_fallidos += 1
    if intentos_fallidos == 3:
        print("\nALERTA: Tarjeta bloqueada por seguridad. Contacte a su banco.")
        break
    print(f"PIN incorrecto. Intentos restantes: {3 - intentos_fallidos}")

# Fase 2: Operaciones y Captura de Datos
if acceso == pin_seguridad:
    while True:
        monto_retiro = int(input("\nIngrese la cantidad a retirar (o -1 para finalizar): "))
        
        if monto_retiro == -1:
            break
        
        if monto_retiro > saldo_disponible:
            print(f"OPERACIÓN RECHAZADA: Saldo insuficiente. Disponible: ${saldo_disponible}")
            continue 
        
        # Actualización de saldo y registro en historial
        saldo_disponible -= monto_retiro
        historial_transacciones.append(monto_retiro)
        
        print(f"TRANSACCIÓN EXITOSA: Se ha retirado ${monto_retiro}")
        print(f"Saldo actual en cuenta: ${saldo_disponible}")

# Fase 3: Reporte Estadístico de la Sesión
if len(historial_transacciones) > 0:
    print("\n" + "="*45)
    print("      REPORTE DE AUDITORÍA DE TRANSACCIONES      ")
    print("="*45)
    print(f"Número total de operaciones:  {len(historial_transacciones)}")
    print(f"Volumen total transaccionado: ${sum(historial_transacciones)}")
    print(f"Operación de mayor cuantía:   ${max(historial_transacciones)}")
    # Aplicamos formato de 2 decimales para precisión financiera
    promedio = sum(historial_transacciones) / len(historial_transacciones)
    print(f"Ticket promedio por retiro:   ${promedio:.2f}")
    print("="*45)
else:
    print("\nSESIÓN FINALIZADA: No se registraron movimientos.")
        
        
