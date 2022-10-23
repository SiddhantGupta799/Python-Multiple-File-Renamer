import os
import components as cp

_dir_path = ""
os.chdir(_dir_path)


def remove_extras(name: str) -> str:
    name = cp.remove_youtube_tags(name)
    name = cp.remove_date(name)
    # name = cp.remove_brackets(name)
    name = cp.remove_underscores(name)
    name = cp.remove_hyphens(name)
    name = cp.remove_links(name)
    """ Write custom filters below this """

    """ And Above this """
    # name = cp.remove_periods(name)
    return cp.remove_redundant_spaces(name).strip()


def filter_name(name: str) -> str:
    name = name.replace("-", " ").strip()
    vec: list = name.split(".")
    for i in range(1, len(vec)):
        vec[i] = list(vec[i].strip())
        vec[i] = ".".join(vec[i])
        vec[i] = '.' + vec[i] + '.'
    name = ". ".join(vec)

    """ Do your Own Filters here before going into regex engine. """
    # return remove_extras(name).strip().title()
    return name


for f in os.listdir():
    f_, f_ext = os.path.splitext(f)
    new_name = f"{filter_name(f_)}{f_ext}"
    print("Original Name: \t", f)
    print("New Name: \t\t", new_name)
    # os.rename(f, new_name)

