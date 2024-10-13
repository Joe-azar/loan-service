from spyne import Application, rpc, ServiceBase, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class SolvencyCheckService(ServiceBase):
    
    @rpc(Unicode, Float, Float, _returns=Float)
    def check_solvency(ctx, name, monthly_income, monthly_expenses):
        # Simple solvency check: revenu - dépenses
        solvency_score = monthly_income - monthly_expenses
        return solvency_score

# Créer l'application Spyne
application = Application([SolvencyCheckService],
                          tns='solvency_check_service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8002, wsgi_application)
    print("Solvency Check Service started on http://localhost:8002")
    server.serve_forever()
