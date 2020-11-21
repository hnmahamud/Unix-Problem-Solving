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
        form = web.input(BookName = '', AuthorName = '', Price = '')
        book_name = form.BookName
        author_name = form.AuthorName
        price = form.Price

        p = 15 / 100
        y = p * int(price)
        final_price = int(price) - y


        allInfo = [book_name, author_name, final_price]

        return render.index(allInfo = allInfo)

if __name__ == "__main__":
    app.run()
