import simpy
import random

# variables para guardar resultados
tiempos_espera = []
clientes_atendidos = 0
clientes_que_esperaron = 0


def cliente(env, nombre, barberos, tiempo_min, tiempo_max):
    global clientes_atendidos
    global clientes_que_esperaron

    llegada = env.now

    print(f"{env.now:.2f} min - {nombre} llega a la barberia")

    with barberos.request() as solicitud:
        yield solicitud

        espera = env.now - llegada
        tiempos_espera.append(espera)

        if espera > 0:
            clientes_que_esperaron += 1

        print(
            f"{env.now:.2f} min - {nombre} comienza su servicio "
            f"(espero {espera:.2f} min)"
        )

        tiempo_servicio = random.randint(tiempo_min, tiempo_max)

        yield env.timeout(tiempo_servicio)

        clientes_atendidos += 1

        print(
            f"{env.now:.2f} min - {nombre} termina su servicio "
            f"({tiempo_servicio} min)"
        )


def generar_clientes(
    env,
    barberos,
    cantidad_clientes,
    tiempo_llegadas,
    tiempo_min,
    tiempo_max
):
    for i in range(1, cantidad_clientes + 1):

        env.process(
            cliente(
                env,
                f"Cliente_{i}",
                barberos,
                tiempo_min,
                tiempo_max
            )
        )

        tiempo = random.randint(
            max(1, tiempo_llegadas - 2),
            tiempo_llegadas + 2
        )

        yield env.timeout(tiempo)


print("===================================")
print(" SIMULACION DE UNA BARBERIA")
print("===================================")

cantidad_barberos = int(input("Numero de barberos: "))
cantidad_clientes = int(input("Numero de clientes a simular: "))
tiempo_llegadas = int(input("Tiempo promedio entre llegadas (min): "))
tiempo_min = int(input("Tiempo minimo de servicio (min): "))
tiempo_max = int(input("Tiempo maximo de servicio (min): "))

env = simpy.Environment()

barberos = simpy.Resource(
    env,
    capacity=cantidad_barberos
)

env.process(
    generar_clientes(
        env,
        barberos,
        cantidad_clientes,
        tiempo_llegadas,
        tiempo_min,
        tiempo_max
    )
)

env.run()

print("\n===================================")
print(" RESULTADOS DE LA SIMULACION")
print("===================================")

if len(tiempos_espera) > 0:
    promedio_espera = sum(tiempos_espera) / len(tiempos_espera)
    mayor_espera = max(tiempos_espera)

    print(f"Clientes atendidos: {clientes_atendidos}")
    print(f"Clientes que esperaron: {clientes_que_esperaron}")
    print(f"Tiempo promedio de espera: {promedio_espera:.2f} min")
    print(f"Mayor tiempo de espera: {mayor_espera:.2f} min")