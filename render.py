from jinja2 import Template, Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath = "./")
templateEnv = Environment(loader = templateLoader)
templateFile = ("template2.j2")
template = templateEnv.get_template(templateFile)

data = {
    "packages": ["terraform", "gomod"],
    "intervals": ["daily", "daily"] 
}

output = template.render(data)

print(output)