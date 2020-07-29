from django.views import View
# original view class 
class JsonView(View):
    def echo_json(self):
        return {"name": "JSON VIEW"}

