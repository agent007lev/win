
import r2r_dac as r2r
import math
import time

# --- Функция генерации синуса ---
def get_sin_wave_amplitude(t, frequency, amplitude=1.0, offset=0.0):
    """
    Возвращает значение синуса в момент времени t.
    t - время в секундах
    frequency - частота в Гц
    amplitude - амплитуда
    offset - смещение (чтобы не уходило в минус)
    """
    return offset + amplitude * math.sin(2 * math.pi * frequency * t)

# --- Основные настройки ---
amplitude = 1.5
offset = 1.5  # Поднимаем синус вверх, чтобы он был от 0 до 3.0 В
signal_frequency = 0.5  # Гц
sampling_frequency = 1000  # Гц (как часто обновляем ЦАП)

if __name__ == "__main__":
    try:
        # Инициализация ЦАП
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2, True)
        times = 0.0

        print("Генерация синуса запущена. Нажмите Ctrl+C для остановки.")
       
        while True:
            # 1. Получаем значение с помощью нашей функции
            signal = get_sin_wave_amplitude(t, frequency)(times, signal_frequency, amplitude, offset)
            times = wait_for_sampling_period(sampling_frequency)
            # 2. Отправляем на ЦАП
            dac.set_voltage(signal)
           
            # 3. Ждем до следующего шага
            time.sleep(1.0 / sampling_frequency)
           
            # 4. Увеличиваем время
            times += 1.0 / sampling_frequency

    except KeyboardInterrupt:
        print("\nОстановка...")
    finally:
        # Обязательно отключаем ЦАП при выходе
        dac.deinit()





