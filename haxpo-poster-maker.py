from flask import Flask
from collections import namedtuple

app = Flask(__name__)
all_projects = []

Project = namedtuple('Project', ["HXID", "HDID", "Deleted", "Idea", "InSF", "InHaxpoInSF", "FilmCategory", "LoneWolf", "Name", "Creator", "Members", "Landmark", "DeclaredLandmark", "Zone", "Notes", "ShortName"])

@app.route('/')
def hello_world():
    to_return = '''
<html>
<head>
<style>
@font-face {
  font-family: "Founders Grotesk";
  font-weight: normal;
  font-style: normal;
  }
@font-face {
  font-family: "Founders Grotesk";
  font-weight: lighter;
  font-style: italic;
  }
@font-face {
  font-family: "Founders Grotesk";
  font-weight: 500;
  font-style: normal;
  }
@font-face {
  font-family: "Founders Grotesk";
  font-weight: 700;
  font-style: normal;
  }
@font-face {
  font-family: "Founders Grotesk X-Condensed";
  font-weight: 700;
  font-stretch: condensed;
  font-style: normal;
  }

.orange { color: #F04F22;}
.navy { color: #231E54;}
.pink { color: #D81961;}
#page {
  position: relative;
  width: 11in;
  height: 4in;
  font-family: "Founders Grotesk";
  font-weight: bold;
  page-break-after: always;
}
#number {
  position: absolute;
  font-size: 2in;
  left: 7.9in;
  top: 0in;
}
#name {
    font-size: 0.9in;
    top: 2.8in;
    position: absolute;
    width: 7.2in;
    text-align: center;
    left: 1.2in;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 4.5in;
}
</style>
</head>
<body>
'''


# - orange "zone 1"(75each)
# - navy "zone 2" (75)
# - pink "zone 3" (75)

    zone='1'
    color_map = {'1': 'orange',
                 '2': 'navy',
                 '3': 'pink'}
    presenting = [project for project in all_projects if project.InHaxpoInSF is True and 1000 > int(project.HXID) > 0]

    for project in presenting:
        project_template = '''
        <div id="page">
              <div id="number" class="%(color)s">
                %(hxid)s
              </div>
              <div id="name" class="%(color)s">
                <div class="inner-name">
                %(shortname)s
                </div>
              </div>
            </div>
        ''' % {'hxid': project.HXID, 'shortname': project.ShortName, 'color': color_map[zone]}
        print project
        to_return += project_template

    return to_return




if __name__ == '__main__':
    f = open('/Users/chris/Documents/workspace/haxpo-poster-maker/data.tsv')
    lines = f.readlines()
    for line in lines:
        data = []
        for v in line.split("\t"):
            if v in ["TRUE", "FALSE"]:
                if v == "TRUE":
                    v = True
                else:
                    v = False
            data.append(v)
        all_projects.append(Project(*data))

    app.debug = True
    app.run()
