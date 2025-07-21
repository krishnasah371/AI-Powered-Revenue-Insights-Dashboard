
import subprocess
import time

print("⏳ Running simulated Azure Data Factory job...")
time.sleep(1)

# Simulate triggering the blob upload
subprocess.run(["python", "simulate_blob_upload.py"])
print("✅ Data refresh completed by simulated Data Factory.")
