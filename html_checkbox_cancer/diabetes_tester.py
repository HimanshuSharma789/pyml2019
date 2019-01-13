import ml_script
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
        data = web.input()
        seq_data = (data.preg, data.plas, data.pres, data.skin, data.test, data.mass, data.pedi, data.age)
        result = ml_script.ml_script().result(seq_data)
        if result:
            return "Positive"
        else:
            return "Negative"


if __name__ == "__main__":
    app.run()
