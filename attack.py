import subprocess

targets = {
    "gruyere": "https://google-gruyere.appspot.com/395276411553556759049058387665397034987/",  # My gruyere instance
    "tyrak": "https://tyrak.bufonu.com/",  # Personal website
    "bufonu": "https://bufonu.com/",  # Personal website
}

for target_name, target_url in targets.items():
    subprocess.run(
        [
            "wapiti",
            "-u",
            target_url,
            "-f",
            "html",
            "-o",
            f"{target_name}_wapiti_report.html",
        ],
        check=True,
    )
