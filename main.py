"""renderer_63a6cf - Async task runner."""
import asyncio, os
TAG = "renderer_63a6cf"
async def task(name: str, delay: float = 0.1):
    print(f"[{TAG}] Task '{name}' started")
    await asyncio.sleep(delay)
    print(f"[{TAG}] Task '{name}' finished")
    return {"task": name, "status": "done"}
async def run_all():
    tasks = [task(f"step_{i}") for i in range(3)]
    return await asyncio.gather(*tasks)
def main():
    print(f"[{TAG}] Launching async tasks...")
    results = asyncio.run(run_all())
    for r in results: print(f"  -> {r}")
    print(f"[{TAG}] All tasks completed.")
if __name__ == "__main__":
    main()
