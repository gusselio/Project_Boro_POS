from modulos.datos import inventario, stock_inicial, notificaciones_compra

def refresh_notificaciones():
    """
    Recalcula notificaciones_compra a partir del inventario y stock_inicial.
    Llama esto cada vez que cambie inventario manualmente o por ventas.
    """
    # Limpiar primero
    notificaciones_compra.clear()

    for insumo, cantidad_actual in inventario.items():
        # Si no tenemos un stock_inicial registrado, inicializamos con el actual
        if insumo not in stock_inicial or stock_inicial.get(insumo, 0) == 0:
            # evita división por cero; asumimos que el stock inicial ahora es el actual
            stock_inicial[insumo] = cantidad_actual

        inicial = stock_inicial[insumo]
        # si por alguna razón inicial es 0, saltamos cálculo de porcentaje
        if inicial == 0:
            if cantidad_actual <= 0:
                notificaciones_compra[insumo] = "⚠️ Agotado"
            continue

        porcentaje = (cantidad_actual / inicial) * 100
        if cantidad_actual <= 0:
            notificaciones_compra[insumo] = "⚠️ Agotado"
        elif porcentaje <= 25:
            notificaciones_compra[insumo] = f"{cantidad_actual} unidades restantes ({porcentaje:.1f}%)"

def ver_notificaciones():
    print("\n==============================")
    print("       NOTIFICACIONES")
    print("==============================")
    if not notificaciones_compra:
        print("✅ Todo está bien, no hay artículos por comprar.")
    else:
        print("⚠️ Debes reabastecer los siguientes artículos:\n")
        for insumo, estado in notificaciones_compra.items():
            print(f"- {insumo}: {estado}")
    print()