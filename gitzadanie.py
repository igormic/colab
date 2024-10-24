def is_critically_balanced(temperature, neutrons_emitted_per_second):
    if (temperature < 800 and
        neutrons_emitted_per_second > 500 and
        temperature * neutrons_emitted_per_second < 500000):
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "zielone"
    elif efficiency >= 60:
        return "pomaranczowe"
    elif efficiency >= 30:
        return "czerwone"
    else:
        return "czarne"

def fail_safe(temperature, neutrons_emitted_per_second, threshold):
  critically_value = temperature * neutrons_emitted_per_second

  if critically_value < 0.9 * threshold:
   return "low"
  elif 0.9 * threshold <= critically_value <= 1.1 * threshold:
   return "normal"
  else:
   return "high"

print(is_critically_balanced(500, 700))
print(is_critically_balanced(300, 400))

print(reactor_efficiency(30, 40, 50000))
print(reactor_efficiency(500, 200, 120000))

print(fail_safe(900, 800, 600000))
