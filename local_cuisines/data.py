def wesley_journal():
    greeting = "Wesley and Naweid's Journal"
    embed = "https://docs.google.com/document/d/15XZWCyArc6Fv6Ywa5bqmP_nOSDWnGqM-ursyV09_FxM/edit"
    info = {"greeting": greeting, "embed": embed}
    return info

def andrea_journal():
    greeting = "Andrea, Ethan, Diego's Journal"
    embed = "https://docs.google.com/document/d/1QPwyc1Xuv9RBLs38YVvEXeJLtfcbk_punZXeIJM1wcw/edit"
    info = {"greeting": greeting, "embed": embed}
    return info

def flask_projectplan():
    greeting = "Flask Series Project Plan"
    embed = "https://docs.google.com/document/d/1VJz3bjcGSNatEY4aVoDGxhfeJRwPQQI6zGf2Ji53uDk/edit"
    info = {"greeting": greeting, "embed": embed}
    return info

def flask_project():
    greeting = "Flask Series Travel Wesbite Project"
    embed = "http://127.0.0.1:5000/france/"
    info = {"greeting": greeting, "embed": embed}
    return info

def hello_projectplan():
    greeting = "Hello Series Project PLan"
    embed = "https://docs.google.com/document/d/1n8XvhfdLlLcQkmsrgegQgb6QPyclnFSn_wVakUGTJAo/edit"
    info = {"greeting": greeting, "embed": embed}
    return info

def hello_project():
    greeting = "Hello Series Shop Game Project"
    embed = "https://repl.it/@AndreaAbed/copyofnewbiecodershop?lite=true"
    info = {"greeting": greeting, "embed": embed}
    return info

def alldata():
    return [wesley_journal(), andrea_journal(), flask_projectplan(), flask_project(), hello_projectplan(), hello_project()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Nighthawk Coding"
    github = "https://github.com/nighthawkcoders"
    linkedin = "https://www.linkedin.com/in/john-mortensen-1021/"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    twitter = "https://twitter.com/NighthawkCoding"
    source = {"name": name, "github": github, "linkedin": linkedin, "youtube": youtube, "twitter": twitter}
