import sqlite3, json
conn = sqlite3.connect("manga_prompts.db")
cur = conn.cursor()
cur.execute("SELECT id, status, current_step FROM jobs")
for row in cur.fetchall():
    print("Job:", row)
cur.execute("SELECT id, scene_id, asset_type, generation_metadata FROM assets")
for row in cur.fetchall():
    meta = json.loads(row[3]) if row[3] else {}
    print(f"Asset {row[0]} (scene {row[1]}): type={row[2]}")
    if "manga_analysis" in meta:
        print("  Analysis:", json.dumps(meta["manga_analysis"], indent=2)[:300])
    if "prompt" in meta:
        print("  Prompt:", meta["prompt"][:150])
cur.execute("SELECT id, description, duration FROM scenes")
for row in cur.fetchall():
    print(f"Scene {row[0]}: desc='{row[1]}', duration={row[2]}")
conn.close()
