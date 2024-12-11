# множественного наследования
class PowerSupply:
    def __init__(self, power):
        self.power = power

    def supply_power(self):
        print(f"Блок питания подает напряжение: {self.power}W")

class Motherboard:
    def __init__(self, chipset):
        self.chipset = chipset

    def distribute_power(self):
        print(f"Материнская плата с чипсетом {self.chipset} распределяет напряжение.")

class CPU:
    def __init__(self, frequency, cores):
        self.frequency = frequency
        self.cores = cores

    def activate_turbo(self):
        print(f"Процессор активирует турбо-режим на частоте {self.frequency}GHz и {self.cores} ядрах.")

class RAM:
    def __init__(self, capacity, frequency):
        self.capacity = capacity
        self.frequency = frequency

    def load_data(self):
        print(f"ОЗУ объемом {self.capacity}GB загружает данные.")

    def unload_data(self):
        print(f"ОЗУ объемом {self.capacity}GB выгружает данные.")

class SSD:
    def __init__(self, capacity):
        self.capacity = capacity

    def save_data(self):
        print(f"SSD объемом {self.capacity}GB сохраняет данные.")

    def delete_data(self):
        print(f"SSD объемом {self.capacity}GB удаляет данные.")

class GPU:
    def __init__(self, model, memory):
        self.model = model
        self.memory = memory

    def display_image(self):
        print(f"Видеокарта {self.model} с памятью {self.memory}GB выводит изображение на экран.")

class PersonalComputer(PowerSupply, Motherboard, CPU, RAM, SSD, GPU):
    def __init__(self, power, chipset, frequency, cores, ram_capacity, ram_frequency, ssd_capacity, gpu_model, gpu_memory):
        PowerSupply.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, frequency, cores)
        RAM.__init__(self, ram_capacity, ram_frequency)
        SSD.__init__(self, ssd_capacity)
        GPU.__init__(self, gpu_model, gpu_memory)

# композиции

class ComputerComponent:
    def __init__(self, name):
        self.name = name

class CompositeComputer:
    def __init__(self, power_supply, motherboard, cpu, ram, ssd, gpu):
        self.power_supply = power_supply
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.gpu = gpu

    def start_computer(self):
        self.power_supply.supply_power()
        self.motherboard.distribute_power()
        self.cpu.activate_turbo()
        self.ram.load_data()
        self.ssd.save_data()
        self.gpu.display_image()

# множественного наследования
pc = PersonalComputer(500, "B550", 3.8, 8, 16, 3200, 1024, "RTX 3080", 10)
pc.supply_power()
pc.distribute_power()
pc.activate_turbo()
pc.load_data()
pc.save_data()
pc.display_image()

#  композиции
power_supply = PowerSupply(500)
motherboard = Motherboard("B550")
cpu = CPU(3.8, 8)
ram = RAM(16, 3200)
ssd = SSD(1024)
gpu = GPU("RTX 3080", 10)

composite_pc = CompositeComputer(power_supply, motherboard, cpu, ram, ssd, gpu)
composite_pc.start_computer()

