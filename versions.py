import json

# Initial variables and their values
workers = [2]
gc_gradle = ["-XX:+UseG1GC", "-XX:+UseParallelGC"]
heap_gradle = ["-Xmx4g", "-Xmx6g", "-Xmx8g", "-Xmx10g"]
repetitions = 30

combinations = []
for worker in workers:
    for gc in gc_gradle:
        for heap in heap_gradle:
            for rep in range(repetitions):
                combinations.append({
                    "WORKERS": str(worker),
                    "GC_GRADLE": gc,
                    "HEAP_GRADLE": heap,
                    "REPETITION": rep + 1  # Repetition number (1-30)
                })

# Print the JSON string to be used in the workflow
print(json.dumps({"include": combinations}))
