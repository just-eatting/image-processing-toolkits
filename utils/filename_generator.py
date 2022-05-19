import uuid


def generate_filename(prefix: str = "", suffix: str = ""):
    s = str(uuid.uuid4())
    s.replace("-", "")
    return prefix + s + suffix


def generate_imagename(suffix: str = ".jpg"):
    if suffix not in [".jpg", ".png", ".jpeg"]:
        suffix = ".jpg"
    return generate_filename(suffix=suffix)
