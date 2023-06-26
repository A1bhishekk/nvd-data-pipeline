
ext_map = {
    "Objective-C": {"m", "mm"},
    "Java": {"java", "jsp", "jspf"},
    "Scala": {"scala"},
    "C/C++": {
        "c",
        "cc",
        "cxx",
        "cpp",
        "hpp",
        "c++",
        "h",
        "hh",
        "cppm",
        "ixx",
        "cp",
        "inl",
    },
    "Groovy": {"groovy"},
    "PHP": {"php", "tpl", "inc", "ctp", "phpt", "phtml"},
    "JavaScript": {"js", "jsx", "coffee"},
    "Python": {"py"},
    "Config files": {"lock", "gradle", "json", "config", "yaml", "conf"},
    "Ruby": {"rb"},
    "HTML": {"html", "erb"},
    "Perl": {"pm"},
    "Go": {"go"},
    "Lua": {"lua"},
    "Erlang": {"erl"},
    "C#": {"cs"},
    "Rust": {"rust"},
    "Vala": {"vala"},
    "SQL": {"sql"},
    "XML": {"xml"},
    "Shell": {"sh"},
}



def get_key(val):
    for key, value in ext_map.items():
        if val in value:
            return key


print(get_key("app.js"))