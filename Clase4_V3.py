
class Medicamento:
    def __init__(self, nombre, dosis):
        self.__nombre = nombre
        self.__dosis = dosis


class Mascota:
    def __init__(self, nombre, historia_clinica, peso, genero, fecha_ingreso):
        self.__nombre = nombre
        self.historia_clinica = historia_clinica
        self.__peso = peso
        self.genero = genero
        self.fecha_ingreso = fecha_ingreso
        self.medicamentos = []

class Sistema:
    def __init__(self):
        self.mascotas_caninos = []
        self.mascotas_felinos = []

    def ingresar_mascota(self, mascota):
        if mascota.genero == "canino":
            if len(self.mascotas_caninos) < 10 and not self.verificar_historia_clinica(mascota.historia_clinica):
                self.mascotas_caninos.append(mascota)
                return True
        elif mascota.genero == "felino":
            if len(self.mascotas_felinos) < 10 and not self.verificar_historia_clinica(mascota.historia_clinica):
                self.mascotas_felinos.append(mascota)
                return True
        return False

    def verificar_historia_clinica(self, historia_clinica):
        for mascota in self.mascotas_caninos + self.mascotas_felinos:
            if mascota.historia_clinica == historia_clinica:
                return True
        return False

    def ver_fecha_ingreso(self, historia_clinica):
        for mascota in self.mascotas_caninos + self.mascotas_felinos:
            if mascota.historia_clinica == historia_clinica:
                return mascota.fecha_ingreso
        return None

    def ver_numero_mascotas(self):
        total_mascotas = len(self.mascotas_caninos) + len(self.mascotas_felinos)
        print(f"Número de mascotas en el servicio: {total_mascotas}")

    def ver_medicamentos(self, historia_clinica):
        for mascota in self.mascotas_caninos + self.mascotas_felinos:
            if mascota.historia_clinica == historia_clinica:
                return mascota.medicamentos
        return []

    def eliminar_mascota(self, historia_clinica):
        for mascota in self.mascotas_caninos:
            if mascota.historia_clinica == historia_clinica:
                self.mascotas_caninos.remove(mascota)
                return True
        for mascota in self.mascotas_felinos:
            if mascota.historia_clinica == historia_clinica:
                self.mascotas_felinos.remove(mascota)
                return True
        return False

                
        



def main():
    sis= Sistema()

    while True:
        print("\nOpciones:")
        print("1. Ingresar mascota al servicio")
        print("2. Ver fecha de ingreso de una mascota")
        print("3. Ver número de mascotas en el servicio")
        print("4. Ver medicamentos de una mascota")
        print("5. Eliminar una mascota del servicio")
        print("6. Salir")

        opcion = int(input("Ingrese el número de la opción: "))

        if opcion == 1:
            # Ingresar una mascota
            nombre = input("Nombre de la mascota: ")
            historia_clinica = input("Número de historia clínica: ")
            genero = input("Tipo de mascota (canino o felino): ")
            peso = float(input("Peso de la mascota: "))
            fecha_ingreso = input("Fecha de ingreso (dd/mm/aaaa): ")
            mascota = Mascota(nombre, historia_clinica, genero, peso, fecha_ingreso)

            if sis.ingresar_mascota(mascota):
                print("Mascota ingresada exitosamente.")
            else:
                print("No se pudo ingresar la mascota.")

        elif opcion == 2:
            # Ver fecha de ingreso de una mascota
            historia_clinica = input("Número de historia clínica de la mascota: ")
            fecha = sis.ver_fecha_ingreso(historia_clinica)
            if fecha:
                print(f"Fecha de ingreso: {fecha}")
            else:
                print("No se encontró la mascota.")

        elif opcion == 3:
            # Ver número de mascotas en el servicio
            sis.ver_numero_mascotas()

        elif opcion == 4:
            # Ver medicamentos de una mascota
            historia_clinica = input("Número de historia clínica de la mascota: ")
            medicamentos = sis.ver_medicamentos(historia_clinica)
            if medicamentos:
                print("Medicamentos:")
                for medicamento in medicamentos:
                    print(f"Nombre: {medicamento.nombre}, Dosis: {medicamento.dosis}")
            else:
                print("No se encontró la mascota.")

        elif opcion == 5:
            # Eliminar una mascota del servicio
            historia_clinica = input("Número de historia clínica de la mascota a eliminar: ")
            if sis.eliminar_mascota(historia_clinica):
                print("Mascota eliminada exitosamente.")
            else:
                print("No se pudo eliminar la mascota.")

        elif opcion == 6:
            # Salir
            break

        else:
            print("Opción inválida. Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()

        
        
        
        
        
        
        