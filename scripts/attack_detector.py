SQLI = [
    "union",
    "or+1=1",
    "--"
]

TRAVERSAL = [
    "../",
    "etc/passwd",
    "boot.ini",
    "win.ini"
]

def detect_sqli(df):

    return df[
        df["Request"]
        .str.lower()
        .str.contains("|".join(SQLI))
    ]

def detect_traversal(df):

    return df[
        df["Request"]
        .str.lower()
        .str.contains("|".join(TRAVERSAL))
    ]