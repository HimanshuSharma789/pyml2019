import web

urls = (
    '/', 'Home'
)

app = web.application(urls, globals())
render = web.template.render('')


class Home:
    def GET(self):
        return render.gui_home()

    def POST(self):
        return web.input()


if __name__ == "__main__":
    app.run()
