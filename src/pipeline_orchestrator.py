import subprocess
import sys
import time

pipeline_steps = [
    "generate_synthetic_data.py",
    "data_ingestion.py",
    "data_validation.py",
    "data_transformation.py",
    "load_to_postgresql.py"
]

print("=" * 70)
print("        NECTAR IoT DATA PIPELINE ORCHESTRATION")
print("=" * 70)

pipeline_start = time.time()

for step in pipeline_steps:

    print(f"\nRunning: {step}")

    start = time.time()

    result = subprocess.run(
        [sys.executable, f"src/{step}"],
        text=True
    )

    end = time.time()

    if result.returncode == 0:
        print(f"SUCCESS - {step}")
        print(f"Execution Time: {end-start:.2f} seconds")
    else:
        print(f"FAILED - {step}")
        print("Stopping Pipeline...")
        sys.exit(1)

pipeline_end = time.time()

print("\n" + "=" * 70)
print("PIPELINE COMPLETED SUCCESSFULLY")
print(f"Total Execution Time: {pipeline_end-pipeline_start:.2f} seconds")
print("=" * 70)