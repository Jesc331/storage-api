from json import dumps as json_dumps
from modules.auth import validate_token, auth_required
import bottle

app = bottle.Bottle()

@app.get("/main/home")
def display_page(*args, **kwargs):
    bottle.response.status_code = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Not implemented")

@app.get("/main/home/<image_id>")
def get_profile(*args, code = None, **kwargs):
    # codigo
    return dict(code = 501, message = "Not implemented")

@app.get("/main/profile/user_home/<user_id>")
def update_record(*args, code = None, **kwargs):
    # Codigo
    return dict(code = 501, message = "Not implemented")

@app.delete("/main/profile/delete/<image_id>")
def delete_images(*args, code = None, **kwargs):
    # Codigo
    return dict(code = 501, message = "Not implemented")

@app.post("/main/profile/reportTools")
def create_reports(*args, **kwargs):
    # Codigo
    return dict(code = 501, message = "Not implemented")

@app.post("/auth/user_storage/<data>")
def create_profile(*args, **kwargs):
    # Codigo
    return dict(code = 501, message = "Not implemented")

@app.get("/main/profile/reportTools/<report_id>")
def get_info_by_id(*args, **kwargs):
    # Codigo
    return dict(code = 501, message = "Not implemented")
