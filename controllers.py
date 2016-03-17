# -*- coding: utf-8 -*-
from openerp import http

# class Simpletodo(http.Controller):
#     @http.route('/simpletodo/simpletodo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simpletodo/simpletodo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simpletodo.listing', {
#             'root': '/simpletodo/simpletodo',
#             'objects': http.request.env['simpletodo.simpletodo'].search([]),
#         })

#     @http.route('/simpletodo/simpletodo/objects/<model("simpletodo.simpletodo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simpletodo.object', {
#             'object': obj
#         })