import psutil
import datetime


# List of keywords that often appear in suspicious / spying program names.
# This is just for education – NOT a real antivirus engine.
SUSPICIOUS_KEYWORDS = [
    "keylog",
    "logger",
    "spy",
    "stealth",
    "monitor",
    "sniff",
    "capture",
    "hook"
]


def is_suspicious_process(proc: psutil.Process) -> bool:
    """
    Check if a process looks suspicious based on its name, executable path
    or command line containing certain keywords.
    """
    try:
        name = (proc.name() or "").lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        name = ""

    try:
        exe = (proc.exe() or "").lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        exe = ""

    try:
        cmdline_list = proc.cmdline() or []
        cmdline = " ".join(cmdline_list).lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        cmdline = ""

    combined_text = " ".join([name, exe, cmdline])

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in combined_text:
            return True

    return False


def scan_processes():
    """
    Scan all running processes and return:
    - a list of (process_info_dict, is_suspicious_boolean)
    - a separate list of only suspicious process info dicts
    """
    all_results = []
    suspicious_results = []

    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            info = proc.as_dict(attrs=["pid", "name"])
            suspicious = is_suspicious_process(proc)
            all_results.append((info, suspicious))
            if suspicious:
                suspicious_results.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Process may have ended or we don't have permissions – skip it
            continue

    return all_results, suspicious_results


def print_report(all_results, suspicious_results):
    """
    Print a nicely formatted report to the console.
    """

    print("=" * 60)
    print("       KEYLOGGER DETECTION SIMULATOR - PROCESS SCAN")
    print("=" * 60)
    print(f"Scan time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total processes found: {len(all_results)}")
    print(f"Suspicious processes flagged: {len(suspicious_results)}")
    print("-" * 60)

    # Show suspicious processes first
    if suspicious_results:
        print("\n[!] Suspicious processes:")
        for info in suspicious_results:
            print(f"    PID: {info['pid']:>6} | Name: {info['name']}")
    else:
        print("\n[+] No suspicious processes detected based on simple rules.")

    print("\nDetails of all processes (S = suspicious, . = normal):")
    print("-" * 60)

    for info, suspicious in all_results:
        flag = "S" if suspicious else "."
        print(f"{flag}  PID: {info['pid']:>6} | Name: {info['name']}")

    print("-" * 60)
    print("NOTE: This is an educational tool.")
    print("      Real keyloggers can hide better and may not be detected by simple name-based rules.\n")


def main():
    print("Starting Keylogger Detection Simulator...")
    print("Scanning running processes. Please wait...\n")

    all_results, suspicious_results = scan_processes()
    print_report(all_results, suspicious_results)


if __name__ == "__main__":
    main()
