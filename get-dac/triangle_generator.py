import time

def get_tri_wave_amplitude(freq, t):
    # Вычисляем период (сколько времени длится один цикл волны)
    period = 1.0 / freq
   
    # Берем остаток от деления времени на период, чтобы "зациклить" время от 0 до period
    t_mod = t % period
   
    # Если прошло меньше половины периода — волна растет от 0 до 1
    if t_mod < (period / 2):
        return t_mod / (period / 2)
    # Если больше половины — волна падает от 1 до 0
    else:
        return 1.0 - ((t_mod - (period / 2)) / (period / 2))

def wait_for_sampling_period(sampling_frequency):
    # Просто спим нужное количество секунд между семплами
    time.sleep(1.0 / sampling_frequency)

