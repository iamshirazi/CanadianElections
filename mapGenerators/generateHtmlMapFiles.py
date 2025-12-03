from jinja2 import Environment, FileSystemLoader

def generateElectionMapFile(electionYear):
    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('electionMapTemplate.jinja')
    output = template.render(electionYear = str(electionYear))
    # print(output)
    with open("pages/elections/" + str(electionYear) + ".html", 'w') as f:
        print(output, file = f)
