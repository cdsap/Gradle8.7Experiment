workers = [2]
gc_gradle = ["-XX:+UseG1GC", "-XX:+UseParallelGC"]
heap_gradle = ["-Xmx4g", "-Xmx6g", "-Xmx8g"]
heap_kotlin = ["-Xmx4g", "-Xmx6g", "-Xmx8g"]
kc_gradle = ["-XX:+UseG1GC", "-XX:+UseParallelGC"]
repetitions = 5  # Ensure this applies to all combinations

combinations = []
for worker in workers:
    for gc_g in gc_gradle:
        for kc_g in kc_gradle:
            for heap_g in heap_gradle:
                for heap_k in heap_kotlin:
                    for rep in range(repetitions):  # Apply repetitions to all
                        combinations.append({
                            "WORKERS": str(worker),
                            "GC_GRADLE": gc_g,
                            "HEAP_GRADLE": heap_g,
                            "KC_GRADLE": kc_g,
                            "HEAP_KOTLIN": heap_k,
                            "REPETITION": rep + 1
                        })

# Print the JSON string to be used in the workflow
print(json.dumps({"include": combinations}))
