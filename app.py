from dash import Dash, html
import dash_auth
import flask

# 配置用户和密码
USERNAME_PASSWORD_PAIRS = [
    ['admin', 'yourpassword'],
    ['guest', 'guest123']
]

# 创建 Flask 和 Dash 实例
server = flask.Flask(__name__)
app = Dash(__name__, server=server)

# 启用 Basic 认证
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)

# 应用内容
app.layout = html.Div([
    html.H1("🌍 Welcome to the Global Dash App!"),
    html.P("This app is protected by username and password."),
    html.Ul([
        html.Li("User 1: admin / yourpassword"),
        html.Li("User 2: guest / guest123")
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
