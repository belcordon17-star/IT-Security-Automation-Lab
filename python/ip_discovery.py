import subprocess

devices = [
    "192.168.1.1",
    "192.168.1.10"
]

for ip in devices:
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    status = "ONLINE" if result.returncode == 0 else "OFFLINE"

    print(f"{ip}: {status}")
