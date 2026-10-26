import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

steps_to_view = [7, 196, 279, 579, 628, 775, 796, 966, 1375, 1643, 2174]
with open(r"C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") in steps_to_view and data.get("type") == "USER_INPUT":
            print(f"=== STEP {data.get('step_index')} ===")
            print(data.get("content"))
