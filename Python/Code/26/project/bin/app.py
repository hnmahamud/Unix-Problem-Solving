import web
urls = (
'/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.form()

    def POST(self):
        form = web.input(PostName = '')
        post_name = form.PostName

        file = open('test.txt', 'r')
        Line = file.readline()
        Lines = file.readlines()

        list = []
        counter = 0
        for line in Lines:
            lowLine = line.lower()
            lowPost = post_name.lower()
            if lowPost in lowLine:
                list.append(line.strip())
                counter = counter + 1

        return render.index(list = list, counter = counter)

if __name__ == "__main__":
    app.run()
