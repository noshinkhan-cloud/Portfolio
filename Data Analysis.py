import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = [["Activity before Sleeping", "Light", "Sound", "Total time"],
["Phone", "Dim", "No sound", "9"], ["Book", "Dim", "Medium", "9.9"],
["Phone", "No light", "Medium", "10"],
 ["Book", "Dim", "No sound", "10.2"], ["Phone", "Dim", "Low", "9.8"],
["Book", "Dim", "No sound",  '10.3'], ["Book", "Bright", "Medium", "8.3"],
["Book", "No light", "No sound", "10.8"],
["Phone", "No light", "Low", "10"], ["Phone", "Dim", "No sound", "9"],
 ["Book", "Bright", "No sound", "10"], ["Book", "Dim", "High", "11"],
["Phone", "No light", "Low", "9"],
 ["Phone", "Bright", "No sound", "10"], ["Book", "Dim", "Medium", "9"],
["Phone", "Dim", "No sound", "9"]]

df = pd.DataFrame(data)

print(df)

time_vs_sound = {}
for row in data[1:]:
    total_time = float(row[3])
    sound = row[2]
    if sound in time_vs_sound:
        time_vs_sound[sound].append(total_time)
    else:
        time_vs_sound[sound] = [total_time]

print("\nTotal time slept vs sound:")
for notes, times in time_vs_sound.items():
    print(f"Sound: {notes}, Total time: {sum(times) / len(times):.2f} hours")

plt.bar(list(time_vs_sound.keys()),
        [sum(times) / len(times) for times in time_vs_sound.values()])

plt.xlabel('Sound')

plt.ylabel('Total time slept')

plt.title('Total time slept vs Sound')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()
