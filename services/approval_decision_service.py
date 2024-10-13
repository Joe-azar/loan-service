from spyne import Application, rpc, ServiceBase, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class ApprovalDecisionService(ServiceBase):
    
    @rpc(Float, Float, Float, _returns=Unicode)
    def make_decision(ctx, solvency_score, property_value, loan_amount):
        # Simple approval logic: if solvency score and property value are greater than loan amount
        if solvency_score > 1000 and property_value >= loan_amount:
            return "Loan Approved"
        else:
            return "Loan Rejected"

# Créer l'application Spyne
application = Application([ApprovalDecisionService],
                          tns='approval_decision_service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8004, wsgi_application)
    print("Approval Decision Service started on http://localhost:8004")
    server.serve_forever()
