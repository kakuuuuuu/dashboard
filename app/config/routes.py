from system.core.router import routes

routes['default_controller'] = 'home'
routes['/login']='home#login'
routes['/register']='home#register'
